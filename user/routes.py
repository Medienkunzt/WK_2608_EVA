from flask import Flask, render_template, url_for, redirect, request, jsonify, abort, session
from producer import publish
import db

from app import app
import forms

#db.init_db()

session_ids = []

@app.route('/', methods=['GET', 'POST'])
def index():
    print(session)

    projects = db.get_all_projects()
    print(projects)

    for project in projects:
        print(project)

    form = forms.VoteForm()
    if form.validate_on_submit():
        button_id = int(request.args.get('id'))

        # If you want to vote only once
        # session_ids.append(button_id)
        # session['id'] = session_ids

        publish('like', button_id)

        return redirect(url_for('index'))

    return render_template('index.html', projects=projects, form=form)

@app.route('/clear')
def clear():
    session.clear()

    return redirect(url_for('index'))
