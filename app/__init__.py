import os
from flask import Flask
from .extensions import mysql
from configparser import ConfigParser as cp
from .server import server_blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from .database import check_and_update_client_status


def get_database_config(filename='config.ini', section='MySQL'):
    parser = cp()
    parser.read(filename)
    
    db = {}
    
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f'Section {section} not found in in the {filename} file')
    
    return db


def create_app():
    app = Flask(__name__)

    def start_scheduler():
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_and_update_client_status, "interval", seconds=60, args=[app])
        scheduler.start()

    
    db_config = get_database_config()

    app.config['MYSQL_HOST'] = db_config['host']
    app.config['MYSQL_USER'] = db_config['user']
    app.config['MYSQL_PASSWORD'] = db_config['password']
    app.config['MYSQL_DB'] = db_config['database']

    mysql.init_app(app)

    app.register_blueprint(server_blueprint)

    start_scheduler()

    return app