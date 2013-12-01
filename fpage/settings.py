# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KEY = 'shhhh'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/db_fpage'
    SQLALCHEMY_ECHO = False

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = "dev.db"
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(DB_PATH)
    SQLALCHEMY_ECHO = True