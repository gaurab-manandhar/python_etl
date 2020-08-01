#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import psycopg2

data = [
    ['327717', 'Mrs.', 'Bobbye', 'I', 'Bilderback', 'F', 'bobbye.bilderback@gmail.com', 'Allen Bilderback',
     'Christel Bilderback', 'Pryor', '1/26/1972', '03:31:22 PM', '45.53', '48', '5/4/2007', 'Q2', 'H1', '2007', '5', 'May', 'May',
     '4', 'Friday', 'Fri', '10.24', '126748', '6%', '064-02-3824', '209-596-8403', 'Planada', 'Merced', 'Planada', 'CA', '95365',
     'West', 'bibilderback', 'ZYj_sDAf@;IwgV?'],
    ['263249', 'Drs.', 'Joyce', 'A', 'Seim', 'F', 'joyce.seim@yahoo.com', 'Raymundo Seim',
    'Dorthea Seim', 'Funk', '10/11/1983', '02:29:19 AM', '33.82', '57', '12/18/2006', 'Q4',
     'H2', '2006', '12', 'December', 'Dec', '18','Monday', 'Mon', '10.62', '109109', '28%', '334-11-5544',
     '231-639-3470', 'Grand Rapids', 'Kent', 'Grand Rapids', 'MI', '49518', 'Midwest', 'jaseim', 'M.[nekgNX335QV']
]

field = "Emp ID,Name Prefix,First Name,Middle Initial,Last Name,Gender,E Mail,Father's Name,Mother's Name,Mother's Maiden Name,Date of Birth,Time of Birth,Age in Yrs.,Weight in Kgs.,Date of Joining,Quarter of Joining,Half of Joining,Year of Joining,Month of Joining,Month Name of Joining,Short Month,Day of Joining,DOW of Joining,Short DOW,Age in Company (Years),Salary,Last % Hike,SSN,Phone No. ,Place Name,County,City,State,Zip,Region,User Name,Password"
val = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
# print(val.count(",") + 1)
print(field)
print(len(data[1]))
con = psycopg2.connect("host=localhost dbname=testdb user=postgres")

with con:

    cur = con.cursor()


    query = """INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    cur.executemany(query, data)

    con.commit()