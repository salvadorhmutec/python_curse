#string methods

import string

foo = "how are you?"
print (foo.capitalize())
print (foo.count("H",0))
print (foo.find("o"))
print (foo.rfind("o"))
print (foo.isalnum())
print (foo.isalpha())
print (foo.islower())
print (foo.upper())
print (foo.replace("a","4"))
print (foo.split(" "))
print (foo.title())
print (string.ascii_letters)
print (string.digits)
print (string.punctuation)
print (foo[2:])