# -*- coding: utf-8 -*-


def register_blueprints(app):
    '''
    Place your blueprints import here.

    E.g.

    from intiny.catalog.blueprints import catalogs
    app.register_blueprint(catalogs)
    '''
    from resources import api_urls
    app.register_blueprint(api_urls(app), url_prefix=app.config['API_URL'])
