# ##
# num = int(input('숫자입력 '))
# f = 0

# for i in range (1,num+1):
#     if num%i == 0: f +=1
# if f >2 :print('t소수가 아님')
# else : print ('소수')
# print ()

# ### 함수
# ##함수의 종류
# #1.매개변수와 반환값이 모두 없는 경우
# def nothing():
#     print('업다ㅋ')

# nothing()

# #2.매개변수만 있는 경우
# def multable(num):
#     for i in range(1,10):
#         print(f"{num}*{i} = {num*i}")

# multable(3)

# ##3.반환값(리턴)만 있는 경우
# #예
# l = [1,2,3,4]
# print (len(l))

# def hello():
#     return "만나서 반강"

# print(hello())

# ##4.매가변수와 반환값 모두 있는 경우
# def multable(num):
#     for i in range(1,10):
#         print(f"{num}*{i} = {num*i}")
#     return print (f"{num}단 끝")

# multable(3)


# ##명함만들기
# cnt = 0
# def namecard(name,school,phone): #안에 숫자가 다르게 입력됨 == 안에*
#     print("______________________")
#     global cnt 
#     print("name :",name)
#     print("school :",school)
#     print("phone :",phone)
#     print("_______________________")
#     cnt += 1
#     return cnt 

# namecard("임민정","과천문원중학교","010-2916-0075")

# #2.명안만ㄷㄹ,ㄱ; 2
# cnt = 0
# def namecard(**arg): #안에 숫자가 다르게 입력됨 == 안에*
#     print("______________________")
#     global cnt 
# #    print(i ,':',arg{1})
#     print("_______________________")
#     cnt += 1
#     return cnt 

# nc = {"이름" :"임민정","학교":"문원중","연락처" :"010-2916-0075"}
# namecard(**nc)


## 넓이 구하는 함수
#삼각형
def t (b,h):
    a = b * h * 0.5
    return a

# bb = int(input("삼각형 base 입력"))
# hh = int(input("삼각형 height 입력"))
# print(t(bb,hh))

#사각형
def s (b,h):
    a = b * h 
    return a

# bb = int(input("사각형 base 입력"))
# hh = int(input("사각형 height 입력"))
# print(s(bb,hh))

#원
def c (b):
    a = b * b * 3.14
    return a

# bb = int(input("원 반지름 입력"))
# print(c(bb))

# 도형의 넓이를 구하는 프로그램 (삼각형 사각형 원 )
