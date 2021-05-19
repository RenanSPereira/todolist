from flask import render_template, request, url_for, redirect
from src.models import Todo
from src.database import db

def configure(app):
    
    @app.route('/')
    def index():
        todos = Todo.query.filter_by(finished=False).all()
        qty = qty_completed()
        return render_template('index.html', todos=todos, qty=qty)

    @app.route('/add', methods=['POST'])
    def add():
        todo = Todo(description=request.form['description'], finished=False)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    
    @app.route('/remove/<id>')
    def remove(id):
        todo = Todo.query.filter_by(id=int(id)).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
    
    @app.route('/check/<id>')
    def check(id):
        todo = Todo.query.filter_by(id=int(id)).first()
        todo.finished = True
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))

    def qty_completed():
        qty = Todo.query.filter_by(finished=True).count()
        return qty

    return app    
