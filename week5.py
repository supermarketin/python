#1
# date =input(" type  : ")
# print(f"오늘은 {5}월 {-2:}일 입니다")
# #2
# date= date.split('/')
# print(f"오늘은 {date[1]}월 {date[2]}일 입니다")

# number=input(" type  : ")
# number= number.split('-')
# print(f"{number[0]}{number[1]}{number[2]}")

## 추가 in/join
#맴버쉽 연산자 in
even = [2,4,6,8]
print(2 in even)

# join
friends = ['태연','동건','세현','승기']
print(' '.join(friends))

#인덱스 슬라이싱
print(friends[::-1]) #간격조정 / -1 은 거꾸로

friends.reverse()
print(friends)

### 튜플
tu= 1,2,3,4,5
print(tu,type(tu))

print(tu[2])


# list tuple 비교
l1=[1,2,3]
l2=l1[:] # l1 은 l1 이고 l2 는 l2 로 복사된 
print(l1==l2)#값이 같은지
print(l1 is l2)#대상(객체)가 같은지

t1=(1,2,3)
t2=t1[:] # t1 은 t1 이고 t2 는 t2 로 복사된 것이 아닌
print(t1==t2)#값이 같은지
print(t1 is t2)

##추가함수
## .endswith() / .startwith()
## lstrip() / rstrip() / strip()

f_name= "study.txt"
print(f_name.endwith('txt')) # --로 끝나면 ==해라

f_nmae2 = "2023_note"
print(f_nmae2.startswith('2023')) # ==로 시작하면 ///헤라

data="   삼성주식   "
print(data.lstrip()) #왼쪽 공백 사라짐
print(data.rstrip()) #오른쪽 공백 사라짐
print(data.strip()) #앞뒤 공백 사라짐