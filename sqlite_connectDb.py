# testing database connection

#import packages
import sqlite3
import pandas as pd
# if pandas doesnt run //pip3 install pandas --upgrade
# also make sure if that you are in the right pandas type
    # command + shift + p --> python interpreter

def get_db_connection():
        conn = sqlite3.connect('./patients.db')
        conn.row_factory = sqlite3.Row
        return conn
    
db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

#save data to a dataframe
df = pd.DataFrame(patientListSql)
df

#rename columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'patientstatus', 'providername', 'icd', 'lastvisit']
