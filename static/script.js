async function sendMessage() {

    const input = document.getElementById("userInput");

    const message = input.value;

    if(message.trim() === "") {

        return;
    }

    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `

        <div class="user-message">

            <b>You:</b> ${message}

        </div>
    `;

    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `

        <div class="bot-message">

            <b>AI:</b><br>

            ${data.reply.replace(/\\n/g, "<br>")}

        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}
let isSending = false;

document.getElementById("userInput").addEventListener("keydown", async function(event) {
    if (event.key === "Enter" && !isSending) {
        event.preventDefault();
        isSending = true;

        try {
            await sendMessage();
        } finally {
            isSending = false;
        }
    }
});