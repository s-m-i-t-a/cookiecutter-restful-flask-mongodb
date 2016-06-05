# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix

from config.blueprints import register_blueprints
from signals import register_signals
from utils import get_api_version

__version__ = '0.1.0'

db = MongoEngine()


def create_app(configuration='Production'):
    settings = 'config.settings.%s' % configuration

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)  # fix ssl urls on heroku
    app.config.from_object(settings)

    app.config['API_URL'] = get_api_version(app, __version__.rsplit('.', 1)[0])
    db.init_app(app)

    register_blueprints(app)
    register_signals(app)

    return app
