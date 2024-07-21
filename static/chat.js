userId = document.getElementById("userId").value;
roomId = document.getElementById("roomId").value;
ws = new WebSocket(`ws:${window.location.host}/ws/chat/${roomId}`);

ws.open = () => {
    ws.send(
        JSON.stringify({
            'type': 'connected',
            'userId': userId
        })
    )
}


ws.onmessage = (res) => {
    let obj = JSON.parse(res.data)
    if (obj.type === "connected") {
        alert(1)
        document.querySelector('.message').innerHTML += `<span>${obj.message.msg}</span>`
    } else {
        let messageData = JSON.parse(obj.message);
        document
            .querySelector('.message')
            .innerHTML += `<b>${messageData.username}</b></b><span>${messageData.text}</span>`
    }
}


document.getElementById("send-message").addEventListener("click", () => {
    sendmsg();
})

document.getElementById("message").addEventListener("keypress", (event) => {
    if(event.key === "Enter") {
        sendmsg();
    }
})

function sendmsg() {
    let inputText = document.getElementById("message");
    if(inputText.value !== "") {
        ws.send(JSON.stringify({
        "type": "message",
        "text": inputText.value,
        "userId": userId
        }))
        inputText.value = ""
    }
}