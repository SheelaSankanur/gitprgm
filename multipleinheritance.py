#Create three classes A, B, and C to demonstrate multilevel inheritance.
class A:
     def func1(self):
          print("this is class A.")
class B(A):
     def func2(self):
          print("this is class B.")
class C(B):
     def func3(self):
          print("this is class C.")

obj=C()
obj.func1()
obj.func2()
obj.func3()
