const websocket = new WebSocket("ws://localhost:8765");
const output = document.getElementById("output");
let currentMessage = ""; // Variable to hold the current message during streaming

websocket.onmessage = function(event) {
    const data = event.data;

    if (data === '\n') {
        output.innerHTML += currentMessage + "\n\n"; 
        currentMessage = ""; 
    } else {
        currentMessage += data;

        setTimeout(() => {
            output.innerHTML = currentMessage; 
        }, 100); 
    }
};

function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const message = messageInput.value;
    websocket.send(message);
    messageInput.value = ""; // Clear the input field
}