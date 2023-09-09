from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


        
    @validates('name', 'phone_number')
    def validate(self, key, value):
        if key == 'name':
            if not value:
                raise ValueError('please enter name')
        elif key == 'phone_number':
            if len(value) != 10:
                raise ValueError('please use 10 digits')


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'




class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('content', 'summary', 'category', 'title')
    def validate(self, key, value):
        if key == 'content':
            if len(value) < 250:
                raise ValueError('please enter more than 250 characters')
        elif key == 'summary':
            if len(value) > 249:
                raise ValueError('please enter fewer than 250 characters')
        elif key == 'category':
            if value not in ('Fiction', 'Non-Fiction'):
                raise ValueError('please use Fiction or Non-Fiction')
        elif key == 'title':
            if value not in ('Fiction', 'Non-Fiction'):
                raise ValueError('please enter Fiction or Non-Fiction')


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
