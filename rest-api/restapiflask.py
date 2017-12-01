#!/usr/bin/python

# This is a rest service api running on http://127.0.0.1:5000/
# This uses python with Flask Restful framework

import sys
from flask import Flask
from flask_restful import Resource, Api
from DatabaseConnection import DatabaseConnection
from ResultSet import ResultSet


class PersonalInfo(Resource):
    dbClassName = None

    def __init__(self):
        #   Connect to the database.
        #   The first argument to the file is the class name which is database
        #   specific.
        self.dbClassName = sys.argv[1]

    def get(self):
        dbConn = DatabaseConnection()
        dbConn.setDbType(self.dbClassName)
        connObj = dbConn.getDbConn()
        query = "SELECT * FROM personal_personalInfo"
        resultSet = ResultSet(connObj)
        columnName = resultSet.getColumnNames(query)
        data = [dict(zip(columnName, row))
                for row in resultSet.getQueryResult(query)]
        return data


app = Flask(__name__)

api = Api(app)
api.add_resource(PersonalInfo, '/personalInfo')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error!! Database Type not provided!!! sample usage: \n",
              "\t\t restapiflask <<database class>> \n")
        exit(1)
    app.run(debug=True)
