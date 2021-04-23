import random
from concurrent.futures import ThreadPoolExecutor

pre_prime_list = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
]


def get_random_num(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n + 1)


def low_primal_test(n):
    while True:
        rand_num = get_random_num(n)

        for div in pre_prime_list:
            if rand_num % div == 0 and div ** 2 <= rand_num:
                break
            else:
                return rand_num


def high_primal_test(n):
    m = n - 1
    k = 0
    while m % 2 == 0:
        m >>= 1
        k += 1
    a = random.randrange(2, n)
    for i in range(n):
        if i == 0:
            res = pow(a, m, n)
            if res == n - 1 or res == 1:
                return n
        else:
            res = pow(res, 2, n)
            if res == 1:
                return -1
            elif res == n - 1:
                return n


def do_work(n):
    for i in range(n):
        prime = low_primal_test(n)
        if not isMillerRabinPassed(prime):
            continue
        else:
            return prime
    return -1


def isMillerRabinPassed(mrc):
    """Run 20 iterations of Rabin Miller Primality test"""
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert 2 ** maxDivisionsByTwo * ec == mrc - 1

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def get_primes(n):
    workers = 5000
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(do_work, [n] * 4)
    p, q = list(filter((-1).__ne__, list(res)))[:2]
    return p, q
