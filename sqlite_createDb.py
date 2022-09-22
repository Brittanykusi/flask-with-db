# sqlite comes already installed in python 3 so there is no 
# need for a pip install

# import packages
import sqlite3

# connect to sqlite
connect = sqlite3.connect('./patients.db') # we are creating a database and 
                                                        #the name of the bd is patients
                                                        # if the file doesnt exist
                                                        # it will create one
                                                        
# store db using .cursor() function - for manipulation
db = connect.cursor()

# delete patient table if it exists
db.execute("DROP TABLE IF EXISTS patient_table") # looks within the db patients 
                                                    #and will drop any table that already exists within 
                                                    # the db named patient_table
connect.commit()
# with SQL once youve made a change you need to commit the change
    # it allows you to see that a change has taken place
# // commit () --> This method commits the current transaction. 
    # If you don't call this method, anything you did since the last
# call to commit() is not visible from other database connections.

#create table
table = """ CREATE TABLE patient_table (mrn VARCHAR(255) NOT NULL, 
        firstname CHAR(25) NOT NULL, lastname CHAR(25) NOT NULL, 
        dob CHAR(25) NOT NULL, patientstatus CHAR(25) NOT NULL, 
        providername CHAR(25) NOT NULL, icd CHAR(25) NOT NULL, lastvisit CHAR(25) NOT NULL);"""
# all sql queries end in a semicolon to indicate that we are now 
    # done with the query statement
# VARCHAR and CHAR are strings and the number in the parenthesis 
    # indicates how many characters are allowed in the string
# not null states that every row in the column requires and input or value

db.execute(table)
connect.commit() # commit changes

#input data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, patientstatus, providername, icd, lastvisit) values('11111', 'Susan', 'Smith', '09/20/77', 'active', 'Dr.Nouri', 'K74.0', '09/21/22')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, patientstatus, providername, icd, lastvisit) values('11112', 'Brock', 'John', '01/01/90', 'inactive', 'Dr.Chu', 'E66.9', '09/20/22')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, patientstatus, providername, icd, lastvisit) values('11113', 'Brittany', 'Kusi-Gyabaah', '09/20/99', 'active', 'Dr.Ali', 'R93.2', '09/19/22')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, patientstatus, providername, icd, lastvisit) values('11114', 'Ronald', 'Duck', '09/20/83', 'active', 'Dr.Williams', 'D13.4', '09/18/22')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, patientstatus, providername, icd, lastvisit) values('11115', 'Felix', 'Thecat', '02/22/20', 'active', 'Dr.Nouri', 'G31.83', '09/17/22')")
# you can also create a variable that contains all patient information and insert that instead
# dummyPerson = """ INSERT INTO patient_table(mrn, firstname, lastname, dob) values('11111', 'Susan', 'Smith', '09/20/77')"""
# db.execute(dummyPerson)

connect.commit() #commit changes


# close the connection
connect.close()