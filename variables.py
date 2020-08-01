
"""Variable class is mainly used for getter and setter of database credential """
class Variable():
    host ='localhost'
    datawarehouse_name ='testdb'
    user='postgres'
    password=''
    def __init__(self):
        self.CREATE_TABLE = True
        self.RELATION = False
        self.INPUT_DATA = "/test/input/employee.csv"

    #Function to set varaible
    def db_set(self,host,db_name,user,password):
        self.host = host
        self.datawarehouse_name=db_name
        self.user = user
        self.password = password
    #Function to extract data
    def db_get(self):
        return [self.host,self.datawarehouse_name,self.user,self.password]

    """ Function to set CSV and Table config"""
    def set_config(self,create_table,relation, input_data):
        self.CREATE_TABLE = create_table
        self.RELATION  =relation
        self.INPUT_DATA = input_data
