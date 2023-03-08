        ###자료형 함수
print("hello world")
print(type("hello world"))  # str : string (문자열)
print(type(1+1))            # int : integer(정수)   
print(type(3.14159))        # float : 실수 (소수점이 있는 숫자)

    #연산자         
print(1 + 1)                # 덧셈
print(1 - 1)                # 뺄셈
print(1*1)                  # 곱셈
print(1/1)                  # 나눗셈 (나눗셈은 자료형 float 로 바뀜)
print(1//1)                 # 나눗셈 몫만 구하는 식
print(1%1)                  # 나눗셈 나머지만 구하는 식
print(2**2)                 # 제곱근


        ### 변수
a = 10                      # = : 대입연산자
print(a)   
                
    # 예제
    
name = "xxx"
age = 14
height = 158.5

print (name)
print(age)
print (height)


        ### 변수의 연산
age = age + 1
age += 1                     # 복합대입 연산자 (+=, -=, *=, /= ,//=, %= ,**=)
print(age)

#
print(age == 14)             # 비교연산자 (== 같다, != 다르다, > 크다, <작다, >= 크거나같다 ,<= 작거나같다)(T/F 로 대답해준다.)
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#논리연산자
print(a<b and a==10)         # T T = true
print(a<b and a==20)         # T F = false
print(a>b and a==20)         # F F = false

print(a<b or a==10)         # T T = true
print(a<b or a==20)         # T F = true
print(a>b or a==20)         # F F = false

print(not a==10)            # T = false
print(not a<b )             # F = true