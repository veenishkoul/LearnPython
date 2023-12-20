#Input the argumnets while running the code 
import sys
n = len(sys.argv)
print("Enter the arguments :", n)
print("Name of the python script :", sys.argv[0])
#This code generates recursive numbers in next lines 
x = 0
while x < 10:
        print("Hello world : ", x + 1)
        x = x + 1
