import subpackage
from sqlalchemy.orm import sessionmaker
from NewPersonModel import PersonalInfo
from sqlalchemy import create_engine
from subpackage import request as request
from subpackage import jsonify as jsonify
from db_functions import DatabaseFunctions
from subpackage import get_exec_time
app = subpackage.app
# 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % subpackage.POSTGRES


@app.route('/greeting', methods=['GET'])
@get_exec_time
def getter():
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
    result = session.query(PersonalInfo).all()
    results = []
    for res in result:
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
    return jsonify(results)


@app.route('/messages', methods=['POST'])
def post_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        message = request.json
        act_msg = message['message']
        print(type(message), ":: actual msgs = ", act_msg)
        return "PRAX Message: " + act_msg


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


"""
curl -X DELETE http://localhost:4040/messages/76
"""


@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    dbFunc = DatabaseFunctions()
    msg = dbFunc.delete(id)
    return msg


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4040)
