# class of the API
from flask_restful import Resource
import logging as logger
from flask import jsonify

class TaskByID(Resource):

    def get(self, taskid):
        logger.debug("Inside get method")
        return jsonify({"message": "started get method of TaskByID", "status_code": 200, "taskid": taskid})
    
    def post(self, taskid):
        logger.debug("Inside post method")
        return jsonify({"message": "started post method of TaskByID", "status_code": 200, "taskid": taskid})
    
    def put(self, taskid):
        logger.debug("Inside put method")
        return jsonify({"message": "started put method of TaskByID", "status_code": 200, "taskid": taskid})
    
    def delete(self, taskid):
        logger.debug("Inside delete method")
        return jsonify({"message": "started delete method of TaskByID", "status_code": 200, "taskid": taskid})
        