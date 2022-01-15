from sqlalchemy_utils import database_exists
from config import create_app, setup_database
from flask_bootstrap import Bootstrap5

app = create_app()
app.app_context().push()
bootstrap = Bootstrap5(app)

if __name__ == '__main__':
    from models.database import db
    db.init_app(app)


    @app.before_first_request
    def create_tables():
        db.create_all()


    app.run(port=8001, debug=True)
