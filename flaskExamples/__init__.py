#from add_nums import add_nums
#from number_reverse import NumberReverse
from flask import Flask, json, jsonify, request, render_template, redirect, url_for, Response, flash
from DatabaseConnection import DatabaseConnection
from rnd import get_exec_time
import logging
from logging.handlers import RotatingFileHandler
from logging.config import dictConfig


dictConfig({
        'version': 1,
        'formatters': {'default': {
           'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
       }},
       'handlers': {'wsgi': {
           'class': 'logging.StreamHandler',
           'stream': 'ext://flask.logging.wsgi_errors_stream',
           'formatter': 'default'
       }},
       'root': {
           'level': 'INFO',
           'handlers': ['wsgi']
      }
})
app = Flask(__name__, instance_relative_config=True, template_folder="data/templates")
log_def = True

app.config.from_object('config_file')
app.config.from_pyfile('config.py')
