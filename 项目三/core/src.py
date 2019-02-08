from interface import user, bank, shopping
from lib import common


user_data = {
    'name': None
}


def admin_login():
    print("管理员登录")
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flag, msg = user.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break


def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    count = 0
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':break
        password = input('请输入密码：').strip()
        flag, msg = user.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count == 3:
                user.lock_user_interface(name)
                print('尝试过多，锁定')
                break


def register():
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q': break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            flag, msg = user.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@common.login_auth
def choose_school():
    print('选择学校')


@common.login_auth
def choose_course():
    print('选择课程')


@common.login_auth
def check_sorce():
    print('查看分数')


@common.login_auth
def logout():
    exit()


def build_school():
    print('创建学校')


def build_course():
    print('创建课程')


def build_teacher():
    print('创建老师')
'''
学员视图：可以注册，登陆，选择学校，选择课程，查看分数，退出登录
讲师视图：可以登陆，选择课程，查看课程，查看学生，修改分数，退出登录
管理视图：可以注册，登陆，创建学校，创建课程，创建老师，退出登录'''


def run():
    menu = {
        '1':{
            '1': student_register,
            '2': student_login,
            '3': choose_school,
            '4': choose_course,
            '5': check_sorce,
            '6': logout,
        },
        '2':{
            '1': teacher_register,
            '2': teacher_login,
            '3': '',
            '4': '',
            '5': '',
            '6': logout,
        },
        '3': {
            '1': admin_login,
            '2': build_school,
            '3': build_course,
            '4': build_teacher,
            '5': logout,

        }

    }

    while True:
        menu1 = menu
        choice1 = input('1. 学员\n2. 讲师\n3. 管理员\n请选择>>').strip() # 选择第一层
        if choice1 not in menu1: # 输入内容不在menu1内，则继续输入
            continue
        while True:
            menu_2 = menu1[choice1] # 拿到choice1对应的一层字典
            for index, v in sorted(menu_2.items(), key=lambda item: item[0], reverse=False):
                print('{}:{}'.format(index, v.__name__))
            choice2 = input('请选择操作>>: ').strip()
            if choice2 in menu_2:
                menu_2[choice2]()
