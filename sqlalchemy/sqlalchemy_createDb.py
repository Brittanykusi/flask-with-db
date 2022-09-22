## import packages
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import insert

## create db for table
engine = create_engine('sqlite:///sqlalchemy/sqlalchemy_patients.db', echo = True)
meta = MetaData()

## create and assign table columns and parameters
patients_table2 = Table(
   'patients_table2', meta, 
   Column('mrn', String, primary_key = True), 
   Column('firstname', String), 
   Column('lastname', String), Column('dob', String), )

#commit and create table
meta.create_all(engine)

## insert values into table
stmt = (
    insert(patients_table2).
    values(mrn='11111', firstname='Susan', lastname='Smith', dob='09/20/77'))

stmt = (
    insert(patients_table2).
    values(mrn='11112', firstname='Brock', lastname='John', dob='01/01/90'))

stmt = (
    insert(patients_table2).
    values(mrn='11113', firstname='Brittany', lastname='Kusi-Gyabaah', dob='09/20/99'))

stmt = (
    insert(patients_table2).
    values(mrn='11114', firstname='Donald', lastname='Duck', dob='09/20/83'))

## not sure what to do after this point :/