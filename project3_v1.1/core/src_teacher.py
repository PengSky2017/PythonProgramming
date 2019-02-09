import functools
from interface import teacher_interface, common
user_data = {
    'name': None,
    'identify': 'teacher',
}


def run():
    while True:
        func_dic = {
            '1': login,
            '2': check_course,
            '3': logout,

        }
        print('1. 登录\n2. 查看课程\n3. 退出')
        choice = input('请选择>>').strip()
        if choice in func_dic:
            func_dic[choice]()


# 登录函数装饰器
def login_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


# 登录函数
def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flag, msg = common.login_interface(name, password, user_data)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)


@login_auth
def logout():
    user_data['name'] = None


@login_auth
def check_course():  # 查看课程后可查看课程对应的学生以及录入、修改他们的分数
    course = input("请输入您要查询的课程").strip()
    teacher_interface.operate_course(course, user_data)