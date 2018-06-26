import smtplib
import settings

import csv




from collections import defaultdict

columns = defaultdict(list) 

with open('range.csv') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)




from vladiate import Vlad
from vladiate.validators import  FloatValidator, RangeValidator, RegexValidator, UniqueValidator
from vladiate.inputs import LocalFile



class TOA5Input(LocalFile):
    def open(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return lines[1:2] + lines[-1:]




class WeatherValidator(Vlad):
    source = TOA5Input('SPER_CR6_Daily.dat')
    validators = {
    'TIMESTAMP': [
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'RECORD': [
    UniqueValidator(empty_ok = False)
    ],
    'BattV_Min':[
    RangeValidator(low = float(columns[1][2]), high = float(columns[2][2]))
    ],
    'WS_ms_Avg':[
    RangeValidator(low = float(columns[1][3]), high = float(columns[2][3]))
    ],
    'WS_ms_Max':[
    RangeValidator(low = float(columns[1][4]), high = float(columns[2][4]))
    ],
    'WS_ms_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'WS_ms_S_WVT':[
    RangeValidator(low = float(columns[1][6]), high = float(columns[2][6]))
    ],
    'WindDir_D1_WVT':[
    RangeValidator(low = float(columns[1][7]), high = float(columns[2][8]))
    ],
    'WindDir_SD1_WVT':[
    RangeValidator(low = float(columns[1][8]), high = float(columns[2][9]))
    ],
    'SlrMJ_Tot':[
    RangeValidator(low = float(columns[1][10]), high =  float(columns[2][10]))
    ],
    'Rain_mm_Tot':[
    RangeValidator(low = float(columns[1][11]), high = float(columns[2][11]))
    ],
    'AirTC_Avg':[
    RangeValidator(low = float(columns[1][12]), high = float(columns[2][12]))
    ],
    'AirTC_Max':[
    RangeValidator(low = float(columns[1][13]), high = float(columns[2][13]))
    ],
    'AirTC_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'AirTC_Min':[
    RangeValidator(low = float(columns[1][14]), high = float(columns[2][14]))
    ],
    'AirTC_TMn':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'RH_Max':[
    RangeValidator(low = float(columns[1][16]), high = float(columns[2][16]))
    ],
    'RH_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'RH_Min':[
    RangeValidator(low = float(columns[1][18]), high =  float(columns[2][18]))
    ],
    'RH_TMn':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ]
    }


## Using Gmail to send the error



#subject = 'Important Message'  
#body = "Hey, what's up?\n\n- You"

#email_text = """\  
#From: %s  
#To: %s  
#Subject: %s

#%s
#""" % (sent_from, ", ".join(to), subject, body)

#try:  
#    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#    server.ehlo()
#    server.login(gmail_user, base64.decode(gmail_password))
#    server.sendmail(sent_from, to, email_text)
#    server.close()

#    print 'Email sent!'
#except:
#    print "Something went wrong...."

