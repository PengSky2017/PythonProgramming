from db import stu_db_handle


# 学员登录用户输入处理层
def login_interface(name, password):
    user_dic = stu_db_handle.select(name)
    if user_dic:
        if password == user_dic['password'] :
            return True, '登陆成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'


# 学员注册用户输入处理层
def register_interface(name, password):
    user_dic = stu_db_handle.select(name)
    if user_dic:
        return False, '用户已经存在'
    else:
        user_dic = {'name': name,
                    'password': password,
                    'school': None,
                    'course': {
                        'name': None,
                        'sorce': None,
                        'teacher': None
                    },
                   }
        stu_db_handle.save(user_dic)
        # user_logger.info('%s 注册了' % name)
        return True, '注册成功'



