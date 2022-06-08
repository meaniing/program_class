plain_text = input("암호화할 문자를 입력하시오 : ")
encrypted_text = ""
 
for c in plain_text:
      x = ord(c)  #문자를 코드값으로 변환
      x = x + 1   #코드값을 1 증가
      cc = chr(x) #코드값을 문자로 변환
      encrypted_text = encrypted_text + cc           #암호문에 추가
 
print(encrypted_text)
 
encrypted_text = input("암호를 풀 문자를 입력하시오 : ")
 
plain_text = ""
 
for c in encrypted_text:
      x = ord(c)  #문자를 코드값으로 변환
      x = x - 1   #코드값을 1 감소
      cc = chr(x) #코드값을 문자로 변환
      plain_text = plain_text + cc #평문에 추가
 
print(plain_text)