#Create a program showing hierarchical inheritance with one parent class and two child classes.
class A:
    def func1(self):
        print("this is class A.")
class B(A):
    def func2(self):
        print("this is class B.")
class C(A):
    def func3(self):
        print("this is class C.")

obj1=B()
obj2=C()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
