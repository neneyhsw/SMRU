# SMRU

## Introduction
SMRU (Search Most and Remove Useless) is an algorithm for WRSNs (Wireless Rechargeable Sensor Networks).  
The repo will simulate the WRSNs environment,  
and implement SMRU algorithm by python3.


The python file will simulate the SMRU algorithm.  
```
python3 SMRU_orginal.py
```

## Experiment
The results will show the simulated diagram.  
The terminal will show the demand of number of chargers every time, sum of executive time, average executive time, and average demand number of chargers.  
The Truly_Charger_Point on terminal shows the position chargers.  
  
data structure of truly charger point:  
Truly_Charger_Point[x, y, 0, how many sensors covered, the sensor number, list(the sensor be covered), -1]

1. row 68 can modify the quantities of sensors. (N <= 40)  
2. row 137 can set radius of charger.  
3. row 138 can set the range of charging.
4. row 232 can calculate the average performance of SMRU.  

SMRU shows:
<img src=https://github.com/neneyhsw/SMRU/blob/main/SMRU_figure.png width="500" height="500">

# Reference
https://www.mdpi.com/1996-1073/13/10/2661
