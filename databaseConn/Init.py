#!/usr/bin/python


from dbUtil import DatabaseConnection
from dbUtil.ResultSet import ResultSet

import sys


class init:
    def __init__(self):
        pass


dbConn = DatabaseConnection()
print(sys.argv[1])
dbConn.setDbType(sys.argv[1])
connObj = dbConn.getDbConn()
resultSet = ResultSet(connObj)

# return the first and second columns
for row in resultSet.getQueryResult("SELECT * FROM personal_personalinfo"):
    print(row[0], " ", row[1])
