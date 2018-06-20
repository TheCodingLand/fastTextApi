# project/api/views.py
from flask_restplus import Namespace, Resource, fields

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

from flask import request

from fastText.api.restplus import api
from fastText.api.models.apimodels import predict, training, model, loadmodel
from fastText.app.fastTextApp import fastTextApp

# these hold our data model folder, fields list, required fields
import time

ft = fastTextApp()

ns = api.namespace('/', description='Api for Fasttext')


@ns.route('/schema')
class Swagger(Resource):
    def get(self):
        return api.__schema__


@ns.route('/ping')
class SanityCheck(Resource):
    def get(self):
        # log.info(json.dumps(api.__schema__))
        return {
            'status': 'success',
            'message': 'pong!'
        }


@api.response(400, 'failed.')
@ns.route('/load', methods=['POST'])
class load(Resource):
    @api.response(201, 'loaded : ok')
    @api.expect(loadmodel) #name, version, supervised, quantized
    def post(self):
        post_data = request.get_json()
        log.error(f"loading {post_data.get('name')} {post_data.get('version')}")
        
        result = ft.loadModel(name=post_data.get('name'), \
                             version=post_data.get('version'), \
                             supervised = post_data.get('supervised'), \
                             quantized = post_data.get('quantized'))
        
        if result == "success":
            response_object = {
                    'status': 'success',
                    'results': result 
                }
            return response_object, 201
        else:
            response_object = {
                    'status': 'fail',
                    'message': result
            }
            return response_object, 500


@api.response(400, 'failed.')
@ns.route('/predict', methods=['POST'])
class load(Resource):
    @api.response(201, 'prediction : ok')
    @api.expect(predict) #modelname, (version), text, nbofresults
    def post(self):

        post_data = request.get_json()
        name=post_data.get('name')
        try:
            version=post_data.get('version')
        except:
            version=0

        text = post_data.get('text')
        nbofresults = post_data.get('nbofresults')
        result = ['error','']
        for model in ft.loadedmodels:
            
            if model.name == name and model.version == version:
                log.error(f"found {model.name} {model.version!s}")
                result = model.predict(text,nbofresults)


                
       
        if result[0] == "error":
            response_object = {
                    'status': 'error',
                    'results': result[1] 
                }
            return response_object, 500
        
        else:
            response_object = {
                    'status': 'success',
                    'results': result 
                }
            return response_object, 201
        