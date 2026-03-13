let h1=document.querySelector("h1")
let name=prompt("enter name")
url=("https://api.agify.io/?name="+ name)
fetch(url)   //fetch method return promise
.then((Response)=>{
    console.log(Response)
    return Response.json() 
})
.then((data)=>{
    h1.textContent=`${data.name} is ${data.age}`
})