import functools
from interface import manager_interface, common
user_data = {
    'name': None,
    'identify': 'admin',
}


def run():
    while True:
        func_dic = {
            '1': login,
            '2': build_school,
            '3': build_course,
            '4': build_teacher,
            '5': logout,
            '6': register,
        }
        print('1. 登录\n2. 创建学校\n3. 创建课程\n4. 创建老师\n5. 退出')
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


# 创建学校
@login_auth
def build_school():
    school_name = input("请输入新建学校名字").strip()
    msg = manager_interface.create_school_interface(school_name)
    print(msg)


# 创建课程
@login_auth
def build_course():
    school_name = input("请输入创建课程的学校名").strip()
    teacher_name = input("请输入在哪个老师名下创建课程").strip()
    course_name = input("请输入创建的课程名字").strip()
    msg = manager_interface.create_course_interface(school_name, teacher_name, course_name)
    print(msg)


# 创建老师
@login_auth
def build_teacher():
    school_name = input("请输入创建讲师的学校名").strip()
    teacher_name = input("请输入创建的老师名字").strip()
    msg = manager_interface.create_teacher_interface(school_name, teacher_name)
    print(msg)


# 退出登录
@login_auth
def logout():
    user_data['name'] = None


# 管理员注册暗门（用户界面不予显示）
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
            flag, msg = common.admin_register_interface(name, password, user_data)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')

