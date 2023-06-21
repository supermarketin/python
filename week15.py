# def f(d):
#     if d == '인사':
#         print('안녕하세요')
#     elif d == '도둑':
#         print('손들어, 꼼짝마!')
#     elif d == '친구':
#         print('환영합니다')
#     else:
#         print('메롱이다')

# f('인사')
# f('도둑')
# f('친구')

# class c:
#     total = 0
#     def add(self,n):
#         self.total = 0
#         return print(self.total)

# math = c()
# math.add(10)
# math.add(3)

# class lol:
#     def __init__ (self):
#         print("소환사가 게임에 접속하였습니다.")

# class sltch(lol):
#     supper().__init__ (self)
#     def __init__ (self):
#         print('개릭터 선택')

# class cal:
#     def __init__ (self):
#         self.total==0
#         print('i am the cal')
#     total = 0
#     def add(self,n):
#         self.total += n
#         return print(self.total)
#     def sub(self,n):
#         self.total -= n
#         return print(self.total)
#     def mul(self,n):
#         self.total *= n
#         return print(self.total)
#     def div(self,n):
#         self.total /= n
#         return print(self.total)

# math = cal()
# math.add(10)
# math.sub(5)
# math.mul(9)
# math.div(9)

# #class 상속
# class cal_divup(cal):
#     def __init__ (self):
#         super().__init__(self)
#         print('i am upgrade')
#     def div (self,n):
#         if n == 0: print("x")
#         else:
#             self.total /= n
#             return print(self.total)
        
# math = cal_divup()
# math.add(10)
# math.sub(5)
# math.mul(7)
# math.div(0)

#모듀ㅠㅠㅠㅠㅠㄹ moduuuuuuuuuuuuuuuuuuuuuuule
#게임플레이

# import move

# p1 = move.up()
# p1 = move.down()

#from move import *
# import move,attack



# move.up()
# move.down()

# p1 = attack.AT()
# p1.punch

from move import *
from attack import *

up()
down()

p1 =AT()
p1.punch
