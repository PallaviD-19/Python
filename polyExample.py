# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:48:11 2021

Program to demonstrate the Polymorphism

@author: Lokesh
"""

class India():
    def lang(self):
        print("Hindi")
    def Capital(self):
        print("Delhi")

class USA():
    def lang(self):
        print("English")
    
    def Capital(self):
        print("Washington, D.C.")

o_Ind=India()
o_USA=USA()

#o_Ind.lang()
#o_Ind.Capital()

#o_USA.lang()
#o_USA.Capital()

# OR

for i in (o_Ind,o_USA):
    i.lang()
    i.Capital()
