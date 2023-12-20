# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(debug=True)