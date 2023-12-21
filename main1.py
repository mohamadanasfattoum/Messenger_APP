from flask import Flask, render_template, request, redirect, url_for
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
        if 'delete_all' in request.form:
            Message.query.delete()
            db.session.commit()
        else:
            content = request.form['content']
            if content:
                new_message = Message(
                    user=name,
                    content=content,
                )
                db.session.add(new_message)
                db.session.commit()

    if request.method == 'GET' and 'delete_id' in request.args:
        delete_id = request.args.get('delete_id')
        message = Message.query.get(delete_id)
        if message:
            db.session.delete(message)
            db.session.commit()

    messages = Message.query.order_by(Message.created_at).all()
    return render_template('with_delete.html', msgs=messages, name=name)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)