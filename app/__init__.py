from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lifeops.db'
db = SQLAlchemy(app)
md = Markdown(app, safe_mode=False, output_format='html5')

from app import routes