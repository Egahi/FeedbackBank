from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from application import requests

# Configure application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////requests.db'
db = SQLAlchemy(app)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render Landing page"""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def buy():
    """Log entery in database"""
    title = request.form.get("title")
    description = request.form.get("description")
    client = request.form.get("client")
    priority = request.form.get("priority")
    date = request.form.get("date")
    area = request.form.get("area")

    #  order by priority
    requests.query.order_by(requests.priority).all()

    # select entries for same client
    previousEntry = requests.query.filter_by(client=client).all()

    modify = False

    # modify priority list to accommodate latest entry
    for i in range(len(previousEntry)):
        if previousEntry[i].priority == priority or modify == True:
            previousEntry[i].priority = previousEntry[i].priority + 1
            db.session.commit()
            modify = True

    me = requests(title, description, client, priority, date, area)
    db.session.add(me)
    db.session.commit()

    # Redirect user to home page
    return redirect("/")
