from string_utils import string_utils
#SQL Queries

class SQL_Queries():
    StringUtils = string_utils()

    def __init__(self,table_name):
        self.TABLE_NAME =table_name
#CRUD Operation function

    def data_validitor(self,data):
        str_util = string_utils()
        if str_util.is_string(data):
            return "VARCHAR (355)"
        elif str_util.is_date(data):
            return "TIMESTAMP"
        elif str_util.is_number(data):
            if str_util.is_intVal(data):
                return "integer"
            else:
                return "DECIMAL(5)"
        else:
            return "VARCHAR (355)"

    def query_maker(self,fields_name):
        qry=""""""
        ttl = len(fields_name)
        FIRST_FIELD = True
        if ttl == 2:
            fld_len = len(fields_name[0])
            for i in range(fld_len):
                if FIRST_FIELD and self.StringUtils.is_intVal(fields_name[1][0]):
                    qry += """CREATE TABLE IF NOT EXISTS {} ("{}" serial PRIMARY KEY, """.format(self.TABLE_NAME,fields_name[0][0])
                    FIRST_FIELD = False
                else:
                    if i < fld_len-1:
                        qry += """"{}" {},""".format(fields_name[0][i],self.data_validitor(fields_name[1][i]))
                    else:
                        qry += """"{}" {} );""".format(fields_name[0][i],self.data_validitor(fields_name[1][i]))
        return qry

    #FUNCTION TO CHECK TABLE EXISTS
    def table_exists(self,table_name):
        return "SELECT EXISTS FROM {}".format(table_name)

    #Create Table into Database
    def create_table(self,table_name,fields):
        return "CREATE TABLE {} ({});".format(table_name,fields)


    #Extract Data without condition
    def extract_all(self,fields,table_name):
        return "SELECT {} FROM {}".format(fields,table_name)

    #Extract Selective Data with condition
    def extract_data(self,fields,table_name,condition):
        return "SELECT {} FROM {} WHERE {};".format(fields,table_name,condition)

    #Insert Records
    def insert_data(self,table_name,field_name):
        fld = ','.join(field_name)
        qry = "INSERT INTO {} VALUES(".format(table_name)
        fld_len = len(field_name)
        if fld_len >0:
            for fld_row in range(fld_len):
                if fld_row < fld_len - 1:
                    qry += "%s,"
                else:
                    qry += "%s)"

        return qry

    #Update Records
    def update_data(self,table_name,column_name,values,condition):
        len_column = len(column_name)
        if len_column == len(values):
            qry ="UPDATE {} SET ".format(table_name)
            for i in range(len_column):
                if i<len_column-1:
                    qry += "{}={}, ".format(column_name[i],values[i])
                else:
                    qry += "{}={}".format(column_name[i], values[i])

            qry += " WHERE {};".format(condition)
            return qry
     #Delete Records
    def delete_data(self,table_name,condtion):
        return "DELETE FROM {} WHERE {};".format(table_name,condtion)
