from flask import Flask, request
import datetime as dt
from marshmallow import Schema, fields, pprint

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None

class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author  # A User object


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()

class BlogSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema)

user = User(name="Monty", email="monty@python.org")
blog = Blog(title="Something Completely Different", author=user)
result, errors = BlogSchema().dump(blog)
pprint(result)
