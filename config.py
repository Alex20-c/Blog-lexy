import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:lexy@localhost/blogging'


    #email configurations 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    DEBUG = True


class ProdConfig(Config):
    
    SQLACHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
    
class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:lexy@localhost/blogging'
    pass


config_options = {
'development':DevConfig,
'production':ProdConfig
}