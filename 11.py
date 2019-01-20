'''
要求: 从文件中取出每一条记录放入列表中, 列表的每个元素都是{'name':'albert','sex':'male','age':18,'salary':3000}的形式
2 根据1得到的列表,取出薪资最高的人的信息
3 根据1得到的列表,取出最年轻的人的信息
4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
5 根据1得到的列表,过滤掉名字以a开头的人的信息
6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值
'''

# part1
filename = '11.txt'
with open(filename) as f:
    items = [line[:-1].split() for line in f.readlines()]
    info = [{'name': name, 'sex': sex, 'age': age, 'salary': salary} \
        for name, sex, age, salary in items]
# print(info)

# part2
print(max(info, key=lambda dic: dic['salary']))

# part3
print(min(info, key=lambda dic: dic['age']))
's'.capitalize()
# part4
print(list(map(lambda items:{'name': items['name'].capitalize(),
                        'sex': items['sex'],
                        'age': items['age'],
                        'salary': items['salary']}, info)))
# part5
print(list(filter(lambda items: items['name'].startswith('a'), info)))

# part6


def fib(a,b,stop):
    if a > stop:
        return
    print(a,end=' ')
    fib(b,a+b,stop)


fib(0,1,10)
#7
l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]
def get(seq):
    for item in seq:
        if type(item) is list: get(item)
        else: print(item)
get(l)

