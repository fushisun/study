# f=open("text.txt",'r+')
# a=f.readline()
# print(a)
# f.seek(6,0)
# f.seek(0,1)
# f.write("goodgoodstudy ")
# f.close()




# old_name=input('请输入您要备份的文件名：')
# index=old_name.rfind('.')
# a=old_name[0:index]
# b=old_name[index:]
# new_name=a+"[备份]"+b
# print(new_name)
# old_f=open(old_name,'rb')
# new_f=open(new_name,'wb')
# content=old_f.read()
# new_f.write(content)


import os
# os.rename('text.txt',"python_text.txt")
# os.remove("python_text.txt")
# os.mkdir('eee')
# os.rmdir("ddd")
# os.chdir('eee')
# a=os.getcwd()
a=os.listdir()
print(a)