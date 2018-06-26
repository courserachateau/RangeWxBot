import smtplib
import settings

import csv

from vladiate import Vlad
from vladiate.validators import  FloatValidator, RangeValidator, RegexValidator, UniqueValidator
from vladiate.inputs import LocalFile



class TOA5Input(LocalFile):
    def open(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return lines[1:2] + lines[4:]




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
    RangeValidator(low = 0.0, high = 500.0)
    ],
    'WS_ms_Avg':[
    RangeValidator(low = 0.0, high = 50.0)
    ],
    'WS_ms_Max':[
    RangeValidator(low = 0.0, high = 90.0)
    ],
    'WS_ms_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'WS_ms_S_WVT':[
    RangeValidator(low = 0.0, high = 50.0)
    ],
    'WindDir_D1_WVT':[
    RangeValidator(low = 0.0, high = 360.0)
    ],
    'WindDir_SD1_WVT':[
    RangeValidator(low = 0.0, high = 360.0)
    ],
    'SlrMJ_Tot':[
    RangeValidator(low = 0.0, high =  40.0)
    ],
    'Rain_mm_Tot':[
    RangeValidator(low = 0.0, high = 50.0)
    ],
    'AirTC_Avg':[
    RangeValidator(low = -20.0, high = 40.0)
    ],
    'AirTC_Max':[
    RangeValidator(low = -10.0, high = 50.0)
    ],
    'AirTC_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'AirTC_Min':[
    RangeValidator(low = -30.0, high = 30.0)
    ],
    'AirTC_TMn':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'RH_Max':[
    RangeValidator(low = 25.0, high = 100.0)
    ],
    'RH_TMx':[
    RegexValidator(pattern = "((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) ([2][0-3]|[0-1][0-9]|[1-9]):[0-5][0-9]:([0-5][0-9]|[6][0])$", empty_ok = False)
    ],
    'RH_Min':[
    RangeValidator(low = 1.0, high =  96.0)
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

