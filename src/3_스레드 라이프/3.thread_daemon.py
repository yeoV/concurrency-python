# 종료점이 정의되지 않은 스레드 -> 스레드 데몬
# 예) 로드밸런서에 API 주소 알려주는 레지스트리 서비스 -> 지속적으로 인스턴스 상태 체크

import time
import threading


def standard_thread():
    print(f"Starting my standard Thread")
    time.sleep(20)
    print(f"Finishing my standard Thread")


def daemon_thread():
    while True:
        print("Heartbeat check")
        time.sleep(2)


if __name__ == "__main__":
    standard_thread = threading.Thread(target=standard_thread)
    daemon_tread = threading.Thread(target=daemon_thread)

    # setDaemon(True) 설정 시, 메인쓰레드 종료 시 즉시 종료되는 쓰레드
    # Option False 시, 종료되지 않고 계속 살아 있음.
    daemon_tread.setDaemon(True)
    daemon_tread.start()

    standard_thread.start()
