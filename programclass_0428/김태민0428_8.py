#점치는 게임 

import random
import sys

while True:
    name = input("name:")
    if name == "":
        sys.exit()
    
    q = input("무엇에대해 알고 싶은가?")
    print(name + "님", "\"", q, "\"에 대해 질문 주셨군요" )
    print("운명의 주사위를 굴려 볼게요")

    a = random.randint(1, 8)

    if a == 1:
        print("네, 확실합니다")

    elif a == 2:
        print("전망이 좋은거 같군요")

    elif a == 3:
        print("믿으셔도 괜찮습니다.")

    elif a == 4:
        print("글쎼요")

    elif a == 5:
        print("한점의 의심도 없군요")

    elif a == 6:
        print("그럼요, 당신은 옳은 선택을 했습니다.")

    elif a == 7:
        print("제 답변은 no입니다.")

    else:
        print("나중에 다시 물어보세요")

    