#윤년 판단

y = int(input("연도를 입력하시오"))

if ( (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 ):
    print(year, "년은 윤년입니다.")
else:
    print(y, "년은 윤년이 아닙니다.")