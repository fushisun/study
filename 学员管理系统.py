info=[]
def print_info():
    print("-"*20)
    print('1:添加学员')
    print('2:删除学员')
    print('3:修改学员信息')
    print('4:查询学员信息')
    print('5:显示所有学员信息')
    print('6:退出系统')
    print("-"*20)

def add_info():
    global info
    info_dict = {}
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    for i in info:
        if new_name == i['name']:
            print('该用户已经存在！')
            return

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    info.append(info_dict)
    print(info)

def del_info():
    global info
    del_name = input('请输入要删除的学员的姓名：')
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)

def search_info():
    global info
    search_name = input('请输入要查找的学员姓名：')
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：----------')
            print(f"该学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')

def print_all():
    print('学号\t姓名\t手机号')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

def modify_info():
    global info
    modify_name=input('请输入要修改的学员的姓名')
    for i in info:
        if modify_name==i['name']:
            i['id']=input('请输入新的学号：')
            i['tel']=input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

while True:
    print_info()
    user_num = input('请选择您需要的功能序号：')
    if user_num == '1':
        print('添加学员')
        add_info()
    elif user_num == '2':
        print('删除学员')
        del_info()
    elif user_num == '3':
        print('修改学员信息')
        modify_info()
    elif user_num == '4':
        print('查询学员信息')
        search_info()
    elif user_num == '5':
        print('显示所有学员信息')
        print_all()
    elif user_num == '6':
        print('退出系统')
        exit_flag = input('确定要退出吗? Y or N: ')
        if exit_flag == 'Y':
            break   
    else:
        print('输入错误，请重新输入!!!')

