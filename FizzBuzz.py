stevilo_x = raw_input ("vnesi stevilo med 1 in 100:")

a = int(stevilo_x)
b = 0

while a != b:
    b = b+1
    print b

if b % 3 == 0:
    print "fizz"

elif b % 5 == 0:
    print "buzz"

elif b % 3 == 0 and b % 5 == 0:
    print "fizzbuzz"

else:
    print b