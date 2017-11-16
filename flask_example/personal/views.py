import personal

from sqlalchemy.orm import sessionmaker
from flask import render_template, flash, redirect, jsonify, json
from json import dumps, loads, JSONEncoder
#from models import Personalinfo
#from database_models import Personalinfo, Bankinfo, Addressinfo
#from PersonalModels import PersonalPersonalinfo, PersonalBankinfo, PersonalInfoSchema, PersonalAddressinfo
from NewPersonModel import personal_personalinfo, PythonObjectEncoder

from tables import PersonTable


from sqlalchemy import create_engine
engine = create_engine('postgresql://polldb_user:polldb_user@localhost:5432/polldb', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


@app.route("/personalInfo", methods=['GET'])
def main():
    """
    rows = {}
    address_as_dict = {}
    phones_as_dict = {}
    banks_as_dict = {}
    k = 0
    i=0
    j = 0
    ##for row in session.query(PersonalPersonalinfo).all():
    for row in PersonalPersonalinfo.query.all():
        i =  i+1
        rows[i] = row.as_dict()
        for addresses in row.address:
            address_as_dict[j]= addresses.__dict__
        for phones in row.phoneinfo:
          phones_as_dict[k] = phones.__dict__
        for banks in row.bank_membership:
            banks_as_dict[j] = banks.__dict__
    rows = PersonalPersonalinfo.query.all()
    rows = []
    for person in row:
        i = i + 1
        rows.append([person.as_dict(), {"address":address for address in person.address }])
#        for addresses in person.address:
#           rows.extend([addresses.as_dict()])
    #rows1 = object_as_dict(rows)
    rows = PersonalPersonalinfo.query.all()
    print(rows)
    return jsonify(rows)
    #return jsonify(rows)
    #results , error = PersonalInfoSchema(many=True).dump(rows).data
    #results , error = PersonalInfoSchema().dump(rows)
    #print(results, error)
#    return jsonify(results)
    """
    results = session.query(PersonalPersonalinfo).join(PersonalAddressinfo).all()
    rows = {}
    i = 0
    for r in results:
        i = i + 1
        #rows[i] = r._asdict()
        rows[i] = r
        print(rows[i])
    return json.dumps(rows)


@app.route('/greeting', methods=['GET'])
def getter():
    results = {}
    result = session.query(personal_personalinfo).all()
    for res in result:
        results[res.id] = res
    print(results)
    return dumps(results, cls=PythonObjectEncoder)
#    return dumps(result, cls=PythonObjectEncoder)


"""
@app.route('/greeting', methods=['GET'])
def myapi():
    person = Personalinfo.query.all()
    table = PersonTable(person)
    return render_template("greetng.html",
                            title = "Personal Info!! Greeting!!",
                            table = table)
"""
if __name__ == '__main__':
    app.run()
