from flask import Flask, render_template, flash, request, json, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests

 
# App config.
DEBUG = True
application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), 
                      validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), 
                         validators.Length(min=3, max=35)])
 
 
@application.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)


@application.route("/data", methods=['GET'])
def get_data():
    r = requests.get('http://localhost:4040/greeting')
    records = r.json()
    return render_template('person.html', person_records=records)
 

if __name__ == "__main__":
    application.run(host='localhost', port=5050)
    
