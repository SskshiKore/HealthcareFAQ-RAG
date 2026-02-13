async function sendMsg(){
 let msg=document.getElementById("msg").value;
 let chat=document.getElementById("chat");
 chat.innerHTML+=`<div class="user">You: ${msg}</div>`;
 let res=await fetch("/ask",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:msg})});
 let data=await res.json();
 chat.innerHTML+=`<div class="bot">Bot: ${data.reply}</div>`;
}
