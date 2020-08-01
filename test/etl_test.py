from CSV_parser import csv_parser
from etl import ETL
from variables import Variable


def ETI_TEST():
    print("Staring ETL Test  Job !!!!")
    var = Variable()
    var.INPUT_DATA ="/input/employee.csv"
    csvParser = csv_parser(var.INPUT_DATA)

    if csvParser.file_exist(var.INPUT_DATA):
        TABLE_NAME = csvParser.get_table_name(var.INPUT_DATA)  # Takes Table name from Filename

        if var.CREATE_TABLE and not var.RELATION:
            ob = ETL(TABLE_NAME, var.INPUT_DATA)
            ob.etl_process(csvParser.check_header(),20)


if __name__ == "__main__":
    ETI_TEST()