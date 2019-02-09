import functools
from interface import common
user_data = {
    'name': None,
    'identify': 'student',
}


# 登录函数装饰器
def login_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


def run():
    while True:
        func_dic = {
            '1': login,
            '2': register,
            '4': logout,
        }
        print('1. 登录\n2. 注册\n3. 退出')
        choice = input('请选择>>').strip()
        if choice in func_dic:
            func_dic[choice]()


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


# 注册函数
def register():
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            school = input('请输入关联学校')
            course = input('请输入关联课程')
            flag, msg = common.register_interface(name, password, school, course, user_data)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@login_auth
def logout():
    user_data['name'] = None


