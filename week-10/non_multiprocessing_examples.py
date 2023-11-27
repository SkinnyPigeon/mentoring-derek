import time


def worker(n):
    print(f"Worker {n} is starting")
    time.sleep(2)
    print(f"Worker {n} is done")


if __name__ == "__main__":
    for i in range(5):
        worker(i)
