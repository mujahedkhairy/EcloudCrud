from db import db


class User(db.Model):
    __tablename__ = 'user'

    # Add this line to handle the existing table issue
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'active': self.active
        }
