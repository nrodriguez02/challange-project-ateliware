from sqlalchemy_utils import database_exists
from config import create_app, setup_database
from flask_bootstrap import Bootstrap5

app = create_app()
app.app_context().push()
bootstrap = Bootstrap5(app)
setup_database(app)

if __name__ == '__main__':
    app.run(port=8001, debug=True)
