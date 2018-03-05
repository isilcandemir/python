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

#for excel
import pandas as pd
file="urbanpop.xlsx"
data=pd.ExcelFile(file)
print(data.sheet_names)
df1 = xl.parse('2004')
print(df1.head())

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])
