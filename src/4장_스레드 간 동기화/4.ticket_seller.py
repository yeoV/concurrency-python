"""
# ticket_available => 사용 티켓 수
# Ticket Seller 쓰레드를 만들듬
"""
import random
import threading
import time


class TicketSeller(threading.Thread):
    semaphore: threading.Semaphore
    ticket_sold: int = 0

    def __init__(self, semaphore) -> None:
        threading.Thread.__init__(self)
        self.semaphore = semaphore

    def run(self):
        global tickets_available
        print("Ticket seller started work")
        while True:
            time.sleep(random.randint(0, 1))
            # acquire 불가능할 경우
            if tickets_available <= 0:
                break
            self.semaphore.acquire()
            self.ticket_sold += 1
            tickets_available -= 1
            print(f"{self.name} Sold one ({tickets_available} left)")
            self.semaphore.release()

        print(f"{self.name} Ticket Seller Sold {self.ticket_sold} in Total")


# 세마포어 primitive
semaphore = threading.BoundedSemaphore(4)

# 티켓 배당
tickets_available = 10

# 배열 생성
sellers = []
for idx in range(4):
    seller = TicketSeller(semaphore)
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()
