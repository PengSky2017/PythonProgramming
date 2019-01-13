'''
1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。 dic = {"k1": "v1v1", "k2": [11,22,33,44]} PS:字典中的value只能是字符串或列表
'''


def func1(file_name, modify_str):
    with open(file_name, a) as f:
        f.write(modify_str)
    print('修改成功')


def func2(p_s):
    count_num = 0
    count_alpha = 0
    count_space = 0
    count_other = 0
    for s in p_s:
        if s.isdigit():
            count_num = count_num + 1
        elif s.isalpha():
            count_alpha = count_alpha + 1
        elif s == ' ':
            count_space = count_space + 1
        else:
            count_other = count_other + 1
    print('数字的个数：{}'.format(count_num))
    print('字母的个数：{}'.format(count_alpha))
    print('空格的个数：{}'.format(count_space))
    print('其他的个数：{}'.format(count_other))


def func3(obj):
    if len(obj) > 5:
        print('该{}对象长度大于5'.format(type(obj)))
    else:
        print('该{}对象长度小于5'.format(type(obj)))


def func4(ls):
    if len(ls) > 2:
        new_ls = ls[:2]
    else:
        new_ls = ls
    return new_ls


def func5(obj):
    newobj = []
    for i in range(len(obj)):
        if i % 2 != 0:
            newobj.append(obj[i])
    return newobj


def func6(dict):
    for key, value in dict.items():
        if len(value) > 2:
            dict[key] = value[:2]
    return dict










