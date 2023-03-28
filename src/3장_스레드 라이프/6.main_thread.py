# 모든 파이썬 프로그래밍에서는 1개의 Main Thread가 동작함
import threading


def my_child_thread():
    print("Child Thread starting")
    print("Current Child Thread -------------------")
    print(f"Child Thread : {threading.current_thread()}")
    print("Current Main Thread -------------------")
    print(f"Main Thread : {threading.main_thread()}")
    print("----------------------------------------")
    print("Child Thread is finished")


child = threading.Thread(target=my_child_thread)
child.start()
child.join()
