import sys
import math
import random

"""
Reference: https://en.wikipedia.org/wiki/Trial_division
"""
def factorize(comp):
    final = ''
    count = 0
    primeVal = 2
    if comp == 0:
        return
    while checkEven(comp):
        comp = comp // primeVal
        count += 1
    if count == 0:
        pass
    else:
        if comp == 1:
            final += (str(primeVal) + "^" + str(count))
        else:
            final += (str(primeVal) + "^" + str(count) + " x ")
    count = 0
    primeVal = 3
    while primeVal * primeVal <= comp:
        if comp % primeVal == 0:
            primeVal = primeVal
            comp = comp // primeVal
            count += 1
        elif comp%primeVal != 0:
            primeVal += 2

    if comp != 1:
        primeVal = comp
        count += 1
    if count == 0:
        pass
    else:
        final += (str(primeVal) + "^" + str(count))
    return final




def checkEven(n):
    if n%2==0:
        return True
    else:
        return False




def MilnerRabinRandomizedProbability(n,k=16):

    if n == 0 or n ==1 or n==2:
        return True

    if checkEven(n) == True:
        return False

    s = 0
    t = n - 1
    while checkEven(n):
        s = s + 1
        t = t // 2

    for i in range(k):
        random.seed()
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n)!= 1:
            return False

        for i in range(1, s):
            if pow(a, (2 ** i) * t, n) == 1 and (pow(a, (2 ** (i - 1)) * t, n) != 1 or pow(a, (2 ** (i - 1)) * t, n) != n - 1):
                return False
    return True


arr = [] #prime number array
comp = [] #composite number array
count = 0

N = sys.argv[1]
#N = 542
#N = 100000000

if int(N) <542:
    print("Wrong input. N should be greater than or equal to 542. ")
else:
    for i in range(int(N),1,-1):
        if MilnerRabinRandomizedProbability(i) == True:
            comp.append(i+1)
            count += 1
            if count >= 100:
                break

    #print(len(comp))
    comp = comp[::-1]
    # for i in comp:
    #     print(str(i) + "  " + str(factorize(i)))

    file = open('output_factors.txt', 'w')
    for i in comp:
        file.write(str(i) + "  " + str(factorize(i)) + "\n")
    file.close()
