## Author - Prashant Acharya
## Date   - 19/May/2019

import cx_Oracle
import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/empDetails",methods=["GET"])
def getEmployeeDetails():
    ## Initialize the database connection
    with cx_Oracle.connect("<>/<>@<>") as db:
        cursor = db.cursor()
        
        ## Invoke the PLSQL packaged function which returns the ref cursor in the form of JSON records
        employees = cursor.callfunc("employee_dtls.get_dtls" , cx_Oracle.CURSOR )
        
        ## initialize an empty list to contain all the json'd records from the resultset.  
        emps = []
        
        ## loop through the ref cursor
        for emp in employees:
            ## start appending the list with the json objects
            emps.append(json.loads(emp[0]))
        
        cursor.close()
        
        ## Return the json to the calling API
        return jsonify(emps)


@app.route("/empDetails/pre12c",methods=["GET"])
def getEmployeeDetailsPre12c():
    ## Initialize the database connection
    with cx_Oracle.connect("<>/<>@<>") as db:
        cursor = db.cursor()
        
        ## Invoke the PLSQL packaged function which returns the ref cursor in the form of JSON records
        employees = cursor.callfunc("employee_dtls.get_emp_dtls" , cx_Oracle.CURSOR )
        
        ## initialize an empty list to contain all the json'd records from the resultset.  
        emps = []
        deptArray={}
        counter=0
        ## loop through the ref cursor
        for emp in employees:
            empArray=[]
            deptArray={"Department":emp[0]}
            rows = emp[1].split('%')
            for row in rows:
                jobName={}
                job_name=row.split('~')
                jobName["Job"]=job_name[0]
                jobName["Name"]=job_name[1]
                empArray.append(jobName)
            deptArray["Employees"]=empArray
            emps.append(deptArray)
        cursor.close()
        
        #print(emps)
        
        ## Return the json to the calling API
        return jsonify(emps)

if __name__ == "__main__":
    app.run(host="localhost",port=5050)

