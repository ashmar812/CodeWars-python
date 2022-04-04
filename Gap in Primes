#this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise None
from math import sqrt

def gap(g, m, n):
    for i in range(m,n):
        flag = True
        if check_prime(i) and check_prime(i+g):
            for z in range(i+1,i+g):
                if check_prime(z):
                    flag=False
            if flag:
                return [i,i+g]
    return None
    
def check_prime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
