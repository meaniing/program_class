print("문제5: 인공지능융합부 202204200 김태민 ")

import random

A = int(input("현재까지 누적된 A의 점수는?")) #누적된 게임의 점수
B = int(input("현재까지 누적된 B의 점수는?")) #누적된 게임의 점수

coin = random.randint(0, 1) # 0이 앞, 1이 뒤
dice = random.randint(1, 6)
print("주사위 결과:", dice)

if coin == 0:
    print("앞면 A 득점!! ") 
    A = A + dice
elif coin == 1:
    print("뒷면 B 득점!! ")
    B = B + dice
print("A의 점수는", A, "\nB의 점수는", B) #A, B 총점수

if A > B : #A가 이겼을때
    print("A님, 축하합니다. \n상금이 수여됩니다.")
elif A < B: #B가 이겼을때
    print("B님, 축하합니다. \n상금이 수여됩니다. ")