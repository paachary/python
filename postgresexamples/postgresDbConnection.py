#!/usr/bin/python
import psycopg2
from DatabaseParams import DatabaseParams


class postgresDbConnection(DatabaseParams):
    def __init__(self):
        print("Connecting to postgres database")
        pass

    def getConnObject(self):
        postgresDbconn = DatabaseParams()
        postgresDbconn.setDbType("postgresql")
        params = postgresDbconn.getConnParameters()
        dbConn = psycopg2.connect(**params)
        return dbConn
