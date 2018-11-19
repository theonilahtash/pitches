from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password = db.Column(db.String(255))
    # Defining the One to many relationship between a user and a pitch
    pitch = db.relationship('Pitch', backref="user", lazy='dynamic')

    # Defining the One to many relationship between a user and a comment
    comment = db.relationship('Comment', backref='main_user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    # Defining a one to many relationship between a category and a pitch
    pitch = db.relationship('Pitch', backref='parent_category', lazy='dynamic')

    def __repr__(self):
        return f'Category {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    # Defining the foreign key from the relationship between a user and a pitch
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Defining the foreign key from the relationship between a category and a pitch
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # Defining a one to many relationship between a pitch and a comment
    comments = db.relationship('Comment', backref="main_pitch", lazy="dynamic")

    def __repr__(self):
        return f'Pitch {self.title}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id =  db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    comment = db.Column(db.String)
    # Defining the foreign key from the relationship between a pitch and a comment
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    # Defining the foreign key from the relationship between a user and a comment
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'Comment {self.comment}'