# ### 딕셔너리 dictionary
# ##딕셔너리 생성
dic={'이름':'홍길동', '나이': 12, '학교':'동화학교교'}
print(dic,type(dic))

print(dic['이름'])

# # ##추가
dic['담임'] = '안드레스'
print(dic,type(dic))

# # ##수정
dic['나이'] = 16
print(dic,type(dic))

# ###삭제
del dic['담임']
print(dic,type(dic))

# ### 실습
# ##과일가계
di={'사과': 500 , '바나나': 2500,'망고':2000 }
print(di)
print(f"망고는 1개당 {di['망고']}원 입니다.")   
di['사과'] = 700
di['용과'] = 33000
del di['바나나']
print(di)


# ### 딕셔너리 함수
fruit = {'사과': 500, '바나나': 2000, '망고' : 2500}

print(fruit.keys(), type(fruit.keys())) # 리스트도 아니고 튜플도 아님 / 딕셔너리 키 묶어서 반환

keys= list(fruit.keys())                #딕셔너리 키 묶어서 반환
print(keys[0])

values = list(fruit.keys())             # 값들을 묶어서 반환
print(values)

temp = dict(zip(keys,values))

tems = list(fruit.keys())             # 키와 벨류 를 쌍으로 묶어서 반환

#print(fruit.get['오렌지'])             # 있는지 없는지 확인 가능 //없음 none

fruit.update({'오렌지': 1200 , '용과': 33000 , '사과': 700}) 
print(fruit)                          #딕셔너리에 한번에 많은 것 을 추가/삭제 ... 할 때

fruit.clear()                         # 딕셔너리 비움
print(fruit)


### 그래프 그리기
## pip install matplotlib
#matplotlibrary
import matplotlib.pyplot as plt

#### korean debug
### win
from matplotlib import font_manager,rc
font_path = 'C:/Windows/Fonts/NGULIM.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#mac
# from matplotlib import rc
# rc('font', family='AppleGothic')

##y= 2x 그래프
x = [1,2,3,4,5]
y=  [2,4,6,8,10]

plt.plot(x,y)
plt.show()

###성적관리



std = ['민정', '태연', '세현']

sub = ['국어','영어','수학', '역사']
st1 = [100, 95, 100, 85]
st2 = [80,90,70,100]
st3 = [90,100,100,70]

score = [
    dict(zip(sub,st1)),
    dict(zip(sub,st2)),
    dict(zip(sub,st3))
]

grade = dict(zip(std,score))
print (grade)
print(score)

# plt.plot(sub , st1)        # 1개만 출력
# plt.show()

plt.plot(grade['민정'].keys(), grade['민정'].values(),'r-')
plt.plot(grade['태연'].keys(), grade['태연'].values(),'g-')
plt.plot(grade['세현'].keys(), grade['세현'].values(), 'bo') #도트
plt.ylim(0,100)
plt.show()