#!/usr/bin/env python

## There are multiple of executing a flask script
## option 1: add these steps before you invoke the script
##    $ export FLASK_APP=hello.py
##    $ export FLASK_DEBUG=1
##    $ flask run

## option 2: add these line in your code ONLY for development
## if __name__ == '__main__':
##     app.run(debug=True)
## By default, the flask webservice listen on 5000 port

from flask import Flask, url_for, request

app = Flask(__name__)

## The route\(\): decorator is used to bind a function to a URL.
## Another option is to call a function :  
## add_url_rule : (rule, endpoint=None, view_func=None, **options)
## It works exactly like route
## Internally, route invokes add_url_rule.
## Below are examples showing both the methods
## Please refer to a private method "registerURLs" below.

@app.route('/', methods=['GET','POST'])

## The below syntax is added in the template.
## but if you want to test if the code works fine without the template, then 
## run it on the python command prompt
#with app.test_request_context\(\)::
#    print url_for('index')
#    print url_for('kasakai')
#    print url_for('user', username='Bol re')
#    print url_for('user', username='Bol re', next='/')
def hello_world():

    ## accessing the method type is by simply checking for request.method

    ##  simulating a curl command for sending a POST request 
    ## curl -X POST http://localhost:5000/


    ## by default, each route decorator takes in only GET request
    ## if someone tries to submit a POST request for a method which is not setup for POST request,
    ## this is the error you might see:
    ##
    ##      <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    ##      <title > 405 Method Not Allowed < /title >
    ##      <h1 > Method Not Allowed < /h1 >
    ##      <p > The method is not allowed for the requested URL. < /p >


    ## Types of methods taken by the routers:
    ##      GET
    ##      POST
    ##      DELETE
    ##      PUT
    ##      HEAD

    return "Hello World"

## Commented out this route method. Please refer to the "registerURLs" method below for 
## alternative way of registering the URLs

##@app.route('/greeting/<username>', methods=['GET','DELETE'])
def myapi(username): 
    print(username)
    if username == None:
        return "Kasa Kai"
    else:
        return "kasa kai %s" %username

###@app.route('/user/<username>/')
def show_user_profile(username):
    if username == None:
        return "Kaay mahntos "
    else:
            return "Kaay Mahntos %s" %username

def registerURLs():
    ## Here we dont use the routing method, but register the url with the corresponding view function

    ## Please note that the parameter passed into the registered function is as below
    app.add_url_rule('/user/<string:username>/', view_func=show_user_profile, methods=['GET'])

    ## The following function is registered with two rules:
    ##  1. if the argument is supplied as NULL.
    app.add_url_rule('/greeting/', view_func=myapi, defaults={'username': None}, methods=['GET'])

    ##  2. if the argument is supplied as a value
    app.add_url_rule('/greeting/<string:username>', view_func=myapi, methods=['DELETE','POST','PUT','GET'])

registerURLs()

print("program name  -> ", __name__)
if __name__ == '__main__':
    app.run(debug=True)
