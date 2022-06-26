from operator import methodcaller
from flask import Flask, render_template, url_for, redirect, request, jsonify, abort
import json

from app import app

import forms
import db

db.init_db()

# Visualizes all existing projects
@app.route('/', methods=['GET', 'POST'])
def index():
    projects = db.get_all_projects()
    
    form = forms.AddProjectForm()
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'desc': form.desc.data,
        }

        db.add_project(data)

        return redirect(url_for('index'))

    return render_template('index.html', form=form, projects=projects)

# Returns a list of all projects as a JSON object
@app.route('/api/projects', methods=['GET'])
def get_projects():
    r = db.get_all_projects()

    projects = []

    for project in r:
        projects.append({
            'id': project.id,
            'title': project.title,
            'desc': project.description,
            'likes': project.likes
        })

    return jsonify(projects)

# Get a specific project
@app.route('/api/project/<int:id>', methods=['GET'])
def get_project(id: int):
    project = db.get_project_by_id(id)

    if project is not None:
        return jsonify({
            'id': project.id,
            'title': project.title,
            'desc': project.description,
            'likes': project.likes,

        })
    else:
        abort(404)

# Updates the likes of a specific project
@app.route('/api/project/likes/<int:id>', methods=['GET'])
def update_project(id: int):
    project = db.get_project_by_id(id)

    if project is not None:
        db.increment_likes(id)

        return jsonify(success=True)
    else:
        abort(404)

@app.route('/add-project', methods=['GET', 'POST'])
def add_project():
    form = forms.AddProjectForm()
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'desc': form.desc.data,
        }

        db.add_project(data)

        return redirect(url_for('index'))

    return render_template('add-project.html', form=form)