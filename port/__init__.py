import os

from flask import Flask

def create_app(test_config=None):
    # create app and configuration
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'port.sqlite'),
    )

    if test_config is None:
        # load instance conf, if exists, 
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test conf
        app.config.from_mapping(test_config)

    # confirm instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #basic page
    @app.route('/hello')
    def hello():
        return 'hello!'

    from . import db
    db.init_app(app)

    return app