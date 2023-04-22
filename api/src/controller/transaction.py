from flask import request
from flask_restful import Api, Resource
from datetime import datetime
from ..server.instance import server, blockchain
app, api = server.app, server.api
from api.src.validator import base_validator


class CreateTransactionValidator(base_validator):
    data_names = ['sender', 'recipient', 'amount', 'data', 'privateKey']

    def validate(self, data):
        errors = []
        try:
            res = bool(datetime.strptime(data['data'], "%d/%m/%Y"))
        except:
            errors.append('Invalid date format. Must be dd/mm/yyyy')

        return errors
            

class CreateTransaction(Resource):
    def post(self):
        data = request.get_json()
        validator = CreateTransactionValidator(request)
        if validator.is_valid():
            date = datetime.timestamp(datetime.strptime(data['data'], "%d/%m/%Y"))
            try:
                transaction = blockchain.createTransaction(
                    sender=data['sender'],
                    recipient=data['recipient'],
                    amount=data['amount'],
                    timestamp=date,
                    privWifKey=data['privateKey']
                )
                return {'transaction': transaction}, 201

            except Exception as e:
                return {'message': str(e)}, 400
        else:
            return {
                'message':'Validation error', 
                'errors': validator.get_errors()}, 400


class GetMemoryPoolTransactions(Resource):
    def get(self):
        return {"memory_pool": blockchain.memPool}, 200


api.add_resource(CreateTransaction, '/transactions/create/')
api.add_resource(GetMemoryPoolTransactions, '/transactions/mempool/')