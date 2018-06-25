import csv

from vladiate import Vlad
from vladiate.validators import  FloatValidator, RangeValidator, RegexValidator
from vladiate.inputs import LocalFile



class TOA5Input(LocalFile):
    def open(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return lines[:1] + lines[4:]




class WeatherValidator(Vlad):
    source = TOA5Input('SPER_CR6_Daily.dat')
    validators = {
    'TS': [
    RegexValidator("^((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$", empty_ok = False)
    ],
    'Average Rainfall': [
    FloatValidator(empty_ok = True)
    ],
    'BattV_Min':[
    RangeValidator(low = 0.0, high = 500.0)
    ],
    'WS-ms_Avg':[
    RangeValidator(low = 0.0, high = 50.0)
    ],
    'WS-ms_Max':[
    RangeValidator(low = 0.0, high = 90.0)
    ],
    'WS-ms_TMx':[
    RegexValidator(pattern = "^((19|20)\\d\\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$", empty_ok = False)
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
clip < ~/.ssh/id_rsa.pub