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

#                                        I'm gunna pack my things and go to your mind
#                                     cause I know your not OK, but your saying " I'm OK "
#                                    I hope you think about yourself , and I will help it
#                                         cause you are a paitent and I am a doctor


# star= int(input('숫자입력'))

# for i in range(1,star+1):
#     for s in range (star , i , -1):
#         print(' ', end = '')
#     print('*'*(i*2-1))



# star= int(input('숫자입력'))

# for s in range (1,star+1):
#     print('*'*s)

# for i in range(star-1,0,-1):
#     print("*"*i)


# star= int(input('숫자입력'))

# for l in range(1,star*2):
#     if l <= star:
#         print('*'*l)
#     else:
#         print('*'*(star*2-l))

# n= int(input('숫자입력'))
# j=0
# for l in range(1,n+1):
#     for i in range(1,n+1):
#         print(l , end = ' ') 
#     print()
# #1
# m=input("text")
# n= int(input("NUMber"))
# print(m,end=' ')
# print(n)
# print(f'{n}{m}')
# #2
# s='과천코딩2022'
# print(s[2:6])
# print(s[-6:-2])
# #3
# f= input('fruit name ')
# n=input ("how many? ")
# print(f"어제 {f}를 {n}깨 먹었씁니다")
# #4
# t = int(input(" 아무거나 써 숫자: "))
# tt = int(input(" 아무거나 써 숫자: "))
# print(f"{t}+{tt} = {t+tt},{t}-{tt} = {t-tt},{t}*{tt} = {t*tt},{t}/{tt} = {t/tt:.2}")
# #5
# mum = int(input(" 아무거나 써 숫자: "))
# if mum % 2 == 0:print('even')
# elif mum%2 !=0:print('odd')
# else: print('dd')
# #6
# p = input(" 아무거나 써 숫자: ")

# for a in range(1,p+1):
#     if p % a == 0: print(a,"(은)는 약수")
#7
# u = int(input(" 아무거나 써 숫자: "))
# v=0
# for i in range(1,u+1):
#     if u%i==0:
#         v +=1
# if u==2:
#     print('t')
# else:
#     print("f")
# #8    
# g = input(" 2-9 사이의 숫자를 써라 안그러ㅕㄴ 청개구리: ")
# for i in range(1,10):
#     print( g,'*' , i, '=' , g*i)
# #9
# n = int(input('n값을 입력하세요.: '))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i    
#     i = i + 1        
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# for i in range(1,n+1):
#     sum += i
# print(sum)
# #10
# n = int(input("Input number: "))
# for i in range(1, n+1) :
# 	s = str(i)
# 	count = 0
# 	for x in s :
#     	# 3, 6, 9 문자가 있으면
# 		if (x=='3') or (x=='6') or (x=='9') :
# 			count += 1
# 	if count == 0 :
# 		print(i, end=' ')
# 	else :
# 		# count 수만큼 X를 출력, 출력 글자 띄기로 구분
# 		print(count*'X', end=' ')


# for i in range(1,n+1):
#     if i%10 == 3 or  i%10 == 6 or  i%10 == 9:
#         print('X', end=' ')
#     elif i//10 == 3 or  i//10 == 6 or  i//10 == 9:
#         print('X', end=' ')
#     else:
#         print(i,end=' ')
# #11
# for l in range(5):
#     for i in range(1,6):
#         print(i+l , end='')
#     print()
# # 4
# #12
n = int(input("Input number: "))
# for i in range(n): # 역방향
#     print(' ' * i + '*' * ((n*2-1) - (2 * i)))
# for s in range(2, n+1): # 정방향
#     print(' ' * ((n*2-n)-s) + '*' * (s * 2 -1 ))

for i in range(n*2-1):#전체 줄 수 아이 가 줄 수
    if i < n:
        print(' '*i + '*'*(2*(n-i)-1))#역삼각
    else:
        print(' '*((n*2-2)-i)+ '*'*((i-n+1)*2+1)) #정삼각
