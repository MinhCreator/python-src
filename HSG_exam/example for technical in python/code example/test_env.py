def sieve(num_in: int) -> list[int]:

    mark_prime = [True] * (num_in + 1)

    prime_init = 2

    while prime_init * prime_init <= num_in:

        if mark_prime[prime_init]:

            for num in range(prime_init * prime_init, num_in + 1, prime_init):
                mark_prime[num] = False

        prime_init += 1

    return [num for num in range(2, num_in + 1) if mark_prime[num]]


print(sieve(10))
from math import floor, sqrt
def is_prime(num: int) -> bool:

    if num == 2 or num == 3 : return True

    if num % 2 == 0 or num % 3 == 0: return False

    if num == 1: return False
    
    if num == 0: return False

    else:

       num_k = 5
       num_floor = floor(sqrt(num))

       while num_k <= num_floor:
           
           if num % num_k == 0 or num % (num_k + 2) == 0 :
               return False
           num_k += 6

       return True
    

import unittest

class TestIsPrime(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(__import__('test_env'))

    # Create a TextTestRunner to run the tests and capture the results
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Print the test results
    print(result)