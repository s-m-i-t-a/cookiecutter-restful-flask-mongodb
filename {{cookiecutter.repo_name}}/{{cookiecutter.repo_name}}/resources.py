# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

# from bar.foo import FooResource


def api_urls(app):
    urls = Blueprint('api', __name__)

    api = Api()
    api.init_app(urls)

    # URLs
    # Tokens
    # api.add_resource(FooResource, '/foo')

    return urls
