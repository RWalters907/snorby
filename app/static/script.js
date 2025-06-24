document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("summary-form");
    const textInput = document.getElementById("text-input");
    const resultBox = document.getElementById("result");
    const summaryText = document.getElementById("summary-text");
    const downloadLink = document.getElementById("download-link");
    const button = document.getElementById("summarize-button");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const text = textInput.value.trim();
        if (!text) return;

        // Bounce animation
        button.classList.remove("bouncing");
        void button.offsetWidth;
        button.classList.add("bouncing");

        // UI reset
        summaryText.textContent = "";
        resultBox.style.display = "none";
        downloadLink.style.display = "none";
        button.disabled = true;

        try {
            const response = await fetch("/summarize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text }),
            });

            const data = await response.json();
            if (response.ok && data.summary) {
                summaryText.textContent = data.summary;
                resultBox.style.display = "block";

                if (data.filename) {
                    downloadLink.href = `/download/${data.filename}`;
                    downloadLink.setAttribute("download", data.filename);
                    downloadLink.style.display = "inline-block";
                }
            } else {
                summaryText.textContent = "❌ Error: " + (data.error || data.detail || "No summary returned.");
                resultBox.style.display = "block";
            }
        } catch (error) {
            summaryText.textContent = "❌ Error connecting to server.";
            resultBox.style.display = "block";
            console.error("Fetch error:", error);
        }

        button.disabled = false;
    });
});
