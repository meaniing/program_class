#로봇기자 만들기
A = input("경기장은 어디입니까?")
B = input("이긴팀은 어디입니까?")
C = input("진팀은 어디입니까?")
D = input("우수선수는 누구입니까?")

while True:
    E, F = map(int, input('이긴팀의 스코어부터 입력하세요. (단 띄어쓰기로 스코어를 구분하시요)').split()) #반복문을 만든 이유는 스코어에 숫자 이외의 것들이 들어가면 안되기 때문
    if E > F :
        break
    else:
        print("스코어의 값이 이상합니다")

print("")
print("====================================================")
print("오늘", A, "에서 야구경기가 열렸습니다.")
print(B, "대", C, "의 치열한 공방전을 펼쳤습니다.")
print(D, "이 맹활약을 하였습니다!")
print("결국" ,A , "가" , B, "를", E, "대", F,"로 이겼습니다")
print("====================================================")