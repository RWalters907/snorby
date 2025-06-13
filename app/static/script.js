document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("summary-form");
    const textInput = document.getElementById("text-input");
    const resultBox = document.getElementById("result");
    const summaryText = document.getElementById("summary-text");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const text = textInput.value.trim();

        if (!text) return;

        try {
            const response = await fetch("/summarize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({ text }),
            });

            const data = await response.json();
            if (data.summary) {
                summaryText.textContent = data.summary;
                resultBox.style.display = "block";
            } else {
                summaryText.textContent = "No summary returned.";
                resultBox.style.display = "block";
            }
        } catch (error) {
            summaryText.textContent = "An error occurred.";
            resultBox.style.display = "block";
            console.error("Error:", error);
        }
    });
});
