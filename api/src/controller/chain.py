from flask_restful import Resource
from ..server.instance import server, blockchain
app, api = server.app, server.api
            

class GetChain(Resource):
    def get(self):
        return {"chain": blockchain.chain}, 200

api.add_resource(GetChain, '/chain/')