from db import admin_db_handle
import functools
from conf import setting
import pickle
import os
user_data = {
    'name': None
}


def login_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            teacher_login()
        else:
            return func(*args, **kwargs)
    return wrapper


def run():
    while True:
        func_dic = {
            '2': teacher_login,
            '3': check_course,
            '4': check_stu,
            '5': modify_sorce,
            '6': logout,

        }
        print('1. 登录\n2. 查看课程\n3. 查看学生\n4. 修改分数\n5. 退出')
        choice = input('请选择>>').strip()
        if choice in func_dic:
            func_dic[choice]()


@login_auth
def check_course():
    rootdir = os.path.join(setting.BASE_DB, 'admin')
    filelist = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(filelist)):
        path = os.path.join(rootdir, filelist[i])
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                user_dic = pickle.load(f)
                if user_dic['course']['teacher'] == user_data['name']:
                    print(user_dic['course']['name'])
    else:
        print('您暂时没有课程！')


@login_auth
def modify_sorce():
    print('修改分数')
    name = input('请输入学生姓名：')
    sorce = input('请输入修改后的分数：')
    rootdir = os.path.join(setting.BASE_DB, 'admin')
    filelist = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(filelist)):
        path = os.path.join(rootdir, filelist[i])
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                user_dic = pickle.load(f)
                if user_dic['name'] == name:
                    user_dic['course']['sorce'] = sorce
    else:
        print('查无此人！')


@login_auth
def check_stu():
    rootdir = os.path.join(setting.BASE_DB, 'admin')
    filelist = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(filelist)):
        path = os.path.join(rootdir, filelist[i])
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                user_dic = pickle.load(f)
                if user_dic['course']['teacher'] == user_data['name']:
                    print(user_dic['name'])
    else:
        print('您暂时没有学生！')


def teacher_login():
    print('教授登录')
    teacher_list = admin_db_handle.build_teacher()
    while True:
        name = input('请输入教师姓名：')
        if name in teacher_list:
            user_data['name'] = name
        else:
            print('教师不存在')


def logout():
    user_data['name'] = None
