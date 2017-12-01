#!/usr/bin/python

from DatabaseConnection import DatabaseConnection
from ResultSet import ResultSet

import sys


class init:
    def __init__(self):
        pass


dbConn = DatabaseConnection()
dbConn.setDbType(sys.argv[1])
connObj = dbConn.getDbConn()
resultSet = ResultSet(connObj)

# return the first and second columns
for row in resultSet.getQueryResult("SELECT * FROM examples"):
    print(row[0], " ", row[1])
