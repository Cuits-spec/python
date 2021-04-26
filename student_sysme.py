# 学生信息管理系统


# 需求：进入系统，显示系统功能界面，功能如下：
# 1.增加学员信息
# 2.删除学员信息
# 3.修改学员信息
# 4.查询学员信息
# 5.显示所有学员信息
# 6.退出系统
# 系统共6个功能，用户根据自己需求选取

# 1.显示功能界面
# 定义函数print_info，负责显示系统功能


def print_info():
    print('-' * 20)
    print('欢迎使用学生管理系统:请选择功能')
    print('1.添加学员信息')
    print('2.删除学员信息')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 20)


print_info()

info = []


# 增加学员信息功能函数
def add_info():
    # 接收用户输入
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_tel = input('请输入手机号：')

    global info

    # 判断用户输入学员姓名是否已经存在，若存在，则报错
    for item in info:
        if new_name == item['name']:
            print("该学员已经存在")
            return
    else:
        # 如果不存在，添加
        info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}

        # 列表追加字典
        info.append(info_dict)
        print(info)


# 删除信息功能函数
def del_info():
    del_name = input('请输入要删除的学员姓名：')

    global info
    for item in info:
        if del_name == item['name']:
            info.remove(item)
            break
    else:
        print('该学员不存在')

    print(info)


# 修改学员信息功能函数
def modify_info():
    modify_name = input('请输入要修改的学员的姓名：')
    global info
    for item in info:
        if modify_name == item['name']:
            item['id'] = input('请输入新的学号：')
            item['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在，无法修改')

    print(info)


def search_info():
    search_name = input('请输入要查询的学员的姓名：')
    global info
    for item in info:
        if search_name == item['name']:
            print('查询到信息如下')
            print(f"学员学号：{item['id']},姓名：{item['name']},手机号：{item['tel']}")
            break
    else:
        print('查无此人')


# 显示所有学员信息
def print_all():
    print('姓名\t学号\t手机\t')
    for item in info:
        print(f"{item['id']}\t\t{item['name']}\t{item['tel']}")


# 2.用户输入功能序号
while True:
    print_info()
    user_num = input('请选择功能序号：')

    # 3.根据用户输入的功能序号，执行不同的功能（函数）
    if user_num == '1':
        add_info()
    elif user_num == '2':
        del_info()
    elif user_num == '3':
        modify_info()
    elif user_num == '4':
        search_info()
    elif user_num == '5':
        print_all()
    elif user_num == '6':
        print('退出系统')
        exit_flag = input('确定退出吗？yes or no?')
        if exit_flag == 'yes':
            break
    else:
        print('请重新输入（1-6）：')
