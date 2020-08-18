import first_primes as fp
import secrets

first_primes = fp.first_primes

def gen_random(l):
    '''Generate a random number l digits long.'''
    randgenerator = secrets.SystemRandom()
    return randgenerator.randrange(2**(l-1)+1, 2**l - 1)

def low_level_checker(l):
    '''Check that the random number isn't divisible by the first few primes.'''
    e = 65537
    while True:
        x = gen_random(l)
        for divisor in first_primes:
            if x % divisor == 0 and divisor**2 <= x:
                break
        else: return x

def miller_rabin_checker(mrc):
    '''Run 20 iterations of the Miller-Rabin Primality Test.'''
    randgenerator = secrets.SystemRandom()
    max_divisions_by_two = 0
    y = mrc-1
    while y % 2 == 0:
        y >>= 1
        max_divisions_by_two += 1
    assert(2**max_divisions_by_two * y == mrc-1)

    def trial_composite(round_tester):
        if pow(round_tester, y, mrc) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(round_tester, 2**i * y, mrc) == mrc-1:
                return False
        return True
    number_of_rabin_trials = 40
    for i in range(number_of_rabin_trials):
        round_tester = randgenerator.randrange(2, mrc)
        if trial_composite(round_tester):
            return False
    return True

def driver(l):
    while True:
        prime_candidate = low_level_checker(l)
        if not miller_rabin_checker(prime_candidate):
            continue
        else:
            return prime_candidate
