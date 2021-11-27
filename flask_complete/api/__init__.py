from flask_restful import Api
from app import flaskappinstance
from .Task import Task

RestServer =  Api(flaskappinstance)



RestServer.add_resource(Task, "/api/v1.0/task")
