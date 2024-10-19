import base64
from web3 import Web3
from flask import Flask, request, jsonify
import os
import importlib.util
import pandas as pd
import pickle

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = './uploads'
app.config['DATA_FOLDER'] = './data'
app.config['MODEL_FOLDER'] = './models'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)
os.makedirs(app.config['MODEL_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/model_upload', methods=['POST'])
def model_upload():
    data = request.get_json()
    fname = data.get('name')
    fdata = data.get('data')

    if not fname or not fdata:
        return jsonify({'error': 'file name or data is missing,try reuploading the file'}), 400

    fbin = base64.b64decode(fdata)

    fpath = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    with open(fpath, 'wb') as f:
        f.write(fbin)

    return jsonify({'message': 'Yaay Lezzgo, File uploaded and saved successfully', 'filepath': fpath}), 200


@app.route('/train_model', methods=['POST'])
def train_model():
    mname = request.json.get('model_file')
    dname = request.json.get('dataset_name')

    if not mname or not dname:
        return jsonify({'error': 'Error fetching model or dataset'}), 400

    mpath = os.path.join(app.config['UPLOAD_FOLDER'], mname)
    dpath = os.path.join(app.config['DATA_FOLDER'], dname)

    if not os.path.exists(mpath):
        return jsonify({'error': f'Model named {mname} not found'}), 404

    if not os.path.exists(dpath):
        return jsonify({'error': f'Dataset named {dname} not found'}), 404

    dataset = pd.read_csv(dpath)

    model = load_model_from_py(mpath)

    trained_model = model.train_model(dataset)

    trained_model_path = os.path.join(app.config['MODEL_FOLDER'], 'trained_model.pkl')
    with open(trained_model_path, 'wb') as f:
        pickle.dump(trained_model, f)

    with open(trained_model_path, 'rb') as f:
        modelbin = f.read()

    modelb64 = base64.b64encode(modelbin).decode('utf-8')
    os.remove(trained_model_path)
    os.remove(dpath)
    os.remove(mpath)
    return jsonify({'message': 'Hurrah , Model has been trained successfully', 'model': modelb64}), 200


def load_model_from_py(filepath):
    spec = importlib.util.spec_from_file_location('custom_model', filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module



if __name__ == '__main__':
    app.run(debug=True)

