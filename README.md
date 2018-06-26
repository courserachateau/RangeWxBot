# RangeWxBot

The script is intended to validate weather station data in *TOA5 format*. Validation is done for different data types, and range checks are performed to ensure data quality

To adjust the ranges, edit the values in `ranges.csv' file. 

## Ranges for different parameters are curently assigned as below

#|Column Name|Units|Value|Low|High|
|:-|---|-:|:-|-:|-:|
|1|TS|-|Time Stamp|NA|NA|
|2|RN|-| Record Number|NA|NA|
|3|BattV_Min|Volts|Minimum Battery Volt|0.0|300.0|
|4|WS-ms_Avg|$ms^{-1}$|Average Wind Speed|0.0|50.0
|5|WS-ms_Max|$ms^{-1}$|Maximum Wind Speed|0.0|90.0
|6|WS-ms_TMx|mm-dd-YYYY `HH:MM`|Timestamp of the maximum windspeed|NA|NA|
|7|WS_ms_S_WVT|$ms^{-1}$|Mean horizontal wind speed|0.0|50.0|
|8|WindDir_D1_WVT|Degree|Mean wind direction|0.0|360.0|
|9|WindDir_SD1_WVT|Degree|Standard Deviation of wind direction|0.0|360.0|
|10|SlrMJ_Tot|MJ $m^{-2}$|Total Solar Radiation|0.0|40.0|
|11|Rain_mm_Tot|mm|Total Rainfall|0.0|50.0|
|12|AirTC_Avg|&deg;C|Average Air Temperature|-20.0|40.0|
|13|AirTC_Max|&deg;C|Maximum Air Temperature|-10.0|50.0|
|14|AirTC_TMx|mm-dd-YYYY `hh:mm`|Timestamp of Maximum Air Temperature|NA|NA|
|15|AirTC_Min|&deg;C|Minimum Air Temperature|-30.0|30.0|
|16|AirTC_TMn|mm-dd-YYYY `hh:mm`|Timestamp of Minimum Air Temperature|NA|NA|
|17|RH_Max|%|Maximum Relative Humidity|25.0|100.0|
|18|RH_TMx|mm-dd-YYYY `hh:mm`|Timestamp of Maximum Relative Humidity|NA|NA|
|19|RH_Min|%|Minimum Relative Humidity|1.0|96.0|
|20|RH_TMn|mm-dd-YYYY `hh:mm`|Timestamp of Minimum Relative Humidity|NA|NA|


