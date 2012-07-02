from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def add(item):
    db.session.add(item)

def save_all():
    db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), nullable = False)
    notes = db.Column(db.Text, default = '', nullable = False)
    done = db.Column(db.Boolean, default=False, nullable = False) 

    def __init__(self, title, notes=''):
        self.title = title
        self.notes = notes

    def __repr__(self):
        return "<Task %d:%r>"%(self.id, self.title)

    def __str__(self):
        return self.__repr__().replace("<", "").replace(">", "")
