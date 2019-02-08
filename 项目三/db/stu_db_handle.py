import os
from conf import setting
import pickle


# 学员登录数据库层
def select(name):
    stu_path = os.path.join(setting.BASE_DB, 'stu')
    user_path = os.path.join(stu_path, '{}.pkl'.format(name))
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            user_dic = pickle.load(f)
            return user_dic
    else:
        return None


# 学员注册数据库层
def save(user_dic):
    stu_path = os.path.join(setting.BASE_DB, 'stu')
    user_path = os.path.join(stu_path, '%s.pkl' % user_dic['name'])
    with open(user_path, 'wb', ) as f:
        pickle.dump(user_dic, f)
        f.flush()