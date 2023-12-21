from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model): # database table
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)





@app.route("/")
def start_page():
    return "Hello, World!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)