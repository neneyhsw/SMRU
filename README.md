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
### SMRU original
The results will show the simulated diagram.  
The terminal will show the demand of number of chargers every time, sum of executive time, average executive time, and average demand number of chargers.  
The Truly_Charger_Point on terminal shows the position chargers.  
  
data structure of truly charger point:  
Truly_Charger_Point[x, y, 0, how many sensors covered, the sensor number, list(the sensor be covered), -1]  
Truly_Charger_Point is final chosen positions.  
You can see the points and diagram to check result.  
The repository can run many times in loop to calculate the average performances.  

1. row 68 can modify the quantities of sensors. (N <= 40)  
2. row 137 can set radius of charger.  
3. row 138 can set the range of charging.
4. row 232 can calculate the average performance of SMRU.  

SMRU will random position of charger first.  
Secondly, searching 360 degrees to find the best angle.  
Comparing to points that under the radius and search 360 degrees to choose the best point.  
Finally, removing the useless points.  

SMRU shows:  
<img src=https://github.com/neneyhsw/SMRU/blob/main/SMRU_figure.png width="500" height="500">


### SMRU mobility
This file compares to influence of mobility, and calculate average time and number of charger.  
In terminal, you can see the information about before and after mobility.  
In the file, it only run once. You can modify row 232 to calculate the average.  


### SMRU Sink Node
In SMRU_Sink.py, we can calculate how much power the sink node need.  
Moreover, we can provide the enough power for sink node by charger.  
Because this method need to satisfy requirement of power of sink nodes,  
it will add chargers for sink nodes until the requirement of power of sink nodes are enough.  


## Reference
https://www.mdpi.com/1996-1073/13/10/2661
