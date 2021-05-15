from flask import render_template, request, url_for, redirect
from models import Todo
from database import db

def configure(app):
    
    @app.route('/')
    def index():
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)

    @app.route('/add', methods=['POST'])
    def add():
        todo = Todo(description=request.form['description'], finished=False)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))

    return app    
