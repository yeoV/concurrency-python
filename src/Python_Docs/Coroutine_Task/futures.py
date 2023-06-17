import asyncio
import concurrent.futures


def blocking_io():
    # File Operation
    # Event Loop : run them in a thread Pool

    with open("/test/data", "rb") as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound opeerations will block the event Loop
    # 일반적으로 Process Pool을 사용하는 것이 더 일반적
    return sum(i * i for i in range(10**7))


async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in default loop's executor:
    # run_in_executor -> 더이상 max_worker 지정 안함. 스스로 기본값 설장
    result = await loop.run_in_executor(None, blocking_io)
    print("Default thread Pool", result)

    # 2. Run in Custom Thread Pool
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
    print("Custom Thread pool", result)

    # 3. Run in a custom process Pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print("Custom Process Pool", result)


if __name__ == "__main__":
    asyncio.run(main())
