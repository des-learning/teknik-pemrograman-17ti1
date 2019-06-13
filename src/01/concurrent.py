import threading
import time

def counting(name, n):
    for i in range(n):
        print('thread {}: {}'.format(name, i))
        time.sleep(0.1)

def sayhello(name, n):
    for i in range(n, -1, -1):
        print('thread {}: hellooooo'.format(name))
        time.sleep(0.1)

N = 4
threads = []
for i in range(N):
    cmd = counting if i % 2 == 0 else sayhello
    thread = threading.Thread(target=cmd, args=(i, 10))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()
