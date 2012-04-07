import math
import operator

def isPrime(number):
    if number==1:
        return False
    prime=True
    for i in range(2,int(math.sqrt(number))+1):
        if float(number)%i == 0:
            prime =False
    return prime
    
def nextPrime(number):
    while(1):
        number+=1
        if isPrime(number):
            return number
            
def find_divisors(number):
    '''Find all the divisors of the given number'''
    divisors=[1,number]
    for i in lrange(2,number):

        if number%i == 0:
            #divisors.append(i)
            print i
            
    return sorted(divisors)
    
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step
        
def nextDivisor(number,divisor):
'''Gets the next smaller divisor for the given number which less than given divisor'''
    if divisor==1 : return None
    dividend = float(number)/divisor
    if dividend - float(int(dividend))==0.0:
        dividend+=1
    while(1):
        if float(number)/dividend==float(int(float(number)/dividend)):
            return int(float(number)/dividend)
        else: dividend+=1
            
            
          
    
    
