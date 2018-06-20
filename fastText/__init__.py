# ai/__init__.py

import os
from flask import Flask, jsonify, Blueprint
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
from fastText.api.restplus import api
from fastText.api.views import ns as ot_events_namespace

from flask_cors import CORS




import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def create_app():

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CORS(app)
    blueprint = Blueprint('api', __name__)
    # instantiate the app
    api.init_app(blueprint)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # register namespace
    api.add_namespace(ot_events_namespace)
    app.register_blueprint(blueprint)
    return app
