function printdata(data){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("data")
            resolve("succes")
        }, 3000);                   
        
    })
}
async function dataprint() {
    await printdata()
    await printdata()
    await printdata()
}
dataprint()