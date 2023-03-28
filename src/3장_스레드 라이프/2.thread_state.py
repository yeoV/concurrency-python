# 2. Thread의 상태 정리
import threading
import time


# 스레드 간단히 시작
def thread_worker():
    # Runnable State -> Run state
    print("My Thread has entered 'Runnung' state")
    # sleep() 호출 시, 비실행 상태로 진입
    time.sleep(10)
    # 스레드 작업 완료 후 종료
    print("My Thread is terminated")


# 이 시점에서 스레드는 아무런 상태 없음
# 자원 할당 받지 않은 상태
mythread = threading.Thread(target=thread_worker)

# thread.start() 실행 시, Runnable 상태로 변환
mythread.start()

# Join 되어 Dead 상태로 바뀜
# Garbage collector가 수집
mythread.join()
print("My Thread has entered 'Dead' State")
