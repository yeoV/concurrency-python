import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # 3개 scheduler call
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("A", 3),
        factorial("A", 4),
    )
    print(L)


asyncio.run(main())

# 모든 Task가 끝나고 나서 최종 결과를 리턴.
# Task A: Compute factorial(2), currently i=2...
# Task A: Compute factorial(3), currently i=2...
# Task A: Compute factorial(4), currently i=2...
# Task A: factorial(2) = 2
# Task A: Compute factorial(3), currently i=3...
# Task A: Compute factorial(4), currently i=3...
# Task A: factorial(3) = 6
# Task A: Compute factorial(4), currently i=4...
# Task A: factorial(4) = 24
# [2, 6, 24]
