#!/usr/bin/python

import sys
import MySQLdb

from DatabaseParams import DatabaseParams

class mySQLDbConnection:

    def __init__(self):
        print("Connecting to mysqlDB");
        None

    def getConnObject(self):
        mysqldbConn = DatabaseParams();
        mysqldbConn.setDbType("mysqldb");
        params = mysqldbConn.getConnParameters();
        dbConn = MySQLdb.connect(**params);
        return dbConn;
