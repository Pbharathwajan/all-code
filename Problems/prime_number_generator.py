import itertools
from math import sqrt   

class stream:
    """ Class of infinite streams. """

    def prime():
        """ Stream of prime numbers. """
        prime_set = {2} # Set of prime numbers that have been found
        yield 2 # First prime
        for x in itertools.count(3, 2): # Check odd numbers, starting with 3
            primes_below_sqrt = {i for i in prime_set if i <= sqrt(x)} 
            for prime in primes_below_sqrt:
                if x % prime == 0:
                    break # x is divisible by a prime factor, so it is not prime
            else:
                prime_set.add(x) # x has been shown to be prime
                yield x 
def take(iterable, n):
    """ Returns first n items of the iterable as a list. """
    return list(itertools.islice(iterable, n))
