from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flaskappinstance = Flask(__name__)




if __name__ =="__main__":
    logger.debug("Starting the app")
    from api import *
    flaskappinstance.run(host="0.0.0.0",port=5000,debug=5000, use_reloader=True)

