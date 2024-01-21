#  孙智祺04
import random
 
# b="1234567890"
# c=random.sample(b,5)
# a="".join(c)
# print(a)
# print(f"闽G-{a}")

import string
a=string.digits+string.ascii_uppercase

# for j in range(3):
e=[]
for i in range(20):
     b=random.sample(a,5)
     c="".join(b)
     f= f"闽G-{c}"
     e.append(f)
print(e)
d=input("请输入您喜欢的车牌号码：")
if d in e:
    print(f"恭喜您成功选择了您的车牌号，您的车牌号是：{d}")
        # exit("ssssss")
else:
    print("请重新输入您的车牌号")

