from flask import Flask, render_template, request
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


@app.route("/<name>", methods=['GET','POST'])
def start_page(name):
    if request.method == 'POST':
        new_message = Message(
            user = name,
            content = request.form['content'],
        )
        db.session.add(new_message)
        db.session.commit()
    return render_template('base.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)




# لحتى يشتغل لازم فعل البيئة لوهمية وارجع اخرج منها للملف الرأيسي 
# messanger_app\src\venv>
# .\Scripts\activate
# cd -
# messanger_app\src> 
# messanger_app\src> strt coding