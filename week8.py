# ###조건문 if
# num = int(input('수자입력 : '))

# if num > 10 :
#     print(f"{num}을 고르다니...안타깝네여")
# elif num < 10:
#     print(f"{num}을 고르다니...안타깝네여")
# else:#예외처리
#     print(f"{num}을 고르다니 현명하군ㅇ")


## 삼항연산자
#<조건식이 참일경우 결과> if <조건식> else <조건식이 거짓일경우 결과>
# mum = int(input('수자입력 : '))

# if mum % 2 == 0: 
#     print('짝짝수')
# else :
#     print('응-홀수ㅋ')
    
# print('짝짝수') if mum%2 == 0 else print('응-홀수ㅋ') 


##중첩 이프문
# n = int(input('수자입력 : '))
# if n >= 10:
#     print("큰 미스테잌크는 아니지만 비슷도리누")
#     if n%2 == 0: print('올 정답기기기긱ㄱ')
#     else : print('응 빠이')
# else:
#     print('넘 작으세연 ㅋ')
#     if n%2 == 0: print('올 정답기기기긱ㄱ 라고할뻔----')
#     else : print('응 빠')


# ##이프와 논리연산


# n = int(input('수자입력 : '))
# if n >= 10 and n%2 == 0 and n!= 0 :
#     print("큰 미스테잌크는 아니지만 비슷도리누")
# elif n >= 10 and n%2 != 0 and n!= 0:
#     print('올 정답기기기긱ㄱ')
# elif n < 10 and n%2 == 0 :
#     print("큰 미스테잌크 ")
# elif n < 10 and n%2 == 1:
#     print("헐......너무.....오답....헐....안타까움")
# else: print('응어쩔팁홓')


# ##if 와 멤버쉽 연산자 i n
# e = ['민정','태연','동건']
# st= input('학생이름 : ')

# if st in e :
#     print(f'{st}씨....ㅊㅋ리 포카리 있으십미당')
# else:
#     print(f'{st}씨....ㅊㅋ리 포카리 있으십미당... ㄺㅎㅃ ㅋㅋ')
    

#퀴즈노
# m = int(input('수자입력 : '))
# mm = int(input('수자입력 : '))
# if m >= m :
#     print(f'{m}...{mm}')
# elif m < mm :
#     print(f'{mm}...{m}')
# else: print('응어쩔팁홓')

##성적출력ㄱ
# s = int(input('수자입력 : '))
# if s >= 90 :
#     print(f'{s}점.... A!!')
# elif  89 > s >= 80 :
#     print(f'{s}점...B')
# elif  79 > s >= 70 :
#     print(f'{s}점...c!')
# else: print('응어쩔팁홓 F 누')


### Homework #######
##1. 두 개의 정수를 입력 받아 큰 수에서 작은 수를 뺀 차를 출력하는 프로그램을 작성하시오. 

##2. 정수를 입력 받아 0이면 "zero", 양수이면 "plus", 음수이면 "minus"라고 출력하는 프로그램을 작성하시오. 

##3. 비만도 측정(BMI) 프로그램
##(*주의사항: 키는 cm로 입력 받아서 m로 환산해야 합니다)
'''
비만도 측정(BMI지수)
BMI를 이용한 비만도 계산은 자신의 몸무게를 키의 제곱으로 나누는 것으로 공식은 kg/㎡.
BMI가 18.5 이하면 저체중 ／ 18.5 ~ 22.9 사이면 정상 
／ 23.0 ~ 24.9 사이면 과체중 ／ 25.0 이상부터는 비만으로 판정.
'''
# ##1
# a = int(input('수자입력 : '))
# aa = int(input('수자입력 : '))
# if a > aa :
#     print(a-aa)
# elif  aa > a :
#     print(aa-a)
# else: print('0')


# ##2
# p = int(input('수자입력 : '))
# if p > 0 :
#     print('plus')
# elif  0 > p :
#     print("minus")
# else: print('zero')

'''
비만도 측정(BMI지수)
BMI를 이용한 비만도 계산은 자신의 몸무게를 키의 제곱으로 나누는 것으로 공식은 kg/㎡.
BMI가 18.5 이하면 저체중 ／ 18.5 ~ 22.9 사이면 정상 
／ 23.0 ~ 24.9 사이면 과체중 ／ 25.0 이상부터는 비만으로 판정.
'''
##3
t = int(input('키 : '))
k = int(input('몸무ㄱ게 : '))
if t*0.01/k <= 18.5 :
    print('저체중')
elif  18.5 < t*0.01/k <= 22.9 :
    print("정상")
elif  23 <= t*0.01/k <= 24.9 :
    print("과체중")
elif  25 <= t*0.01/k  :
    print("비만")
else: print('구라까지마셈여')




