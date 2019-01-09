#def

def add(a,b):
    return a+b

print (add(5,8))
print (add([5,2],[8,2,-9]))


def append_list(a,b=[]):
    b.append(a)
    print(b)

append_list(1)
append_list(2)
append_list([3,4,5])

append_list.char ='a'
print (append_list.char)
