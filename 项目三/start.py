import sys ,os
from core import src_admin, src_stu, src_teach
path = os.path.dirname(__file__)
sys.path.append(path)
if __name__ == '__main__':
    while True:
        func_dic = {
            '1': src_admin.run,
            '2': src_stu.run,
            '3': src_teach.run,
        }
        choice = input('1. 管理员\n2. 学员\n3. 教师\n请选择>>').strip()  # 选择第一层
        if choice in func_dic:  # 输入内容不在menu1内，则继续输入
            func_dic[choice]()


