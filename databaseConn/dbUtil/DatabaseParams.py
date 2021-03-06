#!/usr/bin/python
from dbConfig import config


class DatabaseParams:
    'This is the parent class which has basic methods to get the '
    'db connection parameters'
    dbType = 'mongodb'

    def __init__(self):
        None

    def setDbType(self, dbType):
        self.dbType = dbType

    def getDbType(self):
        return self.dbType

    def getConnParameters(self):
        if (self.dbType is None):
            raise ValueError('The passed argument for dbType is null')
        params = config("/home/prashant/python_code/src/databaseConn/dbConfig/database.ini",
                        self.dbType)

        if (params is None):
            raise ValueError('The connection details in the ini file does not'
                             ' exist for dbType:', self.dbType)
        return params
