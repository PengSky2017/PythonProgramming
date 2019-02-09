import logging.config
from db import db_handler


class Manager:  # 管理员类
    def __init__(self, name, password):
        self.name = name
        self.password = password


class School:  # 学校类
    def __init__(self, name, teachers=None):
        self.name = name
        if teachers is None:
            self.teachers = {}
        else:
            self.teachers = teachers


class Teacher:  # 讲师类
    def __init__(self, name, password, school=None, courses=None):
        self.name = name
        self.password = password
        self.school = school
        if courses is None:
            self.courses = {}
        else:
            self.courses = courses


class Course:  # 课程类
    def __init__(self, name, school, cycle, price, students=None):
        self.name = name
        self.school = school
        self.cycle = cycle
        self.price = price
        if students is None:
            self.students = {}
        else:
            self.students = students


class Student:  # 学员类
    def __init__(self, name, password, school, course, scores=None):
        self.name = name
        self.password = password
        self.school = school
        if scores is None:
            self.scores = {}
        else:
            self.scores = scores
        if course is None:
            self.course = {}
        else:
            self.course = course


# 字典形式代替多if分支的对象实例化
class_dict = {
    'teacher': Teacher,
    'student': Student,
    'admin': Manager
}


def login_interface(name, password, user_data):
    user_dic = db_handler.select(user_data['identify'])
    if user_dic:
        for i in user_dic:
            if i.name == name and i.password == password:
                return True, '登陆成功'
        return False, '用户密码错误或已经锁定'
    else:
        return False, '用户不存在'


def register_interface(name, password, school, course, user_data):
    user_dic = db_handler.select(user_data['identify'])
    new_user = class_dict[user_data['identify']](name, password, school, course)
    if user_dic:
        for i in user_dic:
            if i.name == name:
                return False, '用户已经存在'
        new_user_list = []
        for i in user_dic:
            new_user_list.append(i)
        new_user_list.append(new_user)
        db_handler.save(tuple(new_user_list), user_data['identify'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'
    else:
        db_handler.save((new_user, ), user_data['identify'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'


def admin_register_interface(name, password, user_data):
    user_dic = db_handler.select(user_data['identify'])
    new_user = class_dict[user_data['identify']](name, password)
    if user_dic:
        for i in user_dic:
            if i.name == name:
                return False, '用户已经存在'
        new_user_list = []
        for i in user_dic:
            new_user_list.append(i)
        new_user_list.append(new_user)
        db_handler.save(tuple(new_user_list), user_data['identify'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'
    else:
        db_handler.save((new_user, ), user_data['identify'])
        logging.info('%s 注册了' % name)
        return True, '注册成功'



