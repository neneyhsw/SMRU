import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import math
import time


######## function area ########
def Swap(a, b):  # for shuffle array to result in the sequence of Charger_Points is random
    return b, a

# convert Cartesian Coordinates to Polor Coordinates
def Convert_to_Polor(cx, cy, px, py):
    r = math.sqrt(math.pow(px-cx, 2) + math.pow(py-cy, 2))
    theta = math.atan2(py-cy, px-cx) / math.pi*180  # convert to angle
    #print ("r =", r, "\ntheta =", theta)
    return r, theta

# convert Theta to range(0, 359)
def Theta_Conversion(polor_theta, open_angle_theta):
    if (polor_theta >= 360):
        polor_theta = (polor_theta % 360)
    if (polor_theta < 0):
        polor_theta += 360

    if (polor_theta < open_angle_theta):
        # start_arm == right side
        start_arm = 360 + (polor_theta-open_angle_theta)
        end_arm = polor_theta + open_angle_theta  # end_arm == left side
    elif (polor_theta > (360-open_angle_theta)):
        start_arm = polor_theta - open_angle_theta
        end_arm = (polor_theta+open_angle_theta) - 360
    else:
        start_arm = polor_theta - open_angle_theta
        end_arm = polor_theta + open_angle_theta

    if (start_arm == 360):
        start_arm = 0
    if (end_arm == 360):
        end_arm = 0

    return polor_theta, start_arm, end_arm

# distance between two points
def Distance_between_two_points(point1_x, point1_y, point2_x, point2_y):
    distance = (((point2_x-point1_x)**2)+((point2_y-point1_y)**2)
                )**0.5  # c**2 = a**2 + b**2
    return distance


######## parameter setting ########
# initialize sensor array, this array can add number of sensors to 40
Sensor = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

fig = plt.figure(figsize=(8, 8))  # set figure size to 800*800
N = 40  # quantities of Sensor
Data_sink_node = [[25, 25, 0], [25, 75, 0], [75, 25, 0], [75, 75, 0]]  # the coordinate of Data sink node
sink_num = 4

# test Sensor Array, Array of 20 rows and 2 columns,
test_Sensor_Array = [[11, 40], [82, 89], [79, 57], [73, 20], [41, 60],
                     [52, 82], [41, 47], [39, 3], [86, 20], [46, 20],
                     [2, 89], [8, 30], [74, 93], [81, 44], [29, 40],
                     [39, 66], [84, 45], [28, 86], [11, 80], [82, 78]]

test_Sensor_Array_2 = [[59, 64], [5, 86], [32, 63], [30, 87], [55, 60],
                       [47, 83], [18, 6], [61, 70], [44, 42], [67, 56],
                       [11, 26], [12, 100], [39, 24], [55, 62], [36, 93],
                       [86, 60], [92, 82], [92, 80], [73, 15], [9, 74]]

test2 = [[40, 40], [50, 40]]

test3 = [[46, 80], [90, 44], [9, 83], [52, 62], [31, 7],
         [30, 62], [2, 29], [49, 22], [88, 67], [25, 24],
         [59, 47], [45, 54], [100, 14], [80, 65], [91, 37],
         [90, 63], [30, 66], [6, 33], [32, 57], [28, 66]]

test4 = [[1, 8], [64, 20], [76, 90], [54, 24], [75, 23],
         [99, 73], [64, 80], [83, 91], [58, 12], [79, 93],
         [77, 14], [89, 56], [90, 70], [55, 8], [79, 10],
         [65, 44], [73, 8], [3, 76], [54, 55], [89, 81]]

test5 = [[80, 71], [84, 4], [83, 13], [80, 40], [31, 40],
         [25, 57], [31, 73], [2, 81], [24, 64], [81, 51],
         [8, 91], [1, 92], [34, 23], [77, 96], [62, 82],
         [18, 41], [80, 63], [44, 74], [51, 8], [40, 17]]

test6 = [[97, 79], [15, 75], [16, 85], [2, 10], [70, 7],
         [14, 18], [83, 28], [36, 99], [52, 62], [17, 68],
         [2, 87], [37, 92], [91, 68], [46, 94], [67, 24],
         [85, 60], [27, 55], [15, 59], [5, 10], [5, 69]]

test7 = [[1, 91], [5, 72], [53, 39], [33, 52], [34, 93],
         [80, 40], [7, 68], [17, 79], [59, 94], [37, 94],
         [87, 49], [55, 89], [66, 34], [16, 29], [63, 24],
         [93, 8], [68, 43], [44, 28], [19, 37], [80, 4]]

test8 = [[90, 45], [87, 57], [4, 30], [67, 13], [50, 29],
         [75, 51], [42, 60], [25, 89], [90, 36], [90, 85],
         [72, 22], [35, 88], [56, 71], [80, 9], [53, 81],
         [22, 62], [19, 65], [30, 85], [15, 8], [66, 14]]


# test "remove"
'''
test4.remove(test4[1])
print("test4 =", test4)
print("test4[0] =", test4[0])
print("test4[1] =", test4[1])
print("test4[2] =", test4[2])
'''


# the parameter is to calculate how many Chargers do we need
count = 0  # calculate the number of Sensors are covered
Charger_Num = 0  # calculate Number of Chargers
Truly_Charger_Point = [[0, 0, 0]]  # set how many Chargers do we need
uxy = [[0, 0]]  # vector coordinate of sector

# set circle parameter
cx = 50  # x coordinate of center of circle
cy = 50  # y coordinate of center of circle
r1 = 20  # radius of Hotspot 1(circle 1)
r2 = 40  # radius of Hotspot 2(circle 2)
cr = 16  # radius of charger
angle = 90  # the angle of sector
sink_r = 36  # cover 100*100 diagram's range (25^2+25^2)^(1/2)

# set the name of title, xlabel, and ylabel
plt.title("SMRU")
plt.xlabel("X(m)")
plt.ylabel("Y(m)")

# set length and width of diagram
plt.xlim(0, 100)
plt.ylim(0, 100)

# randomly Sensor location
for i in range(N):
    for j in range(2):
        Sensor[i][j] = np.random.randint(0, 101)
print("Sensor =", Sensor, "\n")  # show the sensor array


# draw center of circle(Data sink node)
for i in range(sink_num):
    if (i == 0):
        plt.scatter(Data_sink_node[i][0], Data_sink_node[i][1], alpha=1, color="#ff7f0e", marker="s",
                    label="Data sink node")  # marker is square
    else:
        plt.scatter(Data_sink_node[i][0], Data_sink_node[i][1], alpha=1, color="#ff7f0e", marker="s")  # marker is square

# generate 2 circle for Hotspot(radius = 20)
# "fill" parameter is whether to fill the circle
circle1 = plt.Circle((cx, cy), r1, edgecolor="#1f77b4",
                     fill=False, linestyle="--")
circle2 = plt.Circle((cx, cy), r2, edgecolor="#1f77bf",
                     fill=False, linestyle="--")
plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)


# extend column of Charger_Point array
#Charger_Point = test_Sensor_Array.copy()
#Charger_Point = test_Sensor_Array_2.copy()
#Charger_Point = test2.copy()
Charger_Point = Sensor.copy()
#Charger_Point = test3.copy()
#Charger_Point = test4.copy()
#Charger_Point = test5.copy()
#Charger_Point = test6.copy()
#Charger_Point = test7.copy()
#Charger_Point = test8.copy()

for j in range(N):
    # j+1 is because in finally, I will set the included value that
    k = np.array([j+1])
    # in third column to True to avoid repeated selection
    # extend third column to avoid Charger Points are repeated selection
    Charger_Point[j].extend(k)

    # store the number of covered, 0 represent the point is covered by other point
    l = np.array([0])
    Charger_Point[j].extend(l)

    # store static sensor number
    Charger_Point[j].extend(k)

    # store list(covered point) in Charger_Point[i][5]
    Charger_Point[j].extend([[0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0,
                              0, 0]])

    # for record sector angle
    Charger_Point[j].extend(l)

List5_Length = 12
# test the num whether is correct
#print("Charger_Point original =", Charger_Point, "\n")

# calculate how many Chargers do we need
Truly_Row = 0  # to count how many times did Truly_Charger_Point did
# record the previous max value to compare now max value
Previous_Max_Sensor_Number = 0
Max_count = 0  # temporarily store max value every degrees, finally assign value to Max_Sensor_
Max_Sensor_Degree = float(0)  # record the best degree
while_count = 0
sum_time = float(0)
avg_Charger_Num = float(0)
while_count_2 = 0
over3times = 0
temp_flag = False
Mobility_Revision_Time = float(0)

while(True):
    while_count_2 = 0
    Best_Charger_Num = 0
    ######## Break judgment area ########
    while_count += 1
    if (while_count > 1):
        break
    print("while_count =", while_count)

    Charger_Num = 0
    Truly_Row = 0
    Truly_Charger_Point = [[0, 0, 0]]

    
    # randomly Sensor location
    for i in range(N):
        #for j in range(2):
        #    Charger_Point[i][j] = np.random.randint(0, 101)
        for j in range(List5_Length):
            Charger_Point[i][5][j] = 0
        Charger_Point[i][2] = i+1
        Charger_Point[i][3] = 0
        Charger_Point[i][4] = i+1
        Charger_Point[i][6] = -1
    #print("Charger_Point =", Charger_Point)


    for i in range(100):  # do N times shuffle
        # shuffle Charger_Point Array
        for j in range(N):
            # because high range is < high, thus high = N
            randnum = np.random.randint(low=0, high=(N), size=None)
            Charger_Point[j], Charger_Point[randnum] = Swap(
                Charger_Point[j], Charger_Point[randnum])
    # print to check whether is shuffled
    #print("Charger_Point =", Charger_Point, "\n")


    while(True):
        ######## Break judgment area ########
        while_count_2 += 1
        if (while_count_2 > 1):
            break
        print("while_count_2 =", while_count_2)

        Charger_Num = 0

        # reset Charger_Point
        # for i in range(N):
        #    Charger_Point[i][2] = i+1
        for i in range(100):  # do N times shuffle
            # shuffle Charger_Point Array
            for j in range(N):
                # because high range is < high, thus high = N
                randnum = np.random.randint(low=0, high=(N), size=None)
                Charger_Point[j], Charger_Point[randnum] = Swap(
                    Charger_Point[j], Charger_Point[randnum])
        # print to check whether is shuffled
        #print("Charger_Point =", Charger_Point)

        time_start = time.time()
        ######## the part of calculating the covered point ########
        for i in range(N):
            # if third column is not 0, record the point is Charger_Point
            if (Charger_Point[i][2] != 0):
                Previous_Max_Sensor_Number = 0  # reset to initial
                around_count = 0

                Charger_Num += 1  # record Number of Chargers

                # convert Cartesian Coordinates to Polor Coordinates
                for j in range(360):
                    #CPr, CPtheta = Convert_to_Polor(Charger_Point[i][0], Charger_Point[i][1], uxy[0][0], uxy[0][1])
                    Max_count = 0  # reset to initial
                    CPtheta = j
                    # calculate start_arm and end_arm(the angle of sector is set 90 degrees)
                    CPtheta, start_arm, end_arm = Theta_Conversion(
                        CPtheta, (angle/2))
                    #print(Truly_Row+1, "times\n")
                    #print("CPtheta =", CPtheta, "\n")
                    #print("start_arm =", start_arm, "\n")
                    #print("end_arm =", end_arm, "\n")

                    for m in range(N):
                        # convert to polor coordinates and compare them
                        Sensor_r, Sensor_theta = Convert_to_Polor(
                            Charger_Point[i][0], Charger_Point[i][1], Charger_Point[m][0], Charger_Point[m][1])
                        Sensor_theta, Trash_Can_start_arm, Trash_Can_end_arm = Theta_Conversion(
                            Sensor_theta, (angle/2))

                        # catch the max_count of every angle
                        if (Sensor_r <= cr):
                            around_count += 1
                            if (Sensor_theta == 0 and Sensor_r == 0):
                                Max_count += 1
                            elif (start_arm > end_arm):
                                if (Sensor_theta <= end_arm or Sensor_theta >= start_arm):
                                    Max_count += 1
                            else:
                                if (start_arm <= Sensor_theta and end_arm >= Sensor_theta):
                                    Max_count += 1

                    # update PMSN
                    if (Max_count > Previous_Max_Sensor_Number):
                        Previous_Max_Sensor_Number = Max_count
                        Max_Sensor_Degree = j
                        Best_start_arm = start_arm
                        Best_end_arm = end_arm

                # Sensor will must be detected by itself, so PMSN at least == 1
                if (Previous_Max_Sensor_Number == 1):
                    # generate vector of sector for next step to calculate Polor Coordinates
                    while(True):
                        uxy = [
                            [np.random.randint(low=0, high=101), np.random.randint(low=0, high=101)]]
                        #print(uxy, uxy[0][0], uxy[0][1])
                        if ((uxy[0][0] != Charger_Point[i][0]) or (uxy[0][1] != Charger_Point[i][1])):
                            break

                    CPr, CPtheta = Convert_to_Polor(
                        Charger_Point[i][0], Charger_Point[i][1], uxy[0][0], uxy[0][1])
                    # Max_count = 0  # reset to initial
                    #CPtheta = j
                    # calculate start_arm and end_arm(the angle of sector is set 90 degrees)
                    CPtheta, Best_start_arm, Best_end_arm = Theta_Conversion(
                        CPtheta, (angle/2))
                    Max_Sensor_Degree = int(CPtheta)

                Charger_Point[i][3] = Previous_Max_Sensor_Number
                Charger_Point[i][6] = Max_Sensor_Degree

                # find the point has more covered points
                if (around_count >= 3):
                    cover_flag = True
                    for j in range(N):
                        if (i == j):
                            continue
                        if (Charger_Point[j][2] != 0):
                            # find the point is in range and uncovered
                            if cover_flag == True:
                                over3times += 1
                                cover_flag = False

                            Sensor_r, Sensor_theta = Convert_to_Polor(
                                Charger_Point[i][0], Charger_Point[i][1], Charger_Point[j][0], Charger_Point[j][1])
                            Sensor_theta, Trash_Can_start_arm, Trash_Can_end_arm = Theta_Conversion(
                                Sensor_theta, (angle/2))

                            if (Sensor_r <= cr):
                                Uncovered_Point = Charger_Point[j]
                                #print("Charger_Point[i] =", Charger_Point[i])
                                #print("Uncovered_Point =", Uncovered_Point)
                                #print("over3times =", over3times)
                                #print("Sensor_theta =", Sensor_theta, "\n")

                                temp_Previous_Max_Sensor_Number = 0
                                # examine the uncovered point whether can cover more point
                                for k in range(360):
                                    Max_count = 0
                                    CPtheta = k
                                    CPtheta, start_arm, end_arm = Theta_Conversion(
                                        CPtheta, (angle/2))
                                    for m in range(N):
                                        if (Charger_Point[m][4] != 0):
                                            temp_Sensor_r, temp_Sensor_theta = Convert_to_Polor(
                                                Charger_Point[j][0], Charger_Point[j][1], Charger_Point[m][0],
                                                Charger_Point[m][1])
                                            temp_Sensor_theta, Trash_Can_start_arm, Trash_Can_end_arm = Theta_Conversion(
                                                temp_Sensor_theta, (angle/2))
                                            if (temp_Sensor_r <= cr):
                                                if (temp_Sensor_theta == 0 and temp_Sensor_r == 0):
                                                    Max_count += 1
                                                elif (start_arm > end_arm):
                                                    if (temp_Sensor_theta <= end_arm or temp_Sensor_theta >= start_arm):
                                                        Max_count += 1
                                                else:
                                                    if (start_arm <= temp_Sensor_theta and end_arm >= temp_Sensor_theta):
                                                        Max_count += 1
                                    if (Max_count > temp_Previous_Max_Sensor_Number):
                                        temp_Previous_Max_Sensor_Number = Max_count
                                        temp_Max_Sensor_Degree = k
                                        temp_Best_start_arm = start_arm
                                        temp_Best_end_arm = end_arm
                                if (temp_Previous_Max_Sensor_Number > Previous_Max_Sensor_Number):
                                    # switch the charger and covered number
                                    Charger_Point[i][3] = 0
                                    Charger_Point[i][6] = 0
                                    Charger_Point[j][3] = temp_Previous_Max_Sensor_Number
                                    Charger_Point[j][6] = temp_Max_Sensor_Degree
                                    #print("Previous_Max_Sensor_Number =",
                                    #      Previous_Max_Sensor_Number)
                                    #print("temp_Previous_Max_Sensor_Number =",
                                    #      temp_Previous_Max_Sensor_Number)
                                    Charger_Point[i], Charger_Point[j] = Swap(
                                        Charger_Point[i], Charger_Point[j])
                                    #print(
                                    #    "after Swap Charger_Point[i] =", Charger_Point[i])
                                    #print(
                                    #    "after Swap Charger_Point[j] =", Charger_Point[j], "\n")
                                    Best_start_arm = temp_Best_start_arm
                                    Best_end_arm = temp_Best_end_arm
                                    Previous_Max_Sensor_Number = temp_Previous_Max_Sensor_Number
                                    Max_Sensor_Degree = temp_Max_Sensor_Degree


                temp_Number_Count = 0
                # erase the covered points(set flag is True)
                for j in range(N):
                    # if (Charger_Point[j][2] != 0):
                    # convert to polor coordinates and compare them
                    Sensor_r, Sensor_theta = Convert_to_Polor(
                        Charger_Point[i][0], Charger_Point[i][1], Charger_Point[j][0], Charger_Point[j][1])
                    Sensor_theta, Trash_Can_start_arm, Trash_Can_end_arm = Theta_Conversion(
                        Sensor_theta, (angle/2))

                    # calculate whether Sensor is in the sector
                    if (Sensor_r <= cr):
                        if (Sensor_theta == 0 and Sensor_r == 0):
                            Charger_Point[j][2] = 0
                            Charger_Point[i][5][temp_Number_Count] = Charger_Point[j][4]
                            temp_Number_Count += 1
                        elif (Best_start_arm > Best_end_arm):
                            if (Sensor_theta <= Best_end_arm or Sensor_theta >= Best_start_arm):
                                Charger_Point[j][2] = 0
                                Charger_Point[i][5][temp_Number_Count] = Charger_Point[j][4]
                                temp_Number_Count += 1
                        else:
                            if (Best_start_arm <= Sensor_theta and Best_end_arm >= Sensor_theta):
                                Charger_Point[j][2] = 0
                                Charger_Point[i][5][temp_Number_Count] = Charger_Point[j][4]
                                temp_Number_Count += 1

                # set a array to be merged in Truly_Charger_Point Array
                Array_Merge = Charger_Point[i].copy()

                # first time, let row index[0] == first point index, other points use expansion to fulfill array
                if (i == 0):
                    Truly_Charger_Point = Array_Merge.copy()
                    #print("Truly_Charger_Point =", Truly_Charger_Point)
                else:
                    Truly_Charger_Point = np.row_stack(
                        (Truly_Charger_Point, Array_Merge))
                    Truly_Row += 1

                Charger_Point[i][2] = 0

        #print("Truly_Row =", Truly_Row)
        #print("Original Charger Num =", Charger_Num)
        #print("Not Delete Truly_Charger_Point =", Truly_Charger_Point)
        #print("Original_Truly_Charger_Point =", Truly_Charger_Point, "\n")

        temp_Delete_Charger = [0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0]
        temp_column = 0
        # search the useless charger, List5_Length is the length of Charger_Point[i][5]
        for i in range(Truly_Row+1):
            if (Truly_Charger_Point[i][5][1] != 0):
                temp_count = 0
                for j in range(List5_Length):
                    L_Break_Flag = False
                    if (Truly_Charger_Point[i][5][j] == 0):
                        break
                    for k in range(Truly_Row+1):
                        if (Truly_Charger_Point[i][4] == Truly_Charger_Point[k][4]):
                            #print("continue", i, k)
                            continue
                        for l in range(List5_Length):
                            if (Truly_Charger_Point[k][5][l] == 0):
                                break
                            if (Truly_Charger_Point[i][5][j] == Truly_Charger_Point[k][5][l]):
                                temp_count += 1
                                #print("temp_count =", temp_count)
                                L_Break_Flag = True
                                break
                        if (L_Break_Flag == True):
                            L_Break_Flag = False
                            break
                # [i][3] is the covered number
                if (Truly_Charger_Point[i][3] == temp_count):
                    #print("delete", i)
                    #Truly_Charger_Point = np.delete(Truly_Charger_Point, temp_Delete_Charger[i], 0)
                    for k in range(List5_Length):
                        Truly_Charger_Point[i][5][k] = 0
                    temp_Delete_Charger[temp_column] = i+1  # i+1 == Row+1
                    temp_column += 1
                    #print("after delete =", Truly_Charger_Point)
                    #Truly_Row -= 1
                    #Charger_Num -= 1
                    #i -= 1

        #print("Charger_Point =", Charger_Point)
        #print("Charger_Num =", Charger_Num, "\n")

        #print("Original_Truly_Charger_Point =", Truly_Charger_Point, "\n")
        #print("temp_Delete_Charger[0] =", temp_Delete_Charger[0])

        
        # for the list sequence do not be affect
        temp_Delete_Charger.sort(reverse=True)
        for i in range(temp_column):
            if (temp_Delete_Charger[i] == 0):
                continue
            Truly_Row -= 1
            Charger_Num -= 1
            Truly_Charger_Point = np.delete(
                Truly_Charger_Point, temp_Delete_Charger[i]-1, 0)


        print("Charger_Num =", Charger_Num, "\n")

        
        if (while_count_2 == 1):
            Best_Charger_Num = Charger_Num
            Best_Charger_Point = Charger_Point.copy()
        else:
            if (Charger_Num < Best_Charger_Num):
                Best_Charger_Num = Charger_Num
                Best_Charger_Point = Charger_Point.copy()
        

    time_end = time.time()
    sum_time += (time_end - time_start)
    avg_Charger_Num += Charger_Num
    #avg_Charger_Num += Best_Charger_Num

avg_sum_time = sum_time / (while_count-1)
avg_Charger_Num = (avg_Charger_Num / (while_count-1))
print("sum_time =", sum_time, "sec")
print("avg_sum_time =", avg_sum_time, "sec")
print("avg_Charger_Num =", avg_Charger_Num, "\n\n")
print("Truly_Charger_Point =", Truly_Charger_Point)
#print("Charger_Point =", Charger_Point)



# draw Charger
for i in range(N):
    Charger_Point[i][2] = i+1

# draw sensor point
for i in range(N):
    if (i == 0):
        plt.scatter(Charger_Point[i][0], Charger_Point[i][1], alpha=0.6,
                    color="#1f77b4", marker="d", label="Sensor")
    else:
        plt.scatter(Charger_Point[i][0], Charger_Point[i][1], alpha=0.6,
                    color="#1f77b4", marker="d")

for i in range(Charger_Num):
    Previous_Max_Sensor_Number = 0

    Truly_Charger_Point[i][6], Best_start_arm, Best_end_arm = Theta_Conversion(
        Truly_Charger_Point[i][6], (angle/2))

    # erase the covered points(set flag is True)
    for j in range(N):
        # convert to polor coordinates and compare them
        Sensor_r, Sensor_theta = Convert_to_Polor(
            Truly_Charger_Point[i][0], Truly_Charger_Point[i][1], Charger_Point[j][0], Charger_Point[j][1])
        Sensor_theta, Trash_Can_start_arm, Trash_Can_end_arm = Theta_Conversion(
            Sensor_theta, (angle/2))

        # calculate whether Sensor is in the sector
        if (Sensor_r <= cr):
            if (Sensor_theta == 0 and Sensor_r == 0):
                Charger_Point[j][2] = 0
            elif (Best_start_arm > Best_end_arm):
                if (Sensor_theta <= Best_end_arm or Sensor_theta >= Best_start_arm):
                    Charger_Point[j][2] = 0
            else:
                if (Best_start_arm <= Sensor_theta and Best_end_arm >= Sensor_theta):
                    Charger_Point[j][2] = 0

    # set sector range of drawing
    if (i == 0):
        wedge = mpatches.Wedge(
            (Truly_Charger_Point[i][0], Truly_Charger_Point[i][1]), cr, Best_start_arm, Best_end_arm, ec="none")
    else:
        wedge = mpatches.Wedge(
            (Truly_Charger_Point[i][0], Truly_Charger_Point[i][1]), cr, Best_start_arm, Best_end_arm, ec="none")

    # set parameters of sector and draw
    wedge.set_label("Charger")
    wedge.set_edgecolor("black")
    wedge.set_facecolor("lightgreen")
    wedge.set_alpha(0.2)
    plt.gcf().gca().add_artist(wedge)

    if (i == 0):
        plt.scatter(Truly_Charger_Point[i][0], Truly_Charger_Point[i][1], alpha=0.6,
                    color="green", marker="o", label="Charger")  # set the center of sector
    else:
        plt.scatter(Truly_Charger_Point[i][0], Truly_Charger_Point[i][1],
                    alpha=0.6, color="green", marker="o")  # set the center of sector

# draw legend
plt.legend(loc="upper right")

# show the diagram
plt.show()
