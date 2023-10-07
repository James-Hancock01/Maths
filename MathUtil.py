from tqdm import tqdm
import time
import math
"""Note: the quiet parameter is to identify whether the progress bar should be visible when running"""

def isPrime(p: int) -> bool:    #Checks if p is primes
    """Primality test using 6k+-1 optimization."""
    if p <= 3:
        return p > 1
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i ** 2 <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True

def SieveOfErastosthenes(end = 10, quiet: bool = True): # Using the Sieve of Erastosthenes algorithm for finding primes
    end += 1
    if end < 2: return []
    if end < 3: return [2]

    primes = [True]*(end+1)   #all numbers set as primes initially
    with tqdm(total = end-1, desc = 'Finding Primes', disable = quiet) as pbar:
        pbar.update(2)
    #modifies prime flag in list for odd numbers
        for i in range(3,math.ceil(math.sqrt(end)), 2): #check odd numbers for primes
            pbar.update(2)
            if primes[i]:   #a prime
                primes[i*i::i] = [False]*len(primes[i*i::i])    #from i^2 in increments of i
                #pbar.update( end//i +1)
        pbar.close()
        return [2] + [i for i in range(3,end, 2) if primes[i]]

def PrimesToLimit(end=1000, quiet: bool = False):
    return SieveOfErastosthenes(end, quiet)

def PrimeFactorisation(n, duplicates:bool = True, quiet: bool = True):
    primes = PrimesToLimit(n, quiet)
    #print("Primes: ", primes)
    factorisation = []
    while n != 1:
        for p in primes:
            if n % p == 0:
                #print(("{0}%{1}={2}").format(n,p,n%p))
                factorisation.append(p)
                #print(("{0}/{1}={2}").format(n,p,n/p))
                n /= p
                if duplicates == False:
                    while n % p == 0:
                        n /= p  #removes duplicates if specified
                if n == 1: break
    factorisation.sort()
    return factorisation

def LCM(m: int, n: int) -> int:  #LowestCommonMultiple
    return int(m*n/GCD(m,n))

def GCD(m: int, n: int) -> int:   #GreatestCommonDivisor
    if m == 0: return n
    if n == 0: return m
    if n > m:
        swap = m
        m = n
        n = swap
    #print(("{0} = {1}x{2} + {3}").format(m, n, 'Q', m%n))

    return(GCD(n, m%n))

def divisors(n: int):
    divisors = []
    for i in range(1,int(n)):
            if n % i == 0: divisors.append(i)
    return divisors

def turning_points(array):
    ''' turning_points(array) -> min_indices, max_indices
    Finds the turning points within an 1D array and returns the indices of the minimum and 
    maximum turning points in two separate lists.
    '''
    idx_max, idx_min = [], []
    if (len(array) < 3): 
        return idx_min, idx_max

    NEUTRAL, RISING, FALLING = range(3)
    def get_state(a, b):
        if a < b: return RISING
        if a > b: return FALLING
        return NEUTRAL

    ps = get_state(array[0], array[1])
    begin = 1
    for i in range(2, len(array)):
        s = get_state(array[i - 1], array[i])
        if s != NEUTRAL:
            if ps != NEUTRAL and ps != s:
                if s == FALLING: 
                    idx_max.append((begin + i - 1) // 2)
                else:
                    idx_min.append((begin + i - 1) // 2)
            begin = i
            ps = s
    return idx_min, idx_max

print(len(SieveOfErastosthenes(10000000, False)))