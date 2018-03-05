#to see current directory
! ls 

file=open("isil.txt", mode="r")
print(file.read())
print(file.closed)
file.close()
print(file.closed)

#for data containing only number
import numpy as np
file = 'digits.csv'
digits = np.loadtxt(file, delimiter=",")
print(type(digits))

# for everytype data
import pandas as pd
file="winequality-red.csv"
data=pd.read_csv(filename)



