'''
1.根据姓名查看学生所有成绩
2.查看所有人的某学科成绩
3.查看总平均分
4.查看某人的某学科成绩
5.根据姓名删除学生信息
'''


class Student:
    school = '深度之眼'

    def __init__(self, name, grade, math, chinese):
        self.name = name
        self.grade = grade
        self.math = math
        self.chinese = chinese

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_math(self):
        return self.math

    def get_chinese(self):
        return self.chinese

    def print_all_score(self):
        print('%s的数学成绩：%3d,语文成绩：%3d' % (self.name,
                                        self.math,
                                        self.chinese))

    def print_one_score(self, subject):
        if subject == 'math':
            print('%s的数学成绩：%3d' % (self.name,
                                   self.math))
        elif subject == 'chinese':
            print('%s的语文成绩：%3d' % (self.name,
                                   self.chinese))


stu1 = Student('pengsky', 1, 100, 90)
stu2 = Student('uv', 2, 90, 100)
stu = {stu1, stu2}
print(type(stu))

# 查看所有成绩
for astu in stu:
    astu.print_all_score()
print('--------------------------------------------------')

# 查看所有人的某学科成绩
for astu in stu:
    astu.print_one_score('math')
print('---------------------------------------------------')
# .查看总平均分
total = 0
num = 0
for astu in stu:
    total += astu.get_math()
    total += astu.get_chinese()
    num += 2
print('总平均分', total / num)
print('----------------------------------------------------')
# 4.查看某人的某学科成绩
name = '张三'
subject = 'math'
for astu in stu:
    if name == astu.get_name():
        astu.print_one_score(subject)

# 5.根据姓名删除学生
delect_stu = 'pengsky'
for astu in stu.copy():
    if delect_stu == astu.get_name():
        stu.remove(astu)
print(stu)