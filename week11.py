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
1
m=input("text")
n= input("NUMber")
print(n+m)
2
s='과천코딩2022'
print(s[2],s[3],s[4],s[5])
33
f= input('fruit name ')
n=input ("how many? ")
print(f"어제 {f}를 {n}깨 먹었씁니다")
4
t = input(" 아무거나 써 숫자: ")
tt = input(" 아무거나 써 숫자: ")
print(f"{t}+{tt} = (t+tt),{t}-{tt} = (t-tt),{t}*{tt} = (t*tt),{t}/{tt} = (t/tt)")
5
mum = input(" 아무거나 써 숫자: ")
if mum % 2 == 0: 
    print('even')
else :
    print('odd')
6
p = input(" 아무거나 써 숫자: ")

for a in range(1, input_num+1 ):
    if input_num % a == 0:
        print(a,"(은)는 약수")
       
7
u = input(" 아무거나 써 숫자: ")
v=0
for i in range(2,a)
    if a/i==0:
        b =1
if b==1 or a==1 or a==0
    print('false')
else
    print("true")
8    
g = input(" 2-9 사이의 숫자를 써라 안그러ㅕㄴ 청개구리: ")
for i in range(1,10)
    print( g,'*' , i, '=' , g*i)
9
print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))
sum = 0
i = 1
while i <= n:
  sum = sum + i    
  i = i + 1        
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
10
n = int(input("Input number: "))
for i in range(1, n+1) :
	s = str(i)
	count = 0
	for x in s :
    	# 3, 6, 9 문자가 있으면
		if (x=='3') or (x=='6') or (x=='9') :
			count += 1
	if count == 0 :
		print(i, end=' ')
	else :
		# count 수만큼 X를 출력, 출력 글자 띄기로 구분
		print(count*'X', end=' ')
12
n = int(input("Input number: "))
for i in range(n): # 정방향
    print(' ' * ((n-1) - i) + '*' * (i * 2 + 1))
for i in range(n): # 역방향
    print(' ' * i + '*' * ((n*2-1) - (2 * i)))
    
        




