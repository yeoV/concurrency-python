import timeit
from urllib.request import Request, urlopen
import asyncio

urls = [
    "https://www.google.co.kr/search?q=" + i
    for i in ["apple", "pear", "grape", "pineapple", "orange", "strawberry"]
]

loop = asyncio.get_event_loop()


def sync_call():
    result = []
    for url in urls:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request)
        page = response.read()
        result.append(len(page))

    print(result)


async def fetch(url):
    global loop
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)


async def async_call():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]  # 태스트(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)  # 결과를 한번에 가져옴
    print(result)


def main():
    global loop
    print("-----------------Sync----------------- ")
    t1 = timeit.default_timer()
    sync_call()
    print(f"Execution Time : {timeit.default_timer() - t1}")

    print("-----------------Async----------------- ")
    t2 = timeit.default_timer()
    loop.run_until_complete(async_call())
    print(f"Execution Time : {timeit.default_timer() - t2}")
    loop.close()


if __name__ == "__main__":
    main()

# -----------------Sync----------------- 
# [255076, 112595, 103890, 318568, 64831, 148402]
# Execution Time : 8.076353792
# -----------------Async----------------- 
# [257200, 112595, 103890, 316429, 64831, 148402]
# Execution Time : 1.8979705420000013
# 비동기 -> 동기보다 6배 정도 빠름