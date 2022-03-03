'''
Write a program to generate new 6 charcter OTP after every 10 seconds.
OTP should  have lower,upper case,numbers and special symbols
'''
# https://docs.python.org/3/library/time.html#time.sleep
# https://docs.python.org/3/library/random.html#random.random
# https://docs.python.org/3/library/math.html#math.floor
# https://docs.python.org/3/library/string.html#string-constants
import math
import time
import random
def otp_generator(pass_length):
  while True:
    digits ='01234567890'#string.digits
    special_char='!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~'#string.punctuation
    low_char="abcdefghijklmnopqrstuvwxyz"#string.ascii_lowercase
    upper_char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#string.ascii_uppercase
    string=digits+special_char+low_char+upper_char#string.printable
    length = len(string)
    otp = ""
    for i in range(pass_length):
            index= math.floor(random.random() * length)
            otp += string[index]
    print(otp)
    time.sleep(10)
if __name__ == "__main__" :
    pass_length=int(input("Enter number of digits in OTP:"))
    otp_generator(pass_length)