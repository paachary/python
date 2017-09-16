#!/usr/bin/python
import sys

from DatabaseParams import DatabaseParams
#import databaseConn.DatabaseConnection

class SqlLiteDbConnection(DatabaseParams):

    def __init__(self):
        #print("in child class");
        None

sqlliteconn = SqlLiteDbConnection();
sqlliteconn.setDbType("sqllite");
params = sqlliteconn.getConnParameters();
print(params);
    
    
