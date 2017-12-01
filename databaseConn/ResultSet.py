#!/usr/bin/python

# A generic class for providing resultset, connection object, column names


class ResultSet:
    dbConnObj = None
    dbCursor = None
    dbColumnNames = None

    def __init__(self, dbConnObj):
        self.dbConnObj = dbConnObj

    def getQueryCursor(self):
        self.dbCursor = self.dbConnObj.cursor()
        return self.dbCursor

    def getQueryResult(self, query):
        if self.dbCursor is None:
            self.dbCursor = self.dbConnObj.cursor()
        self.dbCursor.execute(query)
        return(self.dbCursor.fetchall())

    def getColumnNames(self, query):
        if self.dbCursor is None:
            self.dbCursor = self.getQueryCursor()
        self.dbCursor.execute(query)
        self.dbColumnNames = [col[0] for col in self.dbCursor.description]
        return self.dbColumnNames
