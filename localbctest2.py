from flask import Flask, jsonify, request
from pytezos import pytezos
# @app.route('/call_contract_method', methods=['POST'])
def call_contract_method():
    data = request.json

    contract = pytezos.contract(contract_address)

    response = contract.some_method_name(data.get('param1'), data.get('param2')).send()

    return jsonify(response)

call_contract_method()