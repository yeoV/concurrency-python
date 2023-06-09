"""
# Asyncio : 비동기 처리가 가능한 Class 생성하기
# -> __aenter__, __aexit__ 반드시 구현해야 함
"""
import asyncio


class AsyncAdd:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    async def __aenter__(self):
        await asyncio.sleep(1)
        return self.a + self.b

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass


async def main():
    async with AsyncAdd(1, 2) as result:
        print(result)  # 3


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
