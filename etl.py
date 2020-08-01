#Imports
from sql_queries import SQL_Queries
from DB import DB_Connection
from CSV_parser import csv_parser


class ETL():
    TABLE_NAME=""

    def __init__(self,table_name,input_path):
        self.TABLE_NAME = table_name
        self.INPUT_PATH = input_path

    def etl_process(self,sample_data,data_size=0):
        SQL = SQL_Queries(self.TABLE_NAME)
        #Check Table exists
        DBConn = DB_Connection()
        if  DBConn.has_table(self.TABLE_NAME):
            ParseCSV = csv_parser(self.INPUT_PATH)
            values = ParseCSV.get_data(data_size)
            qry = SQL.insert_data(self.TABLE_NAME, sample_data[0])
            DBConn.crud_ops(qry, values)
            print("Data Insert Sucessfully !!")
        else:
            #Data extraction from CSV File and Transform to database fields
            print("Data Extraction Process Started !!")
            qry = SQL.query_maker(sample_data) #Return SQL query based on CSV fields
            #Create Table base on CSV field
            if bool(DBConn.crud_ops(qry)):
                print("Table Created Sucessfully !!")
                if len(sample_data)>0:
                        ParseCSV = csv_parser(self.INPUT_PATH)
                        values = ParseCSV.get_data(data_size)
                        qry =SQL.insert_data(self.TABLE_NAME,sample_data[0])
                        DBConn.crud_ops(qry,values)
                        print("Data Insert Sucessfully !!")
            else:
                print("Unsucessful to create Table")