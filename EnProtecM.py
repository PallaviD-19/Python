# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:08:23 2021

Program to demonstrate Encapsulation (protected members)

@author: Lokesh

""" 
 
# Creating a base class
class A:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class    
class B(A):
    def __init__(self):
         
        # Calling constructor of Base class

        A.__init__(self) 
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = B()
         
obj2 = A()
 
# Calling protected member
# Outside class will  result in 
# AttributeError
print(obj2.a)
 