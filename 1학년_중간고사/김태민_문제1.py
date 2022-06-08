#변수 설정 및 연산 출력
print("문제1: 인공지능융합부 202204200 김태민 ")

a = 2
b = 3

while a < b : #반목문 설정이 필요해서 그냥 a,b 값을 조건에 맞게 설정
    a = int(input("정수인 첫번째 수를 입력하시오")) #큰 수 입력
    b = int(input("정수인 두번째 수를 입력하시오")) #작은 수 입력
    if a > b:
        print(a + b, a * b, a/b, a % b, sep = '\n'   )
        break
    else:
        print("다시 입력 하시오")



