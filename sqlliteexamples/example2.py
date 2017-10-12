#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys

def getTable(conn):
    cursor = conn.cursor()
    ## equivalent to DBA_OBJECTS
    cmd = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(cmd)
    names = [row[0] for row in cursor.fetchall()]
    print(names)
    return names
 
def fetchRecords(conn, tablename):
    cursor = conn.cursor();
    cmd = "SELECT id, name FROM "+tablename;
    cursor.execute(cmd);
    rows = cursor.fetchall();
    return rows;

tablename = "Users";
con = lite.connect('user.db')
try: 
    with con:
 
        cur = con.cursor()
#        print("Users" in getTable(con))
        if not (tablename in getTable(con)):
           cur.execute("CREATE TABLE "+tablename+"(Id INT, Name TEXT)")
           cur.execute("INSERT INTO "+tablename+" VALUES(1,'Michelle')")
           cur.execute("INSERT INTO "+tablename+" VALUES(2,'Sonya')")
           cur.execute("INSERT INTO "+tablename+" VALUES(3,'Greg')")

        for row in fetchRecords(con, tablename):
            print(row[0],":",row[1]);

except lite.OperationalError as e:
    print("Error %s:" %e.args[0])
    sys.exit(1)
finally:    
    if con:
        con.close()

