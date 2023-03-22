import urllib.request
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
    for idx in range(10):
        execute_thread(idx)
    t1 = time.time()
    print(f"Total Execution Time {t1-t0}")
    

if __name__ == "__main__":
    main()
