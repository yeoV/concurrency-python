from threading import Semaphore, BoundedSemaphore

# 일반적으로 세마포어를 갯수 지정하여 생성
# 초기 세마포어 값 5:
s1 = Semaphore(5)

# 세마포어 1개 획득
# 현재 세마포어 값 : 4
s1.acquire()

# 세마포어 release 하여 4개에서 5개로 증가
s1.release()

# acquire 과정 없이 release 진행
s1.release()

# 세마포어의 값이 6으로 증가함.. 이상적이지 않음
print(s1._value)  # => 6


s2 = BoundedSemaphore(5)  # Start at 5.

s2.acquire()  # Lower to 4.

s2.release()  # Go back to 5.

try:
    s2.release()  # 선언한 초기값을 넘을 경우 ValueError 발생
except ValueError:
    print("As expected, it complained.")
