#커피 가게 매출 계산하기 79.p

americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수:"))
cafelattes = int(input("카페라테 판매 개수:"))
capucinos = int(input("카푸치노 판매 개수"))

sales = americanos*americano_price
sales = sales + cafelatte_price*cafelattes
sales = sales + capucino_price*capucinos
print("총 매출은", sales, "입니다.")