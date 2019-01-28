"""
Api configurations
"""

class Config:
    """
    Base configuration class.
    """
    DEBUG = False # Turns on debugging features in Flask
    TESTING = False
    
class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """
    Testing Configurations, with a separate test database
    """
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig,
}
"""When your app is initialized, the variables
 in config.py are used to configure Flask and 
 its extensions are accessible via the
  app.config dictionary – e.g. app.config["DEBUG"]"""