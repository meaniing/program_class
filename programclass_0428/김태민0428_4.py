#숫자 맞추기 게임

import random

t = 0
g = 0;
answer = random.randint(1, 100)

print("1 부터 100 사이의 숫자를 맞치시오 ")

while g != a:
    g = int(input("숫자를 입력하시오"))
    t = t + 1
    if g < answer:
        print("낮음")
    if g > answer:
        print("높음")

if g == answer:
    print("축하드립니다.")
else:
    print("정답은 ", answer)