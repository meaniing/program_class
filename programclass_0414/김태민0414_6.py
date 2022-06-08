#팩토리얼 계산하기

n = int(input("정수를 입력하시오:"))

f = 1

for i in range(1, n + 1):
    f = f * i
print(n, f)
