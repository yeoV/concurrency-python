# Python 을 통한 비동기처리

## 1. 코루틴과 태스크

**코루틴**

- 비동기 어플리케이션을 위한 async/await 문법을 사용하 수 있음
- 협력형 멀티 태스킹
- 동시성 프로그래밍 지원
- 멀티쓰레딩 작업보다 동시성 프로그래밍에서 메모리 효율성이 더 좋음
  - 멀티쓰레딩 : 각 쓰레드간 Context Switching 발생
  - 코루틴 : 동일 쓰레드 내 탈출 및 재진입을 활용하여 동시성 프로그래밍을 가능하게 함

#### 1.2 어웨이터블

- [src/Python_Docs/Coroutine_Task/coroutine.py](https://github.com/yeoV/concurrency-python/blob/main/src/Python_Docs/Coroutine_Task/coroutine.py)
- 객체가 await 표현식에서 사용될 수 있을 때 -> Awaitable 객체라고 말함
- 어웨이터블 객체에는 3가지 유형이 존재
   1. 코루틴 (Coroutine)
  - 코루틴 함수 : async def 함수
  - 코루틴 객체 : 코루틴 함수를 호출하여 반한된 객체

   2. 태스크 (Task)
  - 코투틴을 동시에 예약하는데 사용됨
  - `asyncio.create_task()` 함수를 사용하여 실행되도록 자동으로 예약

   3. 퓨처 (Future)
  - 비동기 연산의 **최종 결과**를 나타내는 특별한 **저수준** 어웨이터블 객체
  - 객체를 기다릴 떄, 코루틴이 Future가 다른 곳에서 해결될 때 까지 기다릴 것을 뜻함
  - 일반적으로 Future 객체를 만들 필요 없음
    **- 콜백 기반 코드를 async/await 와 함께 사용할 경우 필요**

#### 1.3 Create Task

- 중요 : Save a reference to the result of `create_task()`, to avoid a task disappearing mid-execution.
  - Result 결과를 참조해야 가비지 컬렉터 에 의해 사라지지 않음.

``` python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task()
        task2 = tg.create_task()  # task 새로 생성
    print("Both tasks have completed now")
```

- `async with` 메소드는 그룹의 모든 task가 끝날 때 까지 기다림.

#### 1.4 Sleep

- delay
- result가 제공되면 코루틴이 완료될 때 호출자에게 반환

#### 1.5 동시에 태스트 실행

- [src/Python_Docs/Coroutine_Task/gather.py](https://github.com/yeoV/concurrency-python/blob/main/src/Python_Docs/Coroutine_Task/gather.py)
- `gather()` : Task 나 Future가 취소되어도 gather() 호출은 취소되지 않음
  -> 다른 Task / Future가 취소되게 하는 것을 막기 위함
- **가장 권고되는 방법 -> `asyncio.TaskGruop` 사용**

#### 1.6 대기 프리미티브

- `wait(aws, timeout=None, return_when=)` : Future 와 Task 인스턴스 실행
  - return_when 옵션
    - FIRST_COMPLETED : 하나라도 끝나거나 취소될 때 함수 반환
    - FIRST_EXCEPTION : 하나라도 예외 일으켜 끝나면 반환
    - ALL_COMPLETED : 모든 퓨처가 끝나거나 취소되면 반환
  - timeout 지정 시, 대기 시간 제어 가능

```python
done, pending = await asyncio.wait(aws)

```

#### 1.7 스레드에서 실행하기

- `to_thread()`
  - 메인스레드에서 실행될 경우, 이벤트 루프를 차단하는 IO 바운딩 함수를 실행하는데 사용
  - 별도의 스레드에서 func 함수를 비동기적으로 실행
  - func 최종 결과를 얻기 위해 await 할 수 있는 코루틴 반환
  - **이 함수는 IO-Bound function / method 에서 주요하게 활용**
    - 사유 : Python의 GIL로 인해서 IO-Bound 함수에서 사용해야 성능 효과 있음
      - 입력 대기시간이나 Sleep 의 경우, 해당 시간에 Context Switching 발생
      - GIL / 대체 python lib의 경우, CPU-Bound 작업에서도 활용 가능

## 2. 동기화 프리미티브

- Lock
- Event
- Condition
- Semaphore
- BoundedSemaphore
- Barrier

#### 2.1 Lock

- Mutex Lock 구현 / 스레드 안전 보장 불가
- 공유자원에 대한 독점 엑세스 보장 가능
- Lock을 사용하는 가장 좋은 방법 : `async with`
  - `acquire` `release` 와 동일

```python
lock = asyncio.Lock()
async with lock:
  # Access Shared State

########### Acquire / Release ##############
lock = asyncio.Lock()

await lock.acquire()
try:
  # access shared state
finally:
  lock.release()
```

#### 2.2 Event

- [src/Python_Docs/Synchronization_Primitives/event.py](https://github.com/yeoV/concurrency-python/blob/main/src/Python_Docs/Synchronization_Primitives/event.py)
- 이벤트 발생 시, asyncio 태스크에 알리는데 사용
- `set()` : Event set
- `clear()` : Event 지움 -> wait() 기다리는 태스크 set() 이 다시 호출될 때까지 Block

#### 2.3 Condition

- 태스크가 어떤 이벤트가 발생하기를 기다린 다음 공유 자원에 독점적 access 사용 가능
- Condition 객체 -> Event + Lock 기능 결합
- `async with` 문을 사용하는 것이 가장 좋은 방법
  
``` python
cond = asyncio.Condition()

# ... later
async with cond:
  await cond.wait()

########### Acquire / Release ##############
cond = asyncio.Condition()

await cond.acquire()
try:
  await cond.wait()
finally:
  cond.release()

```

- `notify` : 조건을 기다리는 n 개의 태스크를 깨움

#### 2.4 Semaphore

- 사용 가능한 공유자원의 수 N 개를 활용한 접근권한
- `acquire()` : 세마포어 갯수 감소
- `release()` : 세마포어 갯수 증가

#### 2.5 BoundedSemaphore

- 일반 semaphore 에서 초기 value 위로 내부 카운터를 증가시키면, release() 에서 ValueError 발생

#### 2.6 Barrier

- A barrier is a simple synchronization primitive that allows to block until parties number of tasks are waiting on it
- Task 들은 wait() 메소드가 특정 숫자의 wait() 만큼 waiting 함

## 3.큐 (Queue)

- [src/Python_Docs/Queue/queue.py](https://github.com/yeoV/concurrency-python/blob/main/src/Python_Docs/Queue/queue.py)
- asyncio 큐는 queue 모듈의 클래스와 유사
- `Queue`
  - `task_done()` : 이전에 큐에 넣은 작업이 완료되었음을 나타냄.
  - **`join()` : 큐의 모든 항목을 수신하여 처리할 때까지 블록.**
    - 완료되지 않은 작업 수는 항목이 큐에 추가될 때마다 증가.
    - 코루틴 항목이 `task_done()` 호출할 때마다 감소
    - 완료되지 않은 작업 수가 0으로 떨어지면 `join()` 블록해제
  - `get()`  vs `get_nowait()`
    - get() : 큐가 비어있으면 들어올 때 까지 대기
    - get_nowait() : 큐가 비어있을 경우 QueueEmpty Exception 발생
- `PriorityQueue` : 우선순위 큐
  - (priority_number, data) 형식의 튜플
- `LifoQuere` : 후입 선출 큐

#### + asyncio.TaskGroup

- [src/Python_Docs/Queue/quere_using_taskgroup.py](https://github.com/yeoV/concurrency-python/blob/main/src/Python_Docs/Queue/quere_using_taskgroup.py)
- Python 3.11 버전부터 추가
- 기존에는 `asyncio.gather()` 함수를 통해서 코루틴, 비동기 작업이 완료될 때까지 기다렸다가 리턴
  - 문제 : 전달한 작업이 실패할 경우??
      1. 모든 작업이 성공이든 실패든 결과 얻을 때까지 기다리기
      2. 어느 작업이 실패하면 진행 중인 다른 작업 중단 후 코드로 넘어가 실행
- `gather()` 함수는 1번의 방식을 취하는 것처럼 보이나, 어느 작업 실패 시 다른 작업들은 실행되게 놔두면서 자신은 실패 오류 발생후 리턴
  - 다른 작업들 반환 결과 받아올 수 없음.
  - Option -> `return_excepctions=True` 지정 시 실패 발생해도 모든 작업 끝나는걸 기다렸다가 결과 / 예외 반환
    - 코드상에서 일일이 검사해주어야함
    - 예시코드

    ``` python

    results = await asyncio.gather(mycoro..., return_exceptions=True)
    for result in results:
      if isinstance(result, Exception):
        ... # handle error
      else:
        ... # handle result
      ```

  - **TaskGroup** 은 2번째 접근 방식을 취함
  - 참고
    - <https://www.youtube.com/watch?v=8KyIK7srLds>
