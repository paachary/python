from mysqlConn.mySQLDbConnection import mySQLDbConnection
from postgresqlConn import postgresDbConnection
from oracleConn.OracleDBConnection import OracleDBConnection
from sqlliteConn.SqlLiteDbConnection import SqlLiteDbConnection


class DatabaseConnection(object):

    dbType = None


    def factory(type):
        if type == "mySQLDbConnection":
            return mySQLDbConnection()
        if type == "postgresDbConnection":
            return postgresDbConnection()
        if type == "OracleDBConnection":
            return OracleDBConnection()
        if type == "SqlLiteDbConnection":
            return SqlLiteDbConnection()
        assert 0, "Bad class chosen: " + type

    factory = staticmethod(factory)

    def setDbType(self, dbType):
        self.dbType = dbType

    def getDbType(self):
        return self.dbType

    def getDbConn(self):
        dbObj = DatabaseConnection.factory(self.dbType)
        return dbObj.getConnObject()
