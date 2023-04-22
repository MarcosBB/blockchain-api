from flask_restful import Resource
from ..server.instance import server, blockchain
app, api = server.app, server.api


class MineBlock(Resource):
    def get(self):
        block = blockchain.createBlock()
        return {"block": block}, 201

api.add_resource(MineBlock, '/mine/')