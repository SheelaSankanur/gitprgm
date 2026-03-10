class Animal:
     def sound():
        print("animal makes sound")
 
class Dog (Animal):
     def sound():
        print("dog barks")

class Cat (Animal):
     def sound():
       print("cat meows")
    
obj=Animal() 
Dog.sound()
Cat.sound()