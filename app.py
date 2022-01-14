import os
from sqlalchemy_utils import database_exists
from config import create_app, setup_database
from flask_bootstrap import Bootstrap5

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    bootstrap = Bootstrap5(app)
    if database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        setup_database(app)
    app.run(port=8001)
