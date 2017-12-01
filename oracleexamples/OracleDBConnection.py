#!/usr/bin/python
import cx_Oracle
from DatabaseParams import DatabaseParams


class OracleDBConnection:
    def __init__(self):
        print("Connecting to Oracle Database")
        None

    def getConnObject(self):
        oracleDbConn = DatabaseParams()
        oracleDbConn.setDbType("oracle")
        params = oracleDbConn.getConnParameters()
        connStr = params['user']+"/" + \
            params['passwd']+"@" + \
            params['host']+":" + \
            params['port']+"/" + \
            params['service']
        dbConn = cx_Oracle.connect(connStr)
        return dbConn
