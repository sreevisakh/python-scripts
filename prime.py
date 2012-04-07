import math


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
            
        
