from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from app.models import Base  # Import the Base class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lifeops.db'
db = SQLAlchemy(app)
db.Model = Base  # Link the Base class to SQLAlchemy

# Initialize the database and create tables
with app.app_context():
    db.create_all()

md = Markdown(app, safe_mode=False, output_format='html5')

from app import routes