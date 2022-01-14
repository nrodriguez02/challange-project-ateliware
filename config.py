import os
from flask import Flask
from flask_migrate import Migrate

from models.database import db

from views.history import history_blueprints
from views.search import search_blueprints
from views.index import index_blueprints

# DB CONNECTION
DATABASE = {
    'engine': 'postgresql',
    'user': 'postgres',
    'pw': 'QWERTY',
    'db': 'postgres',
    'host': 'postgresdb',#postgresdb on docker
    'port': '5432',
}

# Get database url from environment variables on Heroku else Docker
database_url = os.environ.get('DATABASE_URL', '%(engine)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE)


def create_app():
    app = Flask(__name__)
    migrate = Migrate()
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = 'cd48e1c22de0961d5d1bfb14f8a66e006cfb1cfbf3f0c0f3'
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(history_blueprints, url_prefix="/history")
    app.register_blueprint(search_blueprints, url_prefix="/search")
    app.register_blueprint(index_blueprints, url_prefix="/")
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
