let name=prompt("enter name")
url=("https://api.agify.io/?name="+ name)
fetch(url)   //fetch method return promise
.then((Response)=>{
    console.log(Response)
    return Response.json()
})
.then((data)=>{
    console.log(data.name)
    console.log(data.age)
}) 