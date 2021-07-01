import time
import random

timeout1 = time.time() + 15
timeout2 = timeout1 + 15

while True:
    test = 0
    total_1 = random.randrange(100)
    total_2 = random.randrange(200)
    if time.time() > timeout1:
        total_1 = random.randrange(300, 1000)
        total_2 = random.randrange(100, 800)
        if time.time() == timeout2:
            break
    test = test - 1
    print(test)
    print(total_1, total_2)
    time.sleep(1)
