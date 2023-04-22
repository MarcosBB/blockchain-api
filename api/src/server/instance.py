from flask import Flask
from flask_restful import Api
from blockchain.blockchain import Blockchain


class ServerInstance():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.blockchain = Blockchain()

    def run(self, port=5000):
        self.app.run(debug=True, port=port)

server = ServerInstance()
blockchain = server.blockchain