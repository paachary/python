import sqlite3 as lite
from dbUtil.DatabaseParams import DatabaseParams


class SqlLiteDbConnection:
    def __init__(self):
        print("Connecting to Sqlite Database")
        None

    def getConnObject(self):
        sqlitedbConn = DatabaseParams()
        sqlitedbConn.setDbType("sqllite")
        params = sqlitedbConn.getConnParameters()
        dbConn = lite.connect(params['user'])
        return dbConn
