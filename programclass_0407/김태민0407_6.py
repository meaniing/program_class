#동저 던지기 게임

import random

print("동전 던지기 게임을 시작합니다.")
c = random.randrange(2)
if c == 0:
    print("앞면")
else :
    print("뒷면")

print("게임 끝")