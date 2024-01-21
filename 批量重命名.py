import os
a=os.listdir()
c=int(input("1添加，2输入"))
if c==1:
    for i in a:
        b="python_"+i
        os.rename(i,b)
        print(b)
elif c==2:
    for i in a:
        b=i[7:]
        os.rename(i,b)
        print(b)
else:
    print("重新输入")
