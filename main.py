import serialPython
import time

# set up the serial line
ser = serial.Serial('COM3', 9600)
time.sleep(2)

# Read and record the data
data = []                       # empty list to store the data
for i in range(50):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    value = string        # convert string to float
    print(value)
    data.append(value)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()

# show the data
for line in data:
    print(line)

