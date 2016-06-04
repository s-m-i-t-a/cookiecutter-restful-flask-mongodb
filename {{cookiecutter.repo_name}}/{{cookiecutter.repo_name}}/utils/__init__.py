# -*- coding: utf-8 -*-
from flask import jsonify


def abort_json(code, message):
    '''
    Return response with given code and message as JSON.
    '''
    response = jsonify({'status': code, 'message': message})
    response.status_code = code
    return response


def get_api_version(app, version):
    return app.config['API_URL_TEMPLATE'] % version
