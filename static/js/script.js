document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) {
        alert("Please type a message!");
        return;
    }

    const responseDiv = document.getElementById("response");
    responseDiv.innerHTML = "Loading...";

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput }),
        });
        const data = await response.json();
        responseDiv.innerHTML = `Response: ${data.response}`;
    } catch (error) {
        responseDiv.innerHTML = "Error communicating with the server.";
        console.error(error);
    }

    // Function to send the user's message and get a response
document.getElementById('send-btn').onclick = function() {
    let userMessage = document.getElementById('user-input').value;
    if (userMessage.trim() !== "") {
        // Display user message
        let userDiv = document.createElement('div');
        userDiv.classList.add('message', 'user-message');
        userDiv.textContent = userMessage;
        document.getElementById('messages').appendChild(userDiv);

        // Clear input field
        document.getElementById('user-input').value = "";

        // Scroll to bottom of messages
        document.getElementById('messages').scrollTop = document.getElementById('messages').scrollHeight;

        // Get bot response (simulated for now)
        setTimeout(function() {
            let botResponse = "This is the bot's response to: " + userMessage;  // Replace with actual API call
            let botDiv = document.createElement('div');
            botDiv.classList.add('message', 'bot-message');
            botDiv.textContent = botResponse;
            document.getElementById('messages').appendChild(botDiv);

            // Scroll to bottom after bot responds
            document.getElementById('messages').scrollTop = document.getElementById('messages').scrollHeight;
        }, 1000);  // Simulate delay in bot response
    }
};

});
