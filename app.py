from flask import Flask

app = Flask(__name__)

@app.route("/") #main route
def home():
    return "Hello world!"

app.run()