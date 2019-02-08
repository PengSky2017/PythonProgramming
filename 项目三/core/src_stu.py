from interface import stu
from db import stu_db_handle, admin_db_handle
import functools
user_data = {
    'name': None
}


# 学员登录装饰器
def login_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            student_login()
        else:
            return func(*args, **kwargs)
    return wrapper


def run():
    while True:
        func_dic = {
            '1': student_login,
            '2': student_register,
            '3': choose_school,
            '4': choose_course,
            '5': check_sorce,
            '6': logout,
        }
        print('1. 登录\n2. 注册\n3. 选择学校\n4. 选择课程\n5. 查看分数\n6. 退出')
        choice = input('请选择>>').strip()
        if choice in func_dic:
            func_dic[choice]()


def student_login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':break
        password = input('请输入密码：').strip()
        flag, msg = stu.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)


# 学员注册用户输入层
def student_register():
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
            flag, msg = stu.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@login_auth
def choose_school():
    print('选择学校')
    user_dic = stu_db_handle.select(user_data['name'])
    if user_dic['school']:
        print('您已选择%s学校！' % user_dic['school'])
        return
    print('1. 北京\n2. 上海')
    while True:
        school = input('请输入北京或者上海：').strip()
        if school in ('北京', '上海'):
            user_dic['school'] = school
            stu_db_handle.save(user_dic)
            print('选择%s成功' % school)
            break


@login_auth
def choose_course():
    print('选择课程')
    user_dic = stu_db_handle.select(user_data['name'])
    if user_dic['course']['name']:
        print('您已选择%s课程！' % user_dic['course']['name'])
        return
    if user_dic['school'] == '北京':
        while True:
            print('1. AI\n2. Python')
            course = input('请输入：').strip()
            if course in ('AI', 'Python'):
                user_dic['course']['name'] = course
                stu_db_handle.save(user_dic)
                print('选择%s课程成功！' % course)
                break
    else:
        while True:
            print('1. ML')
            course = input('请输入：').strip()
            if course in ('ML', ):
                user_dic['course']['name'] = course
                stu_db_handle.save(user_dic)
                print('选择%s课程成功！' % course)
                break


@login_auth
def check_sorce():
    print('查看分数')
    user_dic = stu_db_handle.select(user_data['name'])
    if user_dic['course']['sorce']:
        print('课程%s ： %s' % (user_dic['course']['name'], user_dic['course']['sorce']))
    else:
        print('课程%s暂时没有成绩' % user_dic['course']['name'])


@login_auth
def logout():
    user_data['name'] = None


