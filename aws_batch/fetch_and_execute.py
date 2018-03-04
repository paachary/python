#!/usr/bin/env python

from __future__ import print_function
import psycopg2
import db_config
import boto3
import botocore
import csv


# Initialize the  SQL stmt to insert data into the table(s)
stmt = """ INSERT INTO security_price_dtls ( security_id, ticker_symb, load_dt, price)
            VALUES ({0}, '{1}', '{2}', {3})"""


#
def get_db_Conn():
    params = {  "host":db_config.host,
                "database":db_config.database,
                "user":db_config.user,
                "password":db_config.password,
                "port":db_config.port }
    try:
        db_conn = psycopg2.connect(**params)
        print("Connected to RDS PostgreSQL database")
        return db_conn
    except:
        print("Error connecting to the PostgresSQL database")
        raise


def get_input_file_from_s3():
    downloaded_file = '/tmp/{0}'.format(db_config.s3_file_name)
    s3 = boto3.resource('s3',
                        aws_access_key_id=db_config.aws_access_key_id,
                        aws_secret_access_key=db_config.aws_secret_access_key)
        
    try:
        s3.Bucket(db_config.s3_bucket_name).download_file(db_config.s3_file_name,
                                                      downloaded_file)
        print("File downloaded @ {0}".format(downloaded_file))
        return downloaded_file
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
            exit(1)


# Extract the details from the input CSV and get it in a JSON format
def process_file(input_file, db_conn):
    with open(input_file) as inputfile:
        cursor = db_conn.cursor()
        reader = csv.DictReader(inputfile, delimiter=',')
        try:
            for row in reader:
                cursor.execute(stmt.format(
                               row['Securityid'],
                               row['Ticker'],
                               row['Date'],
                               row['Price']))
            db_conn.commit()
            print("Records inserted into the table successfully")
            cursor.close()
        except:
            print("Error loading into the database")


if __name__ == '__main__':
    try:
        db_conn = get_db_Conn()
        input_file = get_input_file_from_s3()
        process_file( input_file, db_conn )
        db_conn.close()
    except:
        raise
        exit
 
