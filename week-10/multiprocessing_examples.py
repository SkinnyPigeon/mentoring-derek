import multiprocessing
import time


def worker(n, data):
    print(f"Worker {n} is starting")
    time.sleep(2)
    print(data)
    print(f"Worker {n} is done")


base_data =  {
    0: [12,23, 5],
    1: [12,23, 2],
    2: [12,23, 534],
    3: [12,23, 442343],
    4: [12,23, 5],
}

if __name__ == "__main__":
    for i in range(5):
        multiprocessing.Process(target=worker, args=(i,base_data[i])).start()
