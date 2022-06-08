#사용자가 입력하는 숫자의 합 계산하기

total = 0
answer = 'no'
while answer == "yes":
    number = int(input("숫자를 입력하시오:"))
    total = total + number
    answer = input("계속?(yes/no)")
print("합게는: ", total)