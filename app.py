from sqlalchemy_utils import database_exists
from config import create_app
from flask_bootstrap import Bootstrap5
from models.database import db

app = create_app()
app.app_context().push()
bootstrap = Bootstrap5(app)
db.create_all()

if __name__ == '__main__':
    app.run(port=8001, debug=True)
