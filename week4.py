#!1
# num = int(input(" 달 : "))
# mum = int(input(" 일 : "))
# print(f"오늘은 {num}월 {mum}일 입니다.")
#!2
# text1 = input(" 아무거나 써 : ")
# text2 = input(" 아무거나 써: ")
# print(f"{text1+text2}") 
#!3
# text = input(" 아무거나 써 문자: ")
# num = int(input(" 아무거나 써 문자: "))
# print(text*num)


###리스트
l = [1,2,3,4]

friends =["민정", "세현" , "태연" , "동건"]
print(friends)
print(l[0], friends[0])
print(l[1], friends[2])
print(l[2], friends[2])
print(l[3], friends[3])

## 리스트 값 수정
friends[1] = "대연"

##깁밥 만들기
item1 = " 김치 "
item2 = " 승기의 훈수 "
item3 = " 햄 "
item4 = " 백종원의 김밥 만들기 스킬  "
item5 = " 동건이의 손맛과 정성~~^^ "
print(item1+item2+item3+item4+item5)
#이거대신

items = ["김치","승기의 훈수","햄","백종원의 김밥 만들기 스킬","동건이의 손맛과 정성 ~~","동건이의 손맛과 정성 ~~"]
print(items)
print(len(items))

#리스트 추가
items.append("세현이의 드립력")# 맨 뒤에 리스트 추가
items.insert(3,"모두의 시선")# 원하는데 중간에 추가
print(items)

##리스트 삭제
items.pop() #멘 뒤에있는 리스트 삭제!
items.remove("햄")#특정 리스트 삭제!

### 정보
print(items.index("승기의 훈수"))
items.remove("동건이의 손맛과 정성 ~~") #똑같은 값이 있을시 지우거나 뭐 할 떄 더 앞에있는 게 적용됨
print(items.count("동건이의 손맛과 정성 ~~"))


score = [100,100,100 ,96,40 ]

print(max(score)) #리스트의 최댓값
print(min(score))#최솟값
print(sum(score))#모든수의 합
print(f"평균점수 : {sum(score)/5}")

##정렬
score.reverse() #역순으로 체인지(정렬)
score.sort()#오름차순으로 정리
score.sort(reverse=True)#내림차순



