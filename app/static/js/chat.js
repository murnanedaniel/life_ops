const inputField = document.querySelector("#message");
const chatlog = document.querySelector("#chat-log");
let chatHistory = [];

inputField.addEventListener("keydown", async (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        const message = inputField.value;

        // Update chat history
        chatHistory.push({ role: "user", content: message });

        // Send a request to the Flask server with the user's message and chat history
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ chat_history: chatHistory }),
        });

        // Clear the input field
        inputField.value = "";

        // Decode and display the response
        const decoder = new TextDecoder();
        const reader = response.body.getReader();
        let chunks = "";

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            chunks += decoder.decode(value);
            chatlog.innerHTML = chunks.replace(/\n/g, "<br>");
        }

        // Update chat history with the server's response
        chatHistory.push({ role: "assistant", content: chunks });
    }
});
