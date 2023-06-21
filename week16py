# ##모듈2 / 내장몯유루ㅡ
# ## 구글 파리선 표준 라이브러리에서 검색

# import math

# ##math.gcd(2,10)     # 2 와 10의 최대공
# print(math.gcd(11,98))

# ##math.lcm(2,10)     # 2 와 10의 최소공
# print(math.lcm(11,98))

# ##math.sqrt(2)       # 2가되는 제곱근값 출력
# print(math.sqrt(11))

# ##math.log(2,10)     # 밑이 10인 2의 로그값
# print(math.log(11,98))

# from math import *

# print(gcd(12,122))

# ###랜덤 모듈
# from random import *

# #print(randint(2,10)) # 2와 10 사이의 무작위 수 ㅎ하나 출력
# print(randint(1,31))

# #print(choice(ㅜ))  # 배열 자료형 ㅜ에서 하나의 값 랜덤으로 출력
# name= ['태연','민정','민수','준서','유림','채영','준호','민호']
# print(choice(name))

# #print(choice(ㅜ,10)) #ㅜ 에서 10개 출력
# print(choice(name,1))

# #print(shuffle(ㅜ)) # ㅜ 의 순서를 랜덤하게 섞
# print(shuffle(name))

# ## 주사위게임
# from random import *

# print('주사위게임! (엔터로 실행)')

# for i in range(3):
#     com = randint(1,6)
#     input()
#     user = randint(1,6)
#     if user > com : print('인간 승리')
#     elif user < com : print('기계 승리')
#     else : print('비김')

# ## time 모듈
# from time import*

# # time() : 유닉스 타임스템프를 소수로 반환
# print(time())

# # gmtime() : 지엠티 기준의 스트럭타임 데이터로 반환
# print(gmtime())

# #localtime() :  현지시간 스트럭타임 데이터 반환
# print(localtime())

# #ctime() : 현재시간 반환
# print(ctime())

# #sleep(sec) : 일정시간동안( 초 ) 프로그램 실행 지연
# sleep(10)
# print('응 어쩔')

# ## 타이머 만들기
# from time import*

# n = int(input('시간을 입력하세요 :'))
# sleep(n)
# for i in range (n,0,-1):
#     sleep(1)
#     if i <= 10:
#         print(i)
# print('어쩔')

# ## 업엔다운게임
# from random import *

# print('업엔 다운 게임 [로봇을 이기십시오]')
from random import *

p = 0
use = randint(1,100)
while True :
    n = int(input('예상 수를 입력하세요 :'))
    p += 1
    if n> use : 
        print('down')
    elif n < use : 
        print('up')
    else : 
        print('축하드립니다 맞추셨습니다!!!!!!!!')
        break
print(f"당신은 {p}번 만에 맞추셧습니다 ")


