# a = {1,2,3,4,5,6}
# c="我的世界"
# b=dict(zip(c,a))
# print(sorted(a,reverse=True))
# print("c">"ba")
# try:
#     1/0
# except ZeroDivisionError:
#     print(21)


# import time
# time.sleep(3)

# import test.asd as asd
# asd.text(3,4)
# import test.abc as abc
# abc.text2()

#import json
#d=json.dumps(c,ensure_ascii=False)
#print(d)

# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts
# line=Line()
# line.add_xaxis(["中国","美国","英国"])
# line.add_yaxis("asd",[30,20,10])
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%")
# )
# line.render()

class ming:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __le__(self,a):
        return self.age <= a.age
    
    def ss(self):
        print("我是谁")


import random
a =ming("asd",18)
b =ming("sss",22)
print(a<=b)
a.ss()

c =random.randint(2,22)
print(c)


import tes
a("sss")