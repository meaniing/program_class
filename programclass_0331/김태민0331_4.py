#2050년에는 몇살? 

import time

now = time.time()
thisyear = int(1970 + now//(365*24*3600))

print("올해는", str(thisyear), "입니다")
age = int(input("몇살인가요?"))

print("2050년에는", str(age + 2050 - thisyear), "살 이시군요.")