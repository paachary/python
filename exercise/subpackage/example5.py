import subpackage
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from NewPersonModel import personal_personalinfo
from sqlalchemy import create_engine

app = subpackage.app

connectString = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % subpackage.POSTGRES
engine = create_engine(connectString, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/greeting', methods=['GET'])
def getter():
    result = session.query(personal_personalinfo).all()
    results = []
    for res in result:
        custDict = {
            'Id': res.id,
            'firstName': res.first_name,
            'middleName': res.middle_name,
            'lastName': res.last_name}
        results.append(custDict)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
