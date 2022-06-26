import sqlite3
from flask import current_app

def get_db():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.cursor().execute('DROP TABLE IF EXISTS projects')
     
    db.cursor().execute('CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT NOT NULL, likes INTEGER)')

    db.cursor().execute('INSERT INTO projects (title, description, likes) VALUES (?, ?, ?)', ('Erstes Projekt', 'Umsatzsteigerung um 4%', '3'))
    db.commit()

    db.cursor().execute('INSERT INTO projects (title, description, likes) VALUES (?, ?, ?)', ('Zweites Projekt', 'Einführung eines neuen ERP-Systems', '7'))
    db.commit()

def add_project(data):
    db = get_db()

    db.cursor().execute('INSERT INTO projects (title, description, likes) VALUES (?, ?, ?)', (data['title'], data['desc'], '0'))
    db.commit()

def increment_likes(id):
    db = get_db()
    
    db.cursor().execute('UPDATE projects SET likes = likes + 1 WHERE projects.id = ' + str(id))
    db.commit()

# https://www.geeksforgeeks.org/how-to-execute-raw-sql-in-flask-sqlalchemy-app/
# --> Execute raw sql

# SQLAlchemy run SQL statements
# https://rg2021.medium.com/flask-with-sqlalchemy-database-39fc0959609c
# https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
# --> app and db in app.py
# --> Table definitions in models.py
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# --> nullable=False
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/
# --> First .drop_all() and then .create_all()?

# https://stackoverflow.com/questions/58951334/aiopg-sqlalchemy-how-to-drop-table-if-exists-without-raw-sql
# --> SQLAlchem,,y has DropTable if_exists=True


# https://www.codegrepper.com/code-examples/sql/flask+sqlalchemy+update+row
# --> Update column