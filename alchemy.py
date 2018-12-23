from flask_sqlalchemy import SQLAlchemy

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