# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:32:26 2021

Program to demonstrate Encapsulation (Private Member)

@author: Lokesh
"""

class Person:
  def __init__(self): 
    self.name = 'Manjula'
    self.__lastname = 'Dube'
    
  def PrintName(self):
    return self.name +' ' + self.__lastname
    
#Outside class    
P = Person()
print(P.name)
print(P.PrintName())
print(P.__lastname)

#AttributeError: 'Person' object has no attribute '__lastname'

