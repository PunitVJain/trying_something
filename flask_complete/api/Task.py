# class of the API
from flask_restful import Resource
import logging as logger
from flask import jsonify

class Task(Resource):

    def get(self):
        logger.debug("Inside get method")
        return jsonify({"message": "started get method", "status_code": 200})

    def post(self):
        logger.debug("Inside post method")
        return jsonify({"message": "started post method", "status_code": 200})

    def put(self):
        logger.debug("Inside put method")
        return jsonify({"message": "started put method", "status_code": 200})

    def delete(self):
        logger.debug("Inside delete method")
        return jsonify({"message": "started delete method", "status_code": 200})
