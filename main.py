# Data Analysis - Module 1.0  Version 1.0 (Stable)
# Date Created - 25/03/2024
# Last Update - 25/03/2024


# UI Modules
import numpy as nmpy
import matplotlib.pyplot as plt



# Starting Messages
print("Welcome to Data Analyser - Module 1.0 \n\n")
print("Select the thing you want : ")
print("Trignometric Sine Graph : Enter 1")
print("Trignometric Cosine Graph : Enter 2")
print("Pie-Charts : Enter 3")
print("Line Graphs : Enter 4")



# Functions
def trig_sin():
    deg_val = print("Hey , Enter the degrees")
    deg_val1 = int(input())
    deg_val2 = int(input())
    deg_val3 = int(input())
    deg_val4 = int(input())
    deg_val5 = int(input())

    deg_list = [deg_val1,deg_val2,deg_val3,deg_val4,deg_val5]
    deg_list.sort()
    try:
        radian = [i * (nmpy.pi/180) for i in deg_list]
        plt.plot(deg_list,nmpy.sin(radian),marker="+")
        plt.xticks(deg_list)
        plt.show()
    except:
        print("Invalid Response. Please Try again after restarting the program")
        exit(0)

def trig_cos():
    print("Hey , Enter the degrees")
    deg_val_cos1 = int(input())
    deg_val_cos2 = int(input())
    deg_val_cos3 = int(input())
    deg_val_cos4 = int(input())
    deg_val_cos5 = int(input())

    deg_list_cos = [deg_val_cos1, deg_val_cos2, deg_val_cos3, deg_val_cos4, deg_val_cos5]
    deg_list_cos.sort()
    try:
        cosradian = [x * (nmpy.pi / 180) for x in deg_list_cos]
        plt.plot(deg_list_cos, nmpy.cos(cosradian), marker="+")
        plt.xticks(deg_list_cos)
        plt.show()
    except:
        print("Invalid Response. Please Try again after restarting the program")
        exit(0)


def pie_graph():
    max_val = int(input("Hey. Enter the total number of values for the pie chart : "))
    pie_chart_quant = 0
    raw_name_list = []
    raw_value_list = []
    while(pie_chart_quant<max_val):
        user_quan_name_inp = str(input("Enter the quantity name : "))
        user_quan_value_inp = int(input(f"Enter the value of {user_quan_name_inp} (Will be calculated as percentage) : "))
        raw_name_list.append(user_quan_name_inp)
        raw_value_list.append(user_quan_value_inp)
        pie_chart_quant+=1
    try:
        print(raw_name_list)
        print(raw_value_list)
        plt.pie(raw_value_list,labels=raw_name_list)
        plt.show()
    except:
        print("560 Error")


def line_graph():
    line_max_val = int(input("Enter the number of values : "))
    if (line_max_val>1):
        max_line_val = 0
        line_list = []
        while(max_line_val<line_max_val):
            user_line = int(input("Enter values for the line graph : "))
            line_list.append(user_line)
            max_line_val+=1
        try:
            plt.plot(line_list, linestyle='dashed',marker="+")
            plt.show()
        except:
            print("Invalid. Error code 200")
    else:
        print("Try again with a greater value")


user_choice = int(input("\n\nEnter your choice : "))

try:
    if(user_choice==1):
        trig_sin()
    elif(user_choice==2):
        trig_cos()
    elif(user_choice==3):
        pie_graph()
    elif(user_choice==4):
        line_graph()
    else:
        print("Invalid Response. Exiting Program")
        exit(0)
except:
    print("Error happended. Please restart the program")

