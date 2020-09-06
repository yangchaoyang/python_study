# class Poweroftwo():
#     def __init__(self):
#         self.exponent = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.exponent > 10:
#             raise StopIteration
#         else:
#             result = 2 ** self.exponent
#             self.exponent += 1
#             return result

# print(Poweroftwo)
# print(Poweroftwo())

# def power_of_two():
#     for item in range(5):
#         yield 2 ** item

# # print(power_of_two)
# # print(power_of_two())
# p = power_of_two()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

# item = (i.upper()*2 for i in 'def')
# print(item)
# print(next(item))
# print(next(item))
# print(next(item))
# print(next(item))

# nums = [2 ** i for i in range(1, 11)]
# print(nums)

# chars = [(i.upper(), i) for i in ['a', 'b', 'c', 'd', 'e']]
# print(chars)

# print([2 ** i for i in range(1, 11) if i % 2 == 1])
# print([c * n for n in [1, 2, 3] for c in ['a', 'b', 'c']])
# print([char.upper() for string in ['aa', 'bb', 'cc'] for char in string])
# print({char.lower() for char in 'ABCDABCD'})

# import random

# class Char():
#     __letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     __digits = '0123456789'

#     @classmethod
#     def random_letters(cls):
#         return random.choice(cls.__letters)

#     @classmethod
#     def random_digits(cls):
#         return random.choice(cls.__digits)

#     @staticmethod
#     def random_char(string):
#         if not isinstance(string, str):
#             raise TypeError('需要字符参数')

#         return random.choice(string)

# # print(Char.__letters)
# # print(Char.__digits)
# print(Char.__dict__)
# print(Char.random_letters())
# print(Char.random_digits())
# print(Char.random_char('imooc'))

# class A(object):
#     f = 3

#     def __init__(self, fruit):
#         self.fruit = fruit

#     def have(self):
#         print(f'I have an {self.fruit}')

# class B(A):
#     def __init__(self):
#         # A.__init__(self)
#         super().__init__('apple')
#         self.banana = 'banana'

#     def who(self):
#         print(self.fruit)
#         self.have()

# b = B()
# b.who()
# print(issubclass(B, A))

# class C(object):
#     pass

# print(C)

# def filter_nums(nums: list, want_it):
#     return print([n for n in nums if want_it(n)])

# filter_nums([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

# import datetime
# import functools

# def time(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print(f'[{datetime.datetime.now()}]')
#         return func(*args, **kw)
#     return wrapper

# @time
# def say_hello(name):
#     print(f'Hello! {name}')

# # say_hello('yang')
# print(say_hello.__name__)

# reslut = x if x > 0 else -x

# class Student(object):
#     def __init__(self, name: str, score: float):
#         self.name = name
#         self.__score = score
    
#     @property
#     def score(self) -> int:
#         return self.__score

#     @score.setter
#     def score(self, score: float):
#         if score < 0 or score > 100:
#             raise ValueError('成绩错误')
#         self.__score = score

# stu = Student('ycy', 80)
# print(stu.name)
# print(stu.score)
# stu.score = 90
# print(stu.score)

# import pickle, json

# class Pair(object):
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

# pair = Pair(1, 2)

# with open('C:/Users/mi/Desktop/imooc/text.txt', 'wb') as f:
#     content = pickle.dump(pair, f)

# with open('C:/Users/mi/Desktop/imooc/text.txt', 'rb') as f:
#     content = pickle.load(f)

# json_string = json.dumps(pair.__dict__)

# def pair_to_json(pair):
#     return {'first': pair.first, 'second': pair.second}

# json_string = json.dumps(pair, default=pair_to_json)

import multiprocessing
from multiprocessing import freeze_support
import os

def target_func():
    print('子进程运行')
    print('子进程pid：', os.getpid())
    print('子进程ppid', os.getppid())

p = multiprocessing.Process(target=target_func)
p.start()

print('主进程运行')
print('主进程pid：', os.getpid())

if __name__ == '__main__':
    freeze_support()