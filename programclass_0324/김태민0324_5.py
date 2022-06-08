#자동 판매기 프로그램

M = int(input("투입한 돈:"))
P = int(input("물건 값:"))

C = M - P

print("거스름돈:", C)

C500s = C // 500
C = C % 500
C100s = C // 100

print("500원 동전의 개수:", C500s)
print("100원 동전의 개수:", C100s)