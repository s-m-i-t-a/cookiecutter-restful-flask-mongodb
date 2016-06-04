# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.ext import restful

# from bar.foo import FooResource


def api_urls(app):
    urls = Blueprint('api', __name__)

    api = restful.Api()
    api.init_app(urls)

    # URLs
    # Tokens
    # api.add_resource(FooResource, '/foo')

    return urls
