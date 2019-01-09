file = open ('tmp.md','w')
try:
    file.write("Hello Python!!!")
finally:
    file.close()