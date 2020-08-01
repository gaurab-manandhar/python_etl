from CSV_parser import csv_parser
from etl import ETL
from variables import Variable

def main():

    print("Staring ETL Job !!!!")
    var = Variable()
    csvParser = csv_parser(var.INPUT_DATA)


    if csvParser.file_exist(var.INPUT_DATA):
        TABLE_NAME = csvParser.get_table_name(var.INPUT_DATA) # Takes Table name from Filename

        if var.CREATE_TABLE and  not var.RELATION:
            ob =ETL(TABLE_NAME,var.INPUT_DATA)
            ob.etl_process(csvParser.check_header())


if __name__ == "__main__":
  main()



