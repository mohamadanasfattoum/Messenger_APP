# save this as app.py
from flask import Flask
from flask_SQLAlchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model): # database table
    id = db.Column(db.Integar, primary_key=True)
    user = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime(), default= datetime.utcnow)





@app.route("/")
def start_page():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(debug=True)