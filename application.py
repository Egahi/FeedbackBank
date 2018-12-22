from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


# Configure application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    __tablename__ = 'requests'
    ID = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Text)
    description = db.Column('description', db.Text)
    client = db.Column('client', db.Text)
    priority = db.Column('priority', db.Integer)
    date = db.Column('date', db.Text)
    area = db.Column('area', db.Text)

    def __init__(self, tt, desc, clt, pry, dt, ar):
        self.title = tt
        self.description = desc
        self.client = clt
        self.priority = pry
        self.date = dt
        self.area = ar

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
    Entry.query.order_by(Entry.priority).all()

    # select entries for same client
    previousEntry = Entry.query.filter_by(client=client).all()

    modify = False

    # modify priority list to accommodate latest entry
    for i in range(len(previousEntry)):
        if previousEntry[i].priority == priority or modify == True:
            previousEntry[i].priority = previousEntry[i].priority + 1
            db.session.commit()
            modify = True

    # log new entry
    entry = Entry(title, description, client, priority, date, area)
    db.session.add(entry)
    db.session.commit()

    # Redirect user to home page
    return redirect("/")
