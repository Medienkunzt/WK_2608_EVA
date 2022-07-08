from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    likes = db.Column(db.Integer)


def get_all_projects():
    return Project.query.all()

def get_project_by_id(id):
    return Project.query.filter_by(id=id).first()

def init_db():

    db.drop_all()
    db.create_all()

    project1 = Project(title="Erstes Projekt", description="Umsatzsteigerung um 4%", likes=3)
    project2 = Project(title="Zweites Projekt", description="Einführung eines neuen ERP-Systems", likes=7)

    db.session.add(project1)
    db.session.add(project2)

    db.session.commit()

def add_project(data):
    project = Project(title=data['title'], description=data['desc'], likes=0)

    db.session.add(project)
    db.session.commit()


def increment_likes(id):
    project = Project.query.filter_by(id=id).first()
    project.likes = project.likes + 1

    db.session.commit()