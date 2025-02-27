import math
import time

def func(num, ms):
    time.sleep(ms/1000)
    result = math.sqrt(num)
    print(f"Square root of {num} after {ms} milliseconds is {result}")

num = int(input())
ms = int(input())
func(num, ms)