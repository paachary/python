#!/usr/bin/python
import sys
import psycopg2
from DatabaseConnection import DatabaseConnection

class postgresDbConnection(DatabaseConnection):

    def __init__(self):
        #print("in child class");
        None

postgresDbconn = postgresDbConnection();
postgresDbconn.setDbType("postgresql");
params = postgresDbconn.makeDbConnection();
print(params);
print('Connecting to the PostgreSQL database...');
conn = psycopg2.connect(**params);
