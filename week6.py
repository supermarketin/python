# ### range
n=range(10) # n 부터 n 까지(0부터)
n = list(n)
print(n)

n= list(range(1,11,2))
# # n 부터 n 까지 + n간격격

# ###  zip

l1 = [1,2,3]
l2 = [4,5,6]
# # 합치는 법

print(l1+l2)
print(list(zip(l1,l2))) # 짝을 이루어서 리스트로 묶어줌 ( 튜블저장) / 서로 자료형이 달라도 동일한 자료형이면 저장 됨'
print(tuple(zip(l1,l2)))

# ## 중첩 리스트 / 튜플
weapon = ['맨손','막대기','목검','도끼','검']
lv = ['1','2','3','4','5']
armor = ['-','장갑','전투화','방패','갑옷']

item = [lv,weapon,armor]
print(item)

my_item = [item[0][0],item[1][0],item[2][0]] # --쨰 인덱스에 --째 인덱스
print(my_item)

my_item = [item[0][1],item[1][1],item[2][1]]
print(my_item)

my_item = [item[0][2],item[1][2],item[2][2]]
print(my_item)


# ## numpy
# # pip install numpy 쳐서 다운로드

### 넘피 불러오기
import numpy
a = [1,2,3,4,5]
print(a, type (a))
b= numpy.array(a)  #numpy = np 똑같음
print(b, type (b)) #숫자를 가져올 떄 배열과 같음
print(b[2])

### 두 뱅열의 연소들의 연산
q1 = numpy.array([1,2,3])
q2 = numpy.array([4,5,6])

print(q1,q2)
print(numpy.add(q1,q2)) #각각의 인덱스 값을 더함
print(numpy.subtract(q1,q2)) #각각의 인덱스 값을 뺌
print(numpy.multiply(q1,q2)) #각각의 인덱스 값을 곱
print(numpy.divide(q1,q2)) #각각의 인덱스 값을 나눔

### 다차원배월 ( 2차)
import numpy as np

arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

print(arr)
print(arr[0][0])
print(arr[3][0])
print(arr.shape) # 배열의 크기를 알려줌 


## 원한는 크기의 배열을 만들기
#arr1 = range(100) # 0-99 가지 값 생성
arr1 = range(1,100+1) # 1-100 까지의 값 생성
# 1-100 까지 2 간격으로 생성(홀)
arr1 = range(1,100+1,2)
# 1-100 까지 2 간격으로 생성(짝)
arr2 = range(2,100+1,2) 
print(np.array(arr1))
print(np.array(arr2))

###다차원 배열로 만들기
arr3 = range(1,100+1)
arr3 = np.array(arr3)
print(arr3)
#reshape ; 재배열함수
print(arr3.reshape(10,10))

# 짝수 ( 1-100 ) 재배열하기
arr2 = range(2,100+1,2) 
arr2 = np.array(arr2)
print(arr2.reshape(5,10))
print(arr2.reshape(10,5))

##퀴즈
##120 까지의 3의 배수로 이루어진 배열을 (8,5)의 크기의 2차원 어레이로 만드세요
arr4 = range(3,120+1,3) 
arr4 = np.array(arr4)
print(arr4.reshape(8,5))
