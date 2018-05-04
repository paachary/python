import data
from sqlalchemy.orm import sessionmaker
from PersonModel import PersonalInfo
from sqlalchemy import create_engine
from data import request, jsonify, render_template, get_exec_time, redirect,url_for, Response, json
from db_functions import DatabaseFunctions

app = data.app

connectString = \
   'postgresql://{0}:{1}@{2}:{3}/{4}'.\
    format(app.config['POSTGRES_USER'],
           app.config['POSTGRES_PASSWORD'],
           app.config['POSTGRES_HOST'],
           app.config['POSTGRES_PORT'],
           app.config['POSTGRES_DB'],)
engine = create_engine(connectString, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def get_customer_details(resultSet):
    results = []
    for res in resultSet:
        personDtls = {}
        custDict = {
            'Id': res.id,
            'firstName': res.first_name,
            'middleName': res.middle_name,
            'lastName': res.last_name,
            'emailid': res.emailid,
            'age': res.age,
            'gender': res.gender
            }
        phones = []
        for phone in res.phoneinfo:
            phonesinfo = {
                'phoneID': phone.id,
                'phoneType': phone.phone_type,
                'phoneNbr': phone.phone_nbr,
                }
            phones.append(phonesinfo)
        custDict['phones'] = phones
        addresses = []
        for address in res.address:
            addressinfo = {
                'addressID': address.id,
                'addressType': address.address_type,
                'door': address.door,
                'street': address.street,
                'city': address.city,
                'state': address.state,
                'country': address.country,
                'pin': address.pin,
            }
            addresses.append(addressinfo)
        custDict['addresses'] = addresses
        bankdetails = []
        for bankinfo in res.bank_membership:
            banks = {
                'bankID': bankinfo.id,
                'bankName': bankinfo.bank.name,
                'branchName': bankinfo.bank.branch,
                'accountType': bankinfo.acct_type,
                'accountNbr': bankinfo.acctnbr,
                'address': bankinfo.bank.address,
                'phoneNbr': bankinfo.bank.phone_nbr,
            }
            bankdetails.append(banks)
        custDict['bankInfo'] = bankdetails
        personDtls['person'] = custDict
        results.append(personDtls)
    return results


@app.route("/", methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route("/get_customer/<param>", methods=['GET'])
def get_customer(param):
    if (param == 'QUERY' ):
        return render_template("query_customer.html")
    elif (param == 'DELETE' ):
        return render_template("delete_customer.html")


@app.route("/getCustomer", methods=['POST'])
def query_customer():
    fname = request.form['fname']
    lname = request.form['lname']
    result = session.query(PersonalInfo).filter_by(first_name=fname, last_name=lname)
    results = get_customer_details(result)
    return jsonify(results)


@app.route("/deleteCustomer", methods=['POST'])
def delete_customer():
    fname = request.form['fname']
    lname = request.form['lname']
    result = session.query(PersonalInfo).filter_by(first_name=fname, last_name=lname).first()

    return redirect(url_for("delete_message", id=result.id), code=307)


@app.route('/all', methods=['GET'])
@get_exec_time
def getter():
   result = session.query(PersonalInfo).all()
   results = get_customer_details(result)
   return jsonify(results)


@app.route('/personDelete/<int:id>', methods=['POST'])
def delete_message(id):
    message = request.json
    print(message)
    dbFunc = DatabaseFunctions()
    msg = dbFunc.delete(id)
    return redirect("/")


"""
example using curl command for PUT:
curl -X PUT http://localhost:4040/messages/25 -H "Content-Type: application/json" -d '{"person": {"Id": 25,"firstName": "Vaibhavi","lastName": "Acharya",  "middleName": "Prashant","age":"20", "gender":"F","emailid":"prashant_acharya14@yaghoo.com","addresses": [{"addressType": "P","city": "Bangalore","country": "India","door": 61,"pin": 560085,"state": "Karnataka","street": "1st Main, 2nd Cross, BSK 3rd Stage, 4th Block"}],"phones": [{"phoneNbr": "+918042078598","phoneType": "R"},{"phoneNbr": "+919845311661","phoneType": "M"}],"bankInfo": [{"accountNbr": "379402010008030", "accountType": "SB", "address": "Jayanagar, Bangalore", "bankName": "Union Bank of India", "branchName": "Jayanagar", "phoneNbr": "080947846434"}]}}'
"""

@app.route('/messages/<int:id>', methods=['PUT'])
def put_message(id):

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        message = request.json
        dbFunc = DatabaseFunctions()
        msg = dbFunc.upsert(id, message)
        return msg


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4040)

