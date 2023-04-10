from concurrent.futures import ProcessPoolExecutor
import math
import os

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]


def is_prime(n):
    print(f"Now Executing {os.getpid()}")
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
    with ProcessPoolExecutor(max_workers=2) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f" {number} number is : {prime}")


if __name__ == "__main__":
    main()

"""
Now Executing 12424
Now Executing 12423
Now Executing 12423
Now Executing 12424
112272535095293 number is : True
112582705942171 number is : True
Now Executing 12423
112272535095293 number is : True
Now Executing 12424
115280095190773 number is : True
115797848077099 number is : True
1099726899285419 number is : False

-> 2개의 ProcessThread로 인해 os.getid() 2개 생성
"""
