import urllib.request
import threading
import time

IMG_URL = "IMG_URLS"

def download_image(image_path, file_name):
    print("Downloading Image form ", image_path)
    urllib.request.urlretrieve(image_path, file_name)
    print("Completed Download")

def execute_thread(idx):
    image_name = f"temp/image-{idx}.jpg"
    download_image(IMG_URL, image_name)

def main():
    t0 = time.time()
    # threads list
    threads = []
    for idx in range(10):
        thread = threading.Thread(target=execute_thread, args=(idx,))
        threads.append(thread)
        thread.start()

    # join() -> fork 된 child process가 정상적으로 끝났는지 확인
    for t in threads:
        t.join()

    t1 = time.time()
    print(f"Total Execution Time {t1-t0}")
    

if __name__ == "__main__":
    main()
