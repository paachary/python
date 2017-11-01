from flask import render_template, flash, redirect, jsonify, json
#from models import Personalinfo
from database_models import Personalinfo, Bankinfo, Addressinfo
from tables import PersonTable
from personal import app

@app.route("/personalInfo", methods=['GET'])
def main():
    ##personal = Personalinfo.query.all()
    return( Personalinfo.query.all())
    #return jsonify(message="Returning persnal info", personal_info=personal)
#    return render_template("personalInfo.html",
#                           title = "Personal Info",
#                           personal=personal)
#    return 'Hello World !'


@app.route('/greeting', methods=['GET'])
def myapi():
    person =  Personalinfo.query.all()
    table = PersonTable(person)
    return render_template("greetng.html",
                            title = "Personal Info!! Greeting!!",
                            table = table)

if __name__ == '__main__':
    app.run()
