
from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    print(f"Task {n} start")
    time.sleep(2)
    return f"Task {n} Done"

with ThreadPoolExecutor(max_workers=3) as ex:
    futures = [ex.submit(task,i) for i in range(1,6)]
    for f in futures:
        print(f.result())



