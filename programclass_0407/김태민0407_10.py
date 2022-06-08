#로그인프로그램 

id = "rlaxoals1397"
pw = "rlaxoals22"

s = input("아이디를 입력하시오")
p = input("비밀번호를 입력하시오")
if s == id:
    print("비밀번호를 입력하시오")
    if pw == p:
        print("로그인 완료")
    else:
        print("로그인 실패")
else:
    print("로그인 실패")
