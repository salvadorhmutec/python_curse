#Conversion de tipos de datos
from fractions import Fraction
from decimal import Decimal

print ("Float ", 9.56e5)
print ("Integer ", int(9.56e5))
print ("Integer ",int('-98'))
print ("Integer ",int('1111',2))
print ("Integer ",int('0b1111',0))

print ("Float ",float(9))
print ("Float ",float('1e2'))
print ("Float ",float('-.1'))
print ("Float ",float(0.3))


print ("Complex ",complex(3,4.0))

print ("Fraction ",Fraction(1,10))

print ("Decimal ",Decimal(0.3))