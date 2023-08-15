import os
import sys

db_path = 'instance/lifeops.db'

if os.path.exists(db_path):
    os.remove(db_path)
    print("Database deleted successfully!")
else:
    print("Database file not found!")

from app import db, app

with app.app_context():
    db.create_all()
    print("Database created successfully!")
