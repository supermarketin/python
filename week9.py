
# ### 반복문 while

# ### 열번 찍어 안넘어가는 나무 없음
# count = 0

# while count < 10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다")

# print("나무가 넘어갑니다 휘리릴ㄹㄹ리리릴리릴ㄹㄹㄹㄹ리")


# ## 로그인 프로그램
# user={'ty83': '1234','mjspmk':'5678','jake':'2022'}

# cnt=3
# while cnt > 0:
#     id = input ("아이디 입력 :")
#     pw = input ("비밀번호 입력 :")
#     if id in user:
#         if pw == user[id]:
#             print('환영티비비비빕빕')
#             break
#         else:
#             print("다시 ㄱ")
#     else:
#         print("아이디 다시입력 고 아님 회원가입 해라 이")
#     cnt -= 1


# ##무한루프

# value= 0  # 트루 일 시 무한반복 (0,true)

# while value:
#     print('무한반복')
# print('종료')

# #무한반복
# user={'ty83': '1234','mjspmk':'5678','jake':'2022'}

# while cnt > 0:
#     id = input ("아이디 입력 :")
#     pw = input ("비밀번호 입력 :")
#     if id in user:
#         if pw == user[id]:
#             print('환영티비비비빕빕')
#             value=False
#         else:
#             print("다시 ㄱ")
#     else:
#         print("아이디 다시입력 고 아님 회원가입 해라 이")



# ###별찍기
# star =0

# while True:
#     star = star+1
#     if star > 5:
#         break
#     print('*'*star)

# ##practice
# # 정수를 입력받아 1부터 입력받은 정수까지 차례대로 출력하는 프로그램을 작성하세여
# n = int(print('숫자 입력:'))
# np= 0
# #1
# while np < n :
#     np += 1
#     print(np)
# #2
# while True:
#     np += 1
#     print(np)
#     if np == n:
#         break


# #2 정수를 입력받다가 0이 입력되면 그때동안 받은 짝수의 개수와 홀수의 개수를 출력하는 거 만들러

# e=0
# o= 0

# while True:
#     nn = int(input('숫자입력'))
#     print(nn)
#     if nn== 0:
#         break
#     elif nn%2 == 1:
#         o += 1
#     elif nn%2 == 0:
#         e += 1
#     else:
#         print("잘못입력티비")
# print(f" 지금까지 입력한 홀수.......{o}개.... 짝수......{e}개.....")

### Homework #######
##1. while 문을 이용하여 1부터 입력 받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.
##2. 점수를 입력받아 80점 이상이면 합격메시지를 그렇지 않으면 불합격 메시지를 출력하는 작업을 반복하다가 0~100점 이외의 점수가 입력되면 종료하는 프로그램을 작성하시오.
##3. 점수를 계속 입력을 받다가 0이 입력되면 0을 제외하고 이전에 입력된 자료의 수와 합계, 평균을 출력하는 프로그램을 작성하시오. (평균은 반올림하여 소수 둘째자리까지 출력한다.)
