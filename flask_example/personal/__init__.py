from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'polldb_user',
    'pw': 'polldb_user',
    'db': 'polldb',
    'host': 'localhost',
    'port': '5432',
}

##postgresql://polldb_user:polldb_user@localhost:5432/polldb

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
