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
#   results = {}
    result = session.query(personal_personalinfo).all()
#    for res in result:
#        results[res.id] = res
#    print(dumps(results, cls=PythonObjectEncoder))
    empList = []
    for res in result:
        empDict = {
            'Id': res.id,
            'firstName': res.first_name,
            'middleName': res.middle_name,
            'lastName': res.last_name}
        empList.append(empDict)
    return jsonify(empList)
# json.dumps(empList)


if __name__ == '__main__':
    app.run(debug=True)
