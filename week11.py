# ### Homework #######
# ##1. 2단부터 9단까지 구구단을 출력하는 프로그램을 작성하시오.


# ni=2
# while ni<10:
#     for i in range(1,10):
#         print(f'{ni}x{i}={ni*i}')
#     ni += 1
#     print()


# ##2. 몇 가지 과목의 점수를 입력받아서 평균을 구하여 출력하고 평균이 80점 이상이면 "pass", 
# ##   아니면 "fail"이라고 출력하는 프로그램을 작성하시오. (평균은 반올림하여 소수 첫째자리까지 출력)


# ss=[]
# while True:
#     p=int(input('점수는?'))
#     if p == 0: break
#     ss.append(p)

# total= sum(ss)/len(ss)
# if total >= 80: print('pass',total)
# else: print('fail', total)


# ##3. #18. 정수를 입력받아 다음과 같이 순서쌍을 출력하는 프로그램을 작성하시오.
# ## [입력] 4
# ## [출력]
# ## (1, 1) (1, 2) (1, 3) (1, 4)
# ## (2, 1) (2, 2) (2, 3) (2, 4)
# ## (3, 1) (3, 2) (3, 3) (3, 4)
# ## (4, 1) (4, 2) (4, 3) (4, 4)


# e =1
# nii= int(input('숫자입력:'))
# while e <= nii:
#     for g in range(1,nii+1):
#         tp = (e,g)
#         print(tp, end=" ")
#     e +=1
#     print()

# for e in range(1,nii+1):
#     for g in range(1,nii+1):
#         tp = (e,g)
#         print(tp, end=" ")
#     e +=1
#     print()



# ## 별 출력

# star= int(input('숫자입력'))

# for s in range ( 1 ,star+1):
#     print('*'*s)


# ## 역삼각형 출력 ( 별 )

# star= int(input('숫자입력'))

# for s in range (star , 0 , -1):
#     print('*'*s)

# 띄어쓰기 있는 삼각형

# star= int(input('숫자입력'))
# for i in range(1,star+1):
#     for s in range (star , 0 , -1):
#         print('_', end = ' ')
#     print('*'*i)

# ## 구구단 중첩포문

# for ni in range(2,10):
#     for i in range(1,10):
#         print(f'{ni}x{i}={ni*i}')
#     print()

# ## 1부터 입력한 숫자까지  출력
# num = int(input('숫자입력: '))
# for i in range(1,num +1):
#     print(i, end = ' ')

# ## 시작하는 수와 끝나는 수 입력받아서 두 수 사이의 숫자 입력

# o = int(input('시작숫자'))
# i= int(input('시작숫자'))

# for e in range(o, i+1):
#     print(e,end = ' ' )


# ### 두개의 숫자를 한번에 받기
# # 1 10
# m = input(' 2개 숫자 입려')
# m = m.split()
# m[0] = int(m[0])
# m[1] = int(m[1])
# print(m)
# #이게 아래걸로 바뀜
# n = [int(y) for y in m]
# print(m)

m=input("text")
n= input("NUMber")
print(n+m)

f= input('fruit name ')
n=input ("how many? ")
print(f"어제 {f}를 {n}깨 먹었씁니다")

t = input(" 아무거나 써 숫자: ")
tt = input(" 아무거나 써 숫자: ")
print(f"{t}+{tt} = (t+tt),{t}-{tt} = (t-tt),{t}*{tt} = (t*tt),{t}/{tt} = (t/tt)")






