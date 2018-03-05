#to see current directory
! ls 

file=open("isil.txt", mode="r")
print(file.read())
print(file.closed)
file.close()
print(file.closed)
