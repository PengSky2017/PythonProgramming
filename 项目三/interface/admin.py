from db import admin_db_handle


# 管理员登录用户输入处理层
def login_interface(name, password):
    user_dic = admin_db_handle.select(name)
    if user_dic:
        if password == user_dic['password'] :
            return True, '登陆成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'


# 管理员创建学校用户输入层
def build_school_interface(local):
    school_dic = admin_db_handle.build_school(local)
    if school_dic:
        return False, '创建失败！学校已存在'
    else:
        school_dic = {
            'local': local,
            'class': [],
        }
        admin_db_handle.save_school(school_dic)
        return True, '创建成功'


def build_course_interface(course):
    course_dic = admin_db_handle.build_course(course)
    if course_dic:
        return False, '创建失败！课程已存在'
    else:
        course_dic = {
            'course': course,
        }
        admin_db_handle.save_course(course_dic)
        return True, '创建成功'


def build_teacher_interface(teacher_name):
    teacher_list = admin_db_handle.build_teacher()
    if teacher_list:
        if teacher_name in teacher_list:
            return False, '创建失败！教师已存在'
        else:
            teacher_list.append(teacher_name)
            admin_db_handle.save_teacher(teacher_list)
            return True, '创建成功'
    else:
        teacher_list = [teacher_name, ]
        admin_db_handle.save_teacher(teacher_list)
        return True, '创建成功'






