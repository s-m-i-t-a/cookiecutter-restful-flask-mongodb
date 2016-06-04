# -*- coding: utf-8 -*-

import os.path

from .utils import get_dtb_config, getenv


class BaseConfig(object):
    '''
    Base settings for {{cookiecutter.project_name}} project.
    '''

    DEBUG = False

    TESTING = False

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    SECRET_KEY = getenv('SECRET_KEY')

    # Databases uri string (e.g. mongodb://localhost/wsys)
    MONGODB_SETTINGS = get_dtb_config(getenv('DATABASE_URL'))

    # API URL prefix
    API_URL_TEMPLATE = '/api/v%s'

    TOKEN_EXPIRE_TIME = 24 * 60 * 60

    AWS_REGION = getenv('AWS_REGION', 'eu-west-1')
    AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')

    AMZ_ACL_HEADERS = {
        'x-amz-acl': 'public-read',
    }

    MAIL_SERVER = getenv('MAIL_SERVER', 'localhost')
    MAIL_PORT = getenv('MAIL_PORT', 25)
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = getenv('MAIL_DEFAULT_SENDER')


class Production(BaseConfig):
    pass


class Development(BaseConfig):
    '''
    Development settings.
    '''
    DEBUG = True


class Testing(BaseConfig):
    '''
    Testing settings.
    '''

    TESTING = True
    LOGIN_DISABLED = False

    # pro testy neni potreba
    WTF_CSRF_ENABLED = False

    MONGODB_SETTINGS = get_dtb_config("mongodb://localhost/{{cookiecutter.repo_name}}_test")
