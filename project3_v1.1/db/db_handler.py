# -*- coding: utf-8 -*-
import pickle
import os
from conf import setting


def select(identify):
    member_path = {
        'teacher': setting.teacher_db,
        'student': setting.student_db,
        'admin': setting.admin_db,
        'school': setting.school_db
    }
    if os.path.getsize(member_path[identify]) > 0:
        with open(member_path[identify], 'rb') as f:
            member_list = pickle.load(f)
        return list(member_list)  # 返回成员类的列表
    else:
        return None


def save(member_lst, status):  # 输入成员类的元组
    member_path = {
        'teacher': setting.teacher_db,
        'student': setting.student_db,
        'admin': setting.admin_db,
        'school': setting.school_db
    }
    with open(member_path[status], 'wb') as f:
        pickle.dump(member_lst, f)
