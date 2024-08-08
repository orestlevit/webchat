userId = document.getElementById("userId").value;
roomId = document.getElementById("roomId").value;
ws?.close()
ws = new WebSocket(`ws:${window.location.host}/ws/chat/${roomId}`);

ws.onopen = () => {
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
        alertify.success(obj.message.msg);
    } else {
        let messageData = JSON.parse(obj.message);
        if (messageData.userId === userId) {
            document.querySelector(".message").innerHTML += `<p class='own'>${messageData.text}</p>`;
        } else {
            let avatar = document.getElementById("avatar").src;
            document.querySelector(".message").innerHTML += `
                <p class="d-flex">
                    <img src="${avatar}" class="rounded-circle me-2" width="50">
                    <span>
                        <b>${messageData.username}</b><br>
                        ${messageData.text}
                        </span>
                </p>

        `
    }
 }
 document.querySelector(".messages-container").scrollTo(0, document.querySelector(".messages-container").scrollHeight)
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