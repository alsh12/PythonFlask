from flask import Flask , render_template

app = Flask(__name__)


@app.route("/<name>/<age>")
def hello_world(name="Alok",age=0):
    return render_template("Jinja_intro.html",name=name,age=age)


@app.route("/another")
def another():
    return """
    <html>
    <body>
    <h1>Greeting </h1>
    </body>
    </html>
    """


@app.route("/data")
def render_data_structures():

    movies = [
        "Amar Akbar Anthony",
        "Yaarana",
        "Golmaal"
    ];
    return render_template("data-structures.html",movies=movies)


@app.route("/company")
def render_company():
    company = "Apple"
    return render_template("condition_basics.html",company=company)


@app.route("/loop")
def render_loop():
    friendList =[
        "Alok",
        "Ashish",
        "Ketan",
        "Praveen",
        "Viram",
        "Lalit"
    ]
    return render_template("loop.html",friendList=friendList)