#오늘의 속담

import random

quotes = []
quotes.append("꿈을 지녀라 그러면 어려운 현실을 이길수 있다")
quotes.append("분노는 바보들의 가슴속에서만 살아간다.")
quotes.append("고생업이 얻을수 있는 진실로 귀중한 것은 하나도 없다")
quotes.append("사람은 사랑할때 누구나 시인이 된다.")
quotes.append("시작이 반이다")

dailyQuote = random.choice (quotes)
print("######################")
print("# 오늘의 속담 #")
print("######################")
print("")
print(dailyQuote)