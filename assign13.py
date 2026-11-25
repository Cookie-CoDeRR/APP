import threading
import time


def print_numbers():
    for i in range(1, 6):
        print("Number thread:", i)
        time.sleep(1)


def print_squares():
    for i in range(1, 6):
        print("Square thread:", i * i)
        time.sleep(1)


def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter thread:", letter)
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_squares)
thread3 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All threads finished execution.")
