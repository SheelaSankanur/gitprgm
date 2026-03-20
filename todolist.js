function addTask(){
    const input=document.getElementById('taskInput');
    const task=input.value.trim();

    if(task==="")return;

    const li=document.createElement('li')

    const span=document.createElement('span')
    span.textContent=task;

    span.onclick=function(){
        span.classList.toggle('completed');
    }
    const del=document.createElement('span');
    del.textContent='X';
    del.className='delete';

    del.onclick=function(){
        li.remove();
    }
    li.appendChild(span);
    li.appendChild(del);

    document.getElementById('taskList').appendChild(li);
    input.value="";

}
