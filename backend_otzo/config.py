import os
from decouple import AutoConfig, config

config = AutoConfig(search_path=os.path.join(os.path.dirname(__file__), "Otzo"))

class Config:
    SECRET_KEY = config("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}