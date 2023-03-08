name= 'jake'
num= 1024

print(name,num)
#print(name + num)  - 서로 다른 자료형끼리 + 연산시 오류 뜸 

### 포멧팅 ( formating)
name = "jake"
grade = 1
clas = 10

###print ("1학년 10반 jake 입니다 tlqkf")
###print ("%d학년 %d반 %s 입니다 tlqkf"%(grade,clas,name))             #포멧기호
###print ("{}학년 {}반 {} 입니다 tlqkf".format(grade,clas,name))       #포멧함수
###print(f"{grade}학년 {clas}반 {name} 입니다 tlqkf")                  # f-string

"""
name = "Kant"
age = 132
height = 177.8

print("이름: %s, 나이:%d살, 키: %fcm"% (name,age,height))
print("이름: %s, 나이:%d살, 키: %.1f cm"% (name,age,height))
print("이름: {}, 나이:{}살, 키: {:.6f}cm ".format (name,age,height))
print("이름: {}, 나이:{}살, 키: {}cm ".format (name,age,height))
print(f"이름: {name}, 나이:{age}살, 키: {height :.6f}cm ")
print(f"이름: {name}, 나이:{age}살, 키: {height}cm ")

"""

#input():함수 : 입력
num =input("type your name : ")
print(f"welcome, {num}! nice to see you.")
nuum =input("type your age : ")
print(f"wow , you are {nuum}!")
nmm =input("type your adress : ")
print(f"thank you for giving us your adress. is it yours? {nmm}")

#문자열을 숫자로 변환아기 위해 int() 함수 사용 .
#input() 은 항상 숫자열을 달고 옵니다.
mum = int(input(" type your 1st number : "))
mmum = int(input(" type your 2st number : "))
print ("mum+mmum")
print ("mum-mmum")
print ("mum*mmum")
print ("mum/mmum")