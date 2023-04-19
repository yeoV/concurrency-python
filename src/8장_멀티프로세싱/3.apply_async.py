"""
# concurrent.futures.ProcessPoolExecutor 
# multiprocessing.Pool
# 차이점 :
# 1. multiprocessing.Pool 은 거의 동일한 구현 형태를 지닌다.
# 2. concurrent.futures 모듈은 프로세스 풀 생성을 쉽게 해주는 인터페이스만 지원 -> 스레드 / 프로세스 풀 모두 즉각적 시작 가능
-> 그러나, 세밀한 조정이 필요할 경우 불필요

# with -> Pool 생성 가능
# map -> process call 가능
# apply -> call / 동기 처리
# apply_async -> call / 비동기 처리
"""

from multiprocessing import Pool
import os


def task(n):
    print(f"Task PID : {os.getpid()}, result : {n}")


def main():
    with Pool(4) as p:
        print(p.map(task, [2, 3, 4]))
        print(p.apply(task, (5,)))  # 동기
        print(p.apply(task, (6,)))  # 동기

        for idx in range(4):
            my_task = p.apply_async(task, (idx,))
            my_task.wait()


if __name__ == "__main__":
    main()
