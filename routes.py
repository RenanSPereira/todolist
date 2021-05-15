from flask import render_template
from models import Todo

def configure(app):
    
    @app.route('/')
    def index():
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)

    return app    
