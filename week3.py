### 문자열(string)
#문자열 연산
fruit1="watermelon"
fruit2="dragonfruit"
print(f"{fruit1} + {fruit2} = {fruit1+fruit2}") #글자의병합/ -  *  / 안됨
print(f"{fruit1} * {3} = {fruit1*3}") #반복


##인덱스
s1='ABCDEFGHIJKLNMOPQRSTUVWXYZ'
s2='abcdefghijklnmopqrstuvwxyz'

name = s1[13]+s2[8]+s2[12]
print(name)

#이스케이프 코드
print('mom said "did you do your homework?"')
print("\tmom said,\n \" get out \"\\")

##문자열 함수
hi= "hello,world"
print(hi.count('o')) #o 의 갯수 새줌
print(hi.lower())    #문자열 소문자로 변환
print(hi.upper())    #다 대문자로 바꿔줌
print(hi.replace('hello', 'bye')) #문자열 치환. hello -> bye

num = "010-2916-0075"
print(num.isalpha())   #문자 알파벳으로만 구성되어있는지 확인
print(num.isdigit())   #문자 알파벳으로만 구성되어있는지 확인
#중요
birth = "2010/12/16"
births = birth.split('/')
print(birth)
print(births)   # @@ 기준으로 나눠 리스트로 정리
print(len(birth)) # 몇글자인지 알려줌
b=births[0]
print(b)