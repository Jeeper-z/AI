function sendMessage() {
    let message = document.getElementById("message").value;

    if (message.trim() === "") {
        return;
    }
    fetch("/chat", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({ message })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("chat").innerHTML +=
                "<p><b>You:</b> " + message + "</p>";
            if (data.error) {
                document.getElementById("chat").innerHTML +=
                    "<p><b>Bot:</b> " + data.error + "</p>";
            } else {
                document.getElementById("chat").innerHTML +=
                    "<p><b>Bot:</b> " + data.response + "</p>";
            }
        });
    alert(message);
}