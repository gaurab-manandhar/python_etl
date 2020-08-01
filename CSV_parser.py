from csv import reader
from string_utils import string_utils
import os
from os import path


class csv_parser():
    StringUtils = string_utils()
    curr_path = os.getcwd()

    def __init__(self,csv_path):
        self.PATH= csv_path

    def check_header(self):
        with open("{}/{}".format(self.curr_path,self.PATH), 'r') as read_obj:
            csv_reader = reader(read_obj)
            return self.header_array(csv_reader)


    '''Method to request two from CSV file'''
    def header_array(self,csv_reader):
        counter=0
        data = [0]*2
        for row in csv_reader:
            if counter <2:
                data[int(counter)]= row
                counter +=1
            else:
                break
        return data

    def get_table_name(self,path):
        try:
            if path:
                fname = os.path.basename(path)
                file_name,ext = os.path.splitext(fname)
                return self.StringUtils.remove_special_character(file_name)

            else:
                return "File Not Found"
        except FileNotFoundError:
            print("Wrong File Name Enter")

    def file_exist(self,file_path):
        if file_path:
            if path.exists(self.curr_path+file_path):
                return True
            else:
                print(self.curr_path+file_path)
                print("File Not Found !!")
                return False

    def get_data(self, num_row=0):
        assign_data = [0]*num_row
        with open("{}/{}".format(self.curr_path,self.PATH), 'r') as read_obj:
            csv_reader = reader(read_obj)
            # Extract data from CSV
            header = next(csv_reader)
            # Check file as empty
            if header != None:
                data = list(csv_reader)
                if num_row == 0:
                    return data
                else:
                    for i in range(num_row):
                        assign_data[i] = data[i]
                    return assign_data
