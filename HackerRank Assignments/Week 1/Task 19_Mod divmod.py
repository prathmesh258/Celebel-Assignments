
# Task
# Read in two integers, a and b , and print three lines.
# The first line is the integer division  (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: .
# The third line prints the divmod of a and b .


dividend = int(input())
divisor = int(input())
'''
quo,rem=divmod(dividend,divisor)
print(quo)
print(rem)
print((quo,rem))
'''
print(dividend//divisor)
print(dividend%divisor)
print(divmod(dividend,divisor))
