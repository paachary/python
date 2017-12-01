import subpackage
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from NewPersonModel import PersonalInfo
from sqlalchemy import create_engine

app = subpackage.app
# 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % subpackage.POSTGRES
connectString = \
    'postgresql://{0}:{1}@{2}:{3}/{4}'.format(app.config['POSTGRES_USER'],
                                              app.config['POSTGRES_PASSWORD'],
                                              app.config['POSTGRES_HOST'],
                                              app.config['POSTGRES_PORT'],
                                              app.config['POSTGRES_DB'],)
engine = create_engine(connectString, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/greeting', methods=['GET'])
def getter():
    result = session.query(PersonalInfo).all()
    results = []
    for res in result:
        custDict = {
            'Id': res.id,
            'firstName': res.first_name,
            'middleName': res.middle_name,
            'lastName': res.last_name,
            }
        phones = []
        for phone in res.phoneinfo:
            phonesinfo = {
                'phoneType': phone.phone_type,
                'phoneNbr': phone.phone_nbr,
                }
            phones.append(phonesinfo)
        custDict['phones'] = phones
        addresses = []
        for address in res.address:
            addressinfo = {
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
                'bankName': bankinfo.bank.name,
                'branchName': bankinfo.bank.branch,
                'accountType': bankinfo.acct_type,
                'accountNbr': bankinfo.acctnbr,
                'address': bankinfo.bank.address,
                'phoneNbr': bankinfo.bank.phone_nbr,
            }
            bankdetails.append(banks)
        custDict['bankInfo'] = bankdetails
        results.append(custDict)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4040)