
from flask import Blueprint, Flask

from app.api.v1.routes import VERSION_ONE as v1

from app.instance.config import APP_CONFIG

def create_app(config_name):
    '''The create_app function wraps the creation of a new Flask object,
    and returns it after it's loaded up with configuration settings using
    app.config '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])# Load the default configuration
    app.url_map.strict_slashes = False
    app.register_blueprint(v1)
    
    
    return app