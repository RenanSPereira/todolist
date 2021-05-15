from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    finished = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.description 