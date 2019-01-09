# encoding: utf-8

try:
    n = input("Dividend: ")
    d = input("divisor: ")
    print (n / d)
except Exception, err:
    print ("Error found: {}".format(err))
finally:
    print ("Finish")
