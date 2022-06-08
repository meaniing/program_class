#축구게임

op = ["left", "middle", "right"]
c_c = random.choice(options)
u_c = input("어디를 수비 할건가요?")

if c_c == u_c:
    print("수비 성공")
else:
    print("페널티킥 성공")