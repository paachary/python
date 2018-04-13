from add_nums import add_nums
from number_reverse import NumberReverse
from flask import Flask, json, jsonify, request
from DatabaseConnection import DatabaseConnection
from rnd import get_exec_time

app = Flask(__name__, instance_relative_config=True)
log_def = True

app.config.from_object('config_file')
app.config.from_pyfile('config.py')
