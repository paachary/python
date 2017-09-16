#!/usr/bin/python

import sys

class ResultSet:
    dbConnObj = None;

    def __init__(self, dbConnObj):
        self.dbConnObj = dbConnObj;

    def getQueryResult(self, query):
        cur = self.dbConnObj.cursor();
        cur.execute(query);
        return(cur.fetchall());
