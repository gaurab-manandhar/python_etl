import re

class string_utils():

    def is_date(self,date):
        r = re.compile("^\d{1,2}\/\d{1,2}\/\d{4}$")
        if bool(r.match(date)):
            return True
        else:
            return False
    def is_number(self,data):
        r = re.compile("^[0-9\.]*$")
        if bool(r.match(data)):
            return True
        else:
            return False

    def is_intVal(self,data):
        r = re.compile("^[0-9]*$")
        if bool(r.match(data)) :
            return True
        else:
            return False

    def is_string(self,data):
        r = re.compile("^[A-Za-z@\.\W]*$")
        if bool(r.match(data)):
            return True
        else:
            return False

    def remove_special_character(self,data):
        if data:
            alphanumeric = ""
            for character in data:
                if character.isalnum():
                    alphanumeric += character

            return alphanumeric

