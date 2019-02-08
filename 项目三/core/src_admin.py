from interface import admin
from db import admin_db_handle
import functools

user_data = {
    'name': None
}


# 管理员登录装饰器
def login_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            admin_login()
        else:
            return func(*args, **kwargs)
    return wrapper


def run():
    while True:
        func_dic = {
            '1': admin_login,
            '2': build_school,
            '3': build_course,
            '4': build_teacher,
            '5': logout,
        }
        print('1. 登录\n2. 创建学校\n3. 创建课程\n4. 创建老师\n5. 退出')
        choice = input('请选择>>').strip()
        if choice in func_dic:
            func_dic[choice]()


# 管理员登录用户输入层
def admin_login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':break
        password = input('请输入密码：').strip()
        flag, msg = admin.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)


@login_auth
def build_school():
    print('创建学校')
    print('1. 上海\n2. 北京')
    while True:
        local = input('请输入上海或北京>>').strip()
        if local in ('上海', '北京'):
            flag, msg = admin.build_school_interface(local)
            if flag:
                print('创建[%s]学校成功' % local)
            else:
                print(msg)
            break


@login_auth
def build_course():
    print('创建班级')
    print('1. 入门\n2. 进阶')
    while True:
        course = input('请输入入门或进阶').strip()
        if course in ('入门', '进阶'):
            flag, msg = admin.build_course_interface(course)
            print(msg)
            break


@login_auth
def build_teacher():
    print('创建老师')
    teacher_name = input('请输入老师姓名：')
    flag, msg = admin.build_teacher_interface(teacher_name)
    print(msg)


@login_auth
def logout():
    user_data['name'] = None

