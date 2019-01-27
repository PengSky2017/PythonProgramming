class SlopOverError(BaseException):
    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self): # 用户界面打印
        if self.number == 1: # 如果传入的第一个参数为1打印越界提示
            return '<ErrorNum：%s ErrorMsg：%s ErrorType：越界>' % (self.number, self.message)
    __repr__ = __str__ # 调试界面打印


class Integer:
    @classmethod
    # classmethod 修饰符对应的函数不需要实例化，不需要self参数
    def get_num(cls):#第一个参数需要是cls参数，可以来调用类的属性，
        flag = 0
        try:
            input_num = input("please input a num:")
            if not input_num.isdigit():
                flag = 1
                print(ValueError('invalid literal for int() with base 10:{}'.format(input_num)))
                raise ValueError('invalid literal for int() with base 10:{}'.format(input_num))
            if int(input_num) < -2147483648 or int(input_num) > 2147483647:
                flag = 1
                print(SlopOverError(1,input_num))
                raise SlopOverError(1,input_num)
        finally:
            return int(input_num) if flag == 0 else cls.get_num() # 递归


if __name__ == '__main__':
    input_digit = Integer().get_num()

'''
测试结果
please input a num:88888888888888888888
<ErrorNum：1 ErrorMsg：88888888888888888888 ErrorType：越界>
please input a num:pengsky
invalid literal for int() with base 10:pengsky
'''
