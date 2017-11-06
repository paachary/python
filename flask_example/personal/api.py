#!/usr/bin/python

## This is a rest service api running on http://127.0.0.1:5000/ 
## This uses python with Flask Restful framework

import sys
from flask import Flask, request
from flask_restful import Resource, Api
from DatabaseConnection import DatabaseConnection
from ResultSet import ResultSet

class PersonalInfo(Resource):
    dbClassName = None

    def __init__(self):
        ## Connect to the database.
        ## The first argument to the file is the class name which is database specific.
        self.dbClassName = 'postgresDbConnection'

    def get(self):
        dbConn = DatabaseConnection()
        dbConn.setDbType(self.dbClassName)
        connObj = dbConn.getDbConn()   
        query =   " SELECT row_to_json(t) AS person"\
                  " FROM "\
                  " ("\
                      "  SELECT person.first_name, "\
                      "         person.middle_name,"\
                      "         person.last_name,"\
                      "         person.gender,"\
                      "         person.emailid,"\
                      "         person.age,"\
                    "   ("\
                        "   SELECT COALESCE(ARRAY_TO_JSON(ARRAY_AGG(ROW_TO_JSON(d))), '[]')"\
                        "   FROM ("\
                                "   SELECT  address_type,"\
                               "            door,"\
                               "            street,"\
                               "            city,"\
                               "            state,"\
                               "            country,"\
                               "            pin"\
                               "    FROM personal_addressinfo address"\
                               "    WHERE person.id = person_id"\
                               " )d"\
                        "   ) AS address,"\
                        "   ("\
                        "       SELECT COALESCE(ARRAY_TO_JSON(ARRAY_AGG(ROW_TO_JSON(d))), '[]')"\
                        "       FROM ("\
                        "               SELECT  phone_type,"\
                        "                       phone_nbr"\
                        "               FROM personal_phoneinfo phone"\
                        "               WHERE person.id = person_id"\
                        "           ) d"\
                    "    ) AS phone,"\
                    "   ("\
                    "       SELECT COALESCE(ARRAY_TO_JSON(ARRAY_AGG(ROW_TO_JSON(d))), '[]')"\
                    "       FROM ("\
                    "               SELECT acct_type, "\
                    "                       acctnbr, "\
                    "                       name, "\
                    "                       branch,"\
                    "                       address,"\
                    "                       phone_nbr "\
                    "               FROM personal_bankmembership mem, "\
                    "                    personal_bankinfo bank "\
                    "               WHERE mem.bank_id = bank.id "\
                    "                 AND person.id = mem.person_id "\
                    "           ) d "\
                    "   ) AS bank"\
                "       FROM personal_personalInfo AS person "\
                "   ) AS t"
        resultSet = ResultSet(connObj);
        cursor =  resultSet.getQueryCursor()
        columnName = resultSet.getColumnNames(query)
        data = [dict(zip(columnName, row))  
                for row in resultSet.getQueryResult(query)]
        return data

app = Flask(__name__)

api = Api(app)
api.add_resource(PersonalInfo, '/personalInfo')

if __name__ == '__main__':
    """
    if len(sys.argv) < 2:
        print("Error!! Database Type not provided!!! sample usage: \n",
              "         api <<database class>> \n")
        exit(1)
    """
    app.run(debug=True)
