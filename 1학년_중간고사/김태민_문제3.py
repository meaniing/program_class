print("문제3: 인공지능융합부 202204200 김태민 ")

print("만약 구매를 안 한다면 '0'을 입력 해 주세요")
a = 2000 * int(input("사과 몇 개?(단, 정수로 입력)")) #사과
b = 3000 * int(input("배 몇 개?(단, 정수로 입력)")) #배
c = 2500 * int(input("참외 몇 개?(단, 정수로 입력)")) #참외
d = 8000 * int(input("딸기 몇 박스?(단, 정수로 입력)")) #딸기 한 박스
t = a + b + c + d
print("원가 가격:", t, "원")

if t < 10000: #만원 이하 일때
    coupon = input("쿠폰이 있나요? (있으면 1, 없으면 2)")
    if coupon == 1:
        t = t - 5000
        print("최종 금액", t, "원")
    else:
        print("최종 금액", t, "원")
elif  10000 <= t < 20000: #1만원 이상 2만원 미만 일때
    t = t - t * 3/20
    print("할인 적용 금액:", t, "원")
    coupon = int(input("쿠폰이 있나요? (있으면 1, 없으면 2)"))
    if coupon == 1:
        t = t - 5000
        print("최종 금액", t, "원")
    elif coupon == 2:
        print("최종 금액", t, "원")
    else: 
        print("다시 입력시오")
elif  20000 <= t < 30000: #2만원 이상 3만원 미만 일때
    t = t - t * 3/20
    print("할인 적용 금액:", t, "원")
    coupon = int(input("쿠폰이 있나요? (있으면 1, 없으면 2)"))
    if coupon == 1:
        t = t - 5000
        print("최종 금액", t, "원")
    elif coupon == 2:
        print("최종 금액", t, "원")
    else: 
        print("다시 입력시오")
elif  t >= 30000 : #3만원 이상 일때
    t = t - t * 1/5
    print("할인 적용 금액:", t, "원")
    coupon = int(input("쿠폰이 있나요? (있으면 1, 없으면 2)"))
    if coupon == 1:
        t = t - 5000
        print("최종 금액", t, "원")
    elif coupon == 2:
        print("최종 금액", t, "원")
    else: 
        print("다시 입력시오")
else:
    print("다시 입력하시오")
