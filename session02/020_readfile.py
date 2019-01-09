#read files
file = open("020.py",'r')
#print (file.read())
print (file.readlines())

for line in file:
    print (line)

file.close()