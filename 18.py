class CarMeta(type):

    def __init__(self, class_name, class_bases, class_dic):

        super(CarMeta, self).__init__(class_name, class_bases, class_dic)



    def __call__(self, *args, **kwargs):  

        '''
        为什么在CarMeta元类中写__call__方法
        调用Car类的时候由于Car类没有__call__方法，因此调用CarMeta中的__call__方法
        如果不在此处写__call__方法将会调用type中的方法
        此时将失去定制元类的意义
        调用顺序：Car --> CarMeta --> type
        
        '''
        
        obj = object.__new__(self)  # 创建一个空对象

        self.__init__(obj, *args, **kwargs)  # 初始化CarMeta

        if ('production_date' and 'engine_number' and 'capacity') not in dir(obj):  # 判断Foo类中是否有production_date参数，下同

            raise TypeError('类中属性缺失')

        return obj


class Car(metaclass=CarMeta):

    def __init__(self, name, production_date, engine_num, capacity):

        self.name = name

        self.production_date = production_date

        self.engine_num = engine_num
        
        self.capacity = capacity

'''
class Car(metaclass=CarMeta):

    def __init__(self, name, production_date, engine_num, ):

        self.name = name

        self.production_date = production_date

        self.engine_num = engine_num
        
如果创建类是初始化缺少属性，将会raise error
        
		raise TypeError('类中属性缺失')

'''


car = Car("现代", "2019", 'x001', 10)


# --------------------------------------------------------------
# 单例模式

# 模块
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象

# 装饰器
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)

# 类
class Singleton(object):

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

		
# 元类
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1,obj2)