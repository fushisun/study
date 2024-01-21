# a="------info of qsj----------"
# b="name  :  qsj"
# c="age :   18"
# d="hobby  :   eat"
# e="----------end----------"
# print(f'''{a}
# {b}
# {c}
# {d}
# {e} ''')


# salary=int(input("salary:"))
# if salary>100000:
#     print("公司是玩家")
# elif salary>50000:
#     print("996就像呼吸一样自然")
# elif salary>30000:
#     print("老板说什么都对")
# else :
#     print("打工人")
# a=0
# for f in range(101):
#     a+=f
# print(a)

# a=0
# for f in range(101):
#     if f%2==0:
#         a+=f
# print(a)

# for a in range(7):
#     for b in range(10):
#         print(f"{a}0{b}室")

# a=0
# b=0
# while a<101:
#     b+=a
#     a+=1
# print(b)

# for i in range(10):
#     if i<6:
#         for j in range(1,i+1):
#             print("*",end="")
#         print()
#     else:
#         for j in range(1,10-i+1):
#             print("*",end="")
#         print()

# a={}
# a['id'] = 2
# a['name'] = "sss"
# a['tel'] = 123
# print(a)

for i in range(1,10):
    print(' '*(9-i),end='')
    for k in range(1,i+1):
        print("*",end="")
        print(' ',end="")
    print('')


# import math
# for num in range(2,10000): #遍历从2~10000（不包含10000）之间的所有整数
#     result = 0
#     for factor in range(1,int(num/2)+1):
#         if num % factor == 0:  #判断当前整数是否可以被概数整除
#             result = result + factor
#     if result == num: #判断所有因子之和是否与该数本身相等
#         print(num)

# i=[1,2,3,4]
# print(i[1])