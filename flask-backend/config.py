# import os

# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
#     DEBUG = False


# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# class ProductionConfig(Config):
#     DEBUG = False


# config_by_name = dict(
#     dev=DevelopmentConfig,
#     prod=ProductionConfig
# )
