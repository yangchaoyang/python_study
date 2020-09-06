# def deco(leavl='debug'):
#     def use_log(func):
#         def wrapper(*args, **kwargs):
#             print(f'{func.__name__} [{leavl}] is running')
#             return func()
#         return wrapper
#     return use_log

# @deco('info')
# def bar():
#     print('i am bar')

# bar()

# class Foo():
#     def __init__(self,func):
#         self.__func = func
    
#     def __call__(self):
#         print('start')
#         self.__func()
#         print('end')

# @Foo
# def bar():
#     print('i am bar')

# bar()

class Student():
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        if score > 100 or score < 0:
            raise ValueError('error000')
        self.__score = score


stu = Student('ycy', 100)
print(stu.name)
stu.score = 101
print(stu.score)