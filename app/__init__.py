from flask import Flask
from .server import server_blueprint
from .database import *
from .tasks import *


def create_app():
    app = Flask(__name__)

    # Initialize the background tasks
    init_tasks(app)

    # Initialize the MySQL database
    init_db(app)

    app.register_blueprint(server_blueprint)

    return app

