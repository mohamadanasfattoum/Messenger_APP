# save this as app.py
from flask import Flask
from flask_SQLAlchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model): # database table
    id = db.Column(db.Integar, primary_key=True)




@app.route("/")
def start_page():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(debug=True)