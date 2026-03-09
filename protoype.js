function Createphone(color){
    //console.log(this)
    console.log(this)
    this.company="apple"
    this.model="iphone12"
    this.price=50000
    this.color=color
} 
Createphone.prototype.company="apple"
Createphone.prototype.model="iphone12" 
Createphone.prototype.price=50000

let ph1 =new Createphone("black")
console.log(ph1)
let ph2 =new Createphone("white")
console.log(ph2)
let ph3 =new Createphone("red")
console.log(ph3)