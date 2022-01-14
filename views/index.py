from flask import Blueprint, request

index_blueprints = Blueprint("index", __name__)

view = {
    "title": "Search",
    "name": "search",
}


@index_blueprints.route('/')
def index():
    return 'Hello World!'