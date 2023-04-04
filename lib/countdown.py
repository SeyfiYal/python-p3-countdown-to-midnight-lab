# your code goes here!


def countdown(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
    print("HAPPY NEW YEAR!")
countdown(10)


import time

def countdown_with_sleep(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
countdown_with_sleep(10)
