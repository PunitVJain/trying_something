#  flask routes.
from logging import debug
from flask import Flask, request
from flask_restful import Api, Resource
app =  Flask(__name__)
api = Api(app)

class FirstAPI(Resource):

    def get(self):
        return "Hello, to Flask REST-API"
    
    def post(self):
        return({"first": "Start with REST"})
    

api.add_resource(FirstAPI, "/api/helloworld")

if __name__ == "__main__":
    app.run(debug=True, port= 3300)
