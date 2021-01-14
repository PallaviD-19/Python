# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:58:12 2021

Program to demonstrate the Inheritance (Multilevel)

@author: Pallavi
"""

class Person():
    pcount=0
    def __init__(self,name,age,mobNo):
        self.name=name
        self.age=age
        self.mobNo=mobNo
        Person.pcount+=1

#    if we define this method than 
#    no need to write the display method and no need to call that method

#    def __str__(self):
#        return "\nName: "+self.name+"\nId : "+str(self.age)+"\nMobile: "+str(self.mobNo)

    def display(self):
        print("\n Name: ",self.name,"\n Age: ",self.age,"\n MObile no: ",self.mobNo)
      
  
#    def countShow():
#        print("Total Person: %d" %Person.pcount)
 
    
class Employee(Person):
    def __init__(self,name,age,mobNo,eid,salary,desg):
        Person.__init__(self,name,age,mobNo)
        self.eid=eid
        self.salary=salary
        self.desg=desg
        
    
    def display(self):
        Person.display(self)
        print(" Employee Id: ",self.eid,"\n Salary: ",self.salary,"\n Designation: ",self.desg)

   
class SalesManager(Employee):
    def __init__(self,name,age,mobNo,eid,salary,desg,target,insentive):
        Employee.__init__(self,name,age,mobNo,eid,salary,desg)
        self.target=target
        self.insentive=insentive
    
    def display(self):
        Employee.display(self)
        print(" Target: ",self.target,"\n Insentive: ",self.insentive)
 
class Programmer(Employee):
    def __init__(self,name,age,mobNo,eid,salary,desg,ExHrs,chPhr):
        Employee.__init__(self,name,age,mobNo,eid,salary,desg)
        self.ExHrs=ExHrs
        self.chPhr=chPhr
    
    def display(self):
        Employee.display(self)
        print(" Extra Hours: ",self.ExHrs,"\n Charges per hour: ",self.chPhr)
        
        
#p=Person("Pallavi",25,90909090)
#q=Person("Lokesh",30,999990000)
#p=Employee("Pallavi",23,90909090,101,25000,"B.E")
#q=Employee("Lokesh",23,999990000,102,26000,"B.E.")
p=SalesManager("Kajal",23,90909090,101,25000,"B.E",50,10)
q=SalesManager("Vaibhav",23,999990000,102,26000,"B.E.",100,10)
r=SalesManager("Tejaswi",24,98989898,103,25500,"M.B.A",150,10)
p1=Programmer("Pallavi", 23, 9111125071, 101, 25000,"B.E.", 35, 700)
q2=Programmer("Lokesh", 23, 90909090, 102, 26000, "B.E.", 30, 600)
r2=Programmer("Imran", 24, 9999900000, 103, 25500, "B.E.", 25, 650)
p.display()                    
q.display()
r.display()
p1.display()
q2.display()
r2.display()
#Person.countShow()
print("\n Total Person: ",Person.pcount)        
