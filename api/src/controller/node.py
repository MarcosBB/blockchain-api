from flask import request
from flask_restful import Resource
from ..server.instance import server, blockchain
app, api = server.app, server.api


class CreateNode(Resource):
    def post(self):
        name = request.get_json()['name']
        created = blockchain.createNode(name)
        if created:
            return {"message": "Nó criado"}, 201
        else:
            return {"message": "Nó já existe"}, 400


class ResolveConflicts(Resource):
    def get(self):
        resolved = blockchain.resolveConflicts()
        if resolved:
            return {"message": "Conflitos resolvidos"}, 200
        else:
            return {"message": "Não existem conflitos"}, 400


api.add_resource(CreateNode, '/nodes/register/')
api.add_resource(ResolveConflicts, '/nodes/resolve/')