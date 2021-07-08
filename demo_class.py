# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:51:40 2021

@author: admin
"""
'''
class Demo(object):
    total = 0   # 类数据成员
    
    def __new__(cls, *args, **kwargs):
        if cls.total >= 3:   # 访问数据成员
            raise Exception("最多只能创建3个对象")
        else:
            return object.__new__(cls)
    
    def __init__(self):
        Demo.total += 1
'''        

"""
class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2
        
    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2
        
    def show(self):
        print(self._value1)
        print(self.__value2)
        
    def __len__(self):
        return 100
    
    def __max__(self):
        return self._value1 if self._value1>self.__value2 else self.__value2
    
a = A(12,20)

print(a.__max__())
"""

'''
class Animal(object):               #基类
    def show(self):
        print("I'm an animal.")
        
class Cat(Animal):                  # 派生类
    def show(self):
        print("I'm a cat.")

class Dog(Animal):                  # 派生类
    def show(self):
        print("I'm a dog.")

class Tiger(Animal):                # 派生类
    def show(self):
        print("I'm a tiger.")

class Test(Animal):                 # 派生类，没有覆盖基类的show()方法
    pass

x = [item() for item in (Animal, Cat, Dog, Tiger, Test)]
for item in x:
    item.show()
'''

class MyDeque(object):
    def __init__(self, iterable=None, maxlen=10):
        if iterable == None:
            self._content = []
            self._current = 0
        else:
            self._content = list(iterable)
            self._current = len(iterable)
            
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current
            
    def __del__(self):
        del self._content
        
    def setSize(self, size):
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size
        
    def appendRight(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current = self._current+1
        else:
            print("The queue is full")
            
    def appendLeft(self,v):
        if self._current<self._size:
            self._content.insert(0,v)
            self._current = self._current+1
        else:
            print("The queue is full")
    
    def popLeft(self):
        if self._current:
            self._current = self._current-1
            return self._content.pop(0)
        else:
            print("The queue is empty")
        
    def popRight(self):
        if self._current:
            self._current = self._current-1
            return self._content.pop()
        else:
            print("The queue is empty")
    
    def rotate(self,k):
        if abs(k) > self._current:
            print("k must <= " + str(self._content))
            return
        self._content = self._content[-k:] + self._content[:-k]
    
    def reverse(self):
        self._content = self._content[::-1]
    
    def __len__(self):
        return self._current
    
    def __str__(self):
        return 'MyDeque(' + str(self._content) + ', maxlen= ' + str(self._size) +')'
    
    __repr__ = __str__
    
    def clear(self):
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        return not self._content
    
    def isFull(self):
        return self._current == self._size
    
#if __name__ == "__main__":
#    print("Please use me as a module.")


























