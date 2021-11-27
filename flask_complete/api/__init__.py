from flask_restful import Api
from app import flaskappinstance
from .TaskByID import TaskByID
from .Task import Task

RestServer =  Api(flaskappinstance)



RestServer.add_resource(Task, "/api/v1.0/task")
RestServer.add_resource(TaskByID,"/api/v1.0/taskbyid/<string:taskid>")