import os
from conf import setting
import pickle


# 管理员登录数据库层
def select(name):
    admin_path = os.path.join(setting.BASE_DB, 'admin')
    user_path = os.path.join(admin_path, '{}.pkl'.format(name))
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            user_dic = pickle.load(f)
            return user_dic
    else:
        return None


def build_school(local):
    school_path = os.path.join(setting.BASE_DB, '%s.pkl' % local)
    if os.path.exists(school_path):
        with open(school_path, 'rb') as f:
            user_dic = pickle.load(f)
            return user_dic
    else:
        return None


def save_school(school_dic):
    school_path = os.path.join(setting.BASE_DB, '%s.pkl' % school_dic['local'])
    with open(school_path, 'wb', ) as f:
        pickle.dump(school_dic, f)
        f.flush()


def build_course(course):
    course_path = os.path.join(setting.BASE_DB, '%s.pkl' % course)
    if os.path.exists(course_path):
        with open(course_path, 'rb') as f:
            course_dic = pickle.load(f)
            return course_dic
    else:
        return None


def save_course(course_dic):
    course_path = os.path.join(setting.BASE_DB, '%s.pkl' % course_dic['course'])
    with open(course_path, 'wb', ) as f:
        pickle.dump(course_dic, f)
        f.flush()


def build_teacher():
    teacher_path = os.path.join(setting.BASE_DB, 'teacher.pkl')
    if os.path.exists(teacher_path):
        with open(teacher_path, 'rb') as f:
            teacher_list = pickle.load(f)
            return teacher_list
    else:
        return None


def save_teacher(teacher_list):
    teacher_path = os.path.join(setting.BASE_DB, 'teacher.pkl')
    with open(teacher_path, 'wb', ) as f:
        pickle.dump(teacher_list, f)
        f.flush()


