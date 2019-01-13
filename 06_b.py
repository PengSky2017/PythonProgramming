'''
author: PengSky
date: 2019-1-11
contain: 购物商城设计
'''


import os
print("欢迎来到商城！")
tag = True
flag = True
while tag:
    username = input('>>请输入用户名：')
    if os.path.getsize('black.txt') == 0:
        pass
    else:
        with open('black.txt', 'r') as f:
            namelist = f.readlines()
            for line in namelist:
                line = line.strip('\n')
                if username == line and flag:
                    print('您的账号异常，已被列入黑名单，再见！')
                    flag = False
                    tag = False
                    continue
                else:
                    pass
    while tag:
        pw = input('>>请输入密码：')
        with open('06_b.txt', 'r') as f:
            lines = f.readlines()
            infodic = {}
            infolist = []
            for line in lines:
                infolist = line.split('|')
                infodic[infolist[0]] = infolist[1][:-1]

        count = 0
        while count < 3:
            if infodic[username] == pw:
                break
            else:
                count = count +1
                print('密码错误，你还剩{}次机会'.format(3-count))
                if count != 3:
                    pw = input('>>请输入密码：')
                else:
                    with open('black.txt', 'a') as f:
                        f.write('\n' + username)
                    print('你已被列入黑名单，再见')
                    tag = False
                    continue

        while tag:
            menu = {
                '机器学习': '60',
                '普林斯顿微积分读本': '100',
                '统计学习方法': '50',

            }
            print('登录成功！')
            salary = int(input('>>请输入你的工资：'))
            for k, v in menu.items():
                print('{}: {}'.format(k, v))
            book = input('>>请输入要购买的书籍:')
            if int(menu[book]) < salary:
                salary = salary - int(menu[book])
                print('购买成功，您的余额为{}'.format(salary))

            tag = False
            continue


