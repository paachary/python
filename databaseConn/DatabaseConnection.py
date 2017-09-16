#!/usr/bin/python
from config import config
import sys

from mySQLDbConnection import mySQLDbConnection
from postgresDbConnection import postgresDbConnection
from OracleDBConnection import OracleDBConnection


class DatabaseConnection(object):

    dbType = None; ##mySQLDbConnection

    def factory(type):
        if type == "mySQLDbConnection":
            return mySQLDbConnection();
        if type == "postgresDbConnection":
            return postgresDbConnection();
        if type == "OracleDBConnection":
            return OracleDBConnection();
        assert 0, "Bad class chosen: " + type

    factory = staticmethod(factory);

    def setDbType(self,dbType):
        self.dbType = dbType;

    def getDbType(self):
        return dbType;

    def getDbConn(self):
        dbObj = DatabaseConnection.factory(self.dbType);
        return dbObj.getConnObject();

