"""
# 에라토스테네스의 체를 활용한 Process / Thread Pool 속도 비교

"""
import timeit
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    #
    print("-----------------ProcessPoolExecutor------------------")
    t1 = timeit.default_timer()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for number, result in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime? : {result}")
    print(f"Seconds Needed For ProcessPoolExecutor {timeit.default_timer() - t1}")

    print("-----------------ThreadPoolExecutor------------------")
    t2 = timeit.default_timer()
    with ThreadPoolExecutor(max_workers=3) as executor:
        for number, result in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime? : {result}")
    print(f"Seconds Needed For ThreadPoolExecutor {timeit.default_timer() - t2}")
    print("-----------------SingleThreadExecutor------------------")
    t3 = timeit.default_timer()
    for number in PRIMES:
        print(f"{number} is prime? : {is_prime(number)}")
    print(f"Seconds Needed For SingleThread {timeit.default_timer() - t3}")


if __name__ == "__main__":
    main()

#  Result :
# -----------------ProcessPoolExecutor------------------
# 112272535095293 is prime? : True
# 112582705942171 is prime? : True
# 112272535095293 is prime? : True
# 115280095190773 is prime? : True
# 115797848077099 is prime? : True
# 1099726899285419 is prime? : False
# Seconds Needed For ProcessPoolExecutor 0.9324446249999999
# -----------------ThreadPoolExecutor------------------
# 112272535095293 is prime? : True
# 112582705942171 is prime? : True
# 112272535095293 is prime? : True
# 115280095190773 is prime? : True
# 115797848077099 is prime? : True
# 1099726899285419 is prime? : False
# Seconds Needed For ThreadPoolExecutor 2.0565163749999997
# -----------------SingleThreadExecutor------------------
# 112272535095293 is prime? : True
# 112582705942171 is prime? : True
# 112272535095293 is prime? : True
# 115280095190773 is prime? : True
# 115797848077099 is prime? : True
# 1099726899285419 is prime? : False
# Seconds Needed For SingleThread 2.0578970410000004