class Animal{
    sound(){
        console.log("animal makes sound")
    }
}
class Dog extends Animal{
    sound(){
        console.log("dog barks")
    }
}
class Cat extends Animal{
    sound(){
        console.log("cat meows")
    }
}
let dog=new Dog()
dog.sound()
let cat=new Cat()
cat.sound() 