import csv
import random
import time

x_value = 0
total_1 = 1
total_2 = 1
timeout1 = time.time() + 25
timeout2 = timeout1 + 15


fieldnames = ["x_value", "total_1", "total_2"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        #total_1 = random.randrange(1100)
        #total_2 = random.randrange(800)
        total_1 = random.randrange(800)
        total_2 = random.randrange(500)
        if time.time() > timeout1:
            total_1 = random.randrange(100, 600)
            total_2 = random.randrange(500, 1200)
            if time.time() == timeout2:
                break

    time.sleep(1)
