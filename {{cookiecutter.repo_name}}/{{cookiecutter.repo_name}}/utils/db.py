# -*- coding: utf-8 -*-


def connect(db, config):
    '''
    Connect to database
    '''
    dtb = db.connection[config['MONGODB_SETTINGS']['DB']]
    if (config['MONGODB_SETTINGS']['USERNAME'] and
            config['MONGODB_SETTINGS']['PASSWORD']):
        dtb.authenticate(
            config['MONGODB_SETTINGS']['USERNAME'],
            config['MONGODB_SETTINGS']['PASSWORD']
        )

    return dtb


def clean(dtb):
    '''
    Clean database
    '''
    for name in dtb.collection_names():
        if not name.startswith('system'):
            dtb.drop_collection(name)
