# 孙智祺04
# def a(x,y,z,*arge):
#     print("----学生信息------")
#     print("姓名：",x)
#     print("年龄：",y)
#     print(arge)
#     if z>=60:
#         b="考试合格"
#     else:
#         b="考试不合格"
#     return b
# y=a(input(),int(input()),int(input()))
# print(y)


a=100
print(a)
def test1():
    global a
    a=200
    print(a)
def test2():
    print(a)
test1()
test2()
print(a)


# if __name__=="__main__":
#     a("sss",22,"python",123,223,45)30

