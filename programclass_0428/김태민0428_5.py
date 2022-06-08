#초등생을 위한 산수 문제 발생기 

import random

while True:
    x = number = random.randint(1, 100)
    y = number = random.randint(1, 100)
    print(x, "+", y, end = "")
    answer = int(input())
    if answer == x + y:
        print("잘했어요")
    else:
        print("다음 기회에....")

