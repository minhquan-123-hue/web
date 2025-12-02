class TypingTest {
    private readonly WORDS = [
        "the", "be", "to", "of", "and", "in", "that", "have", "it", "for",
        "you", "he", "with", "on", "do", "say", "this", "they", "at", "but",
        "we", "his", "from", "not", "by", "she", "or", "as", "what", "go",
        "their", "can", "who", "get", "if", "would", "her", "all", "my",
        "make", "about", "know", "will", "up", "one", "time", "there", "year"
    ];

    private textDisplay = document.getElementById("text-display")!;
    private input = document.getElementById("input") as HTMLTextAreaElement;
    private timerEl = document.getElementById("timer")!;
    private wpmEl = document.getElementById("wpm")!;
    private accuracyEl = document.getElementById("accuracy")!;
    private restartBtn = document.getElementById("restart")!;

    private targetText = "";
    private startTime: number | null = null;
    private timeLeft = 60;
    private timerInterval: number | null = null;
    private correctChars = 0;
    private totalTypedChars = 0;

    constructor() {
        this.init();
        this.bindEvents();
    }

    private init(): void {
        this.targetText = this.generateRandomText(80);
        this.renderText();
        this.resetStats();
        this.input.disabled = false;
    }

    private generateRandomText(wordCount: number): string {
        const words: string[] = [];
        for (let i = 0; i < wordCount; i++) {
            words.push(this.WORDS[Math.floor(Math.random() * this.WORDS.length)]);
        }
        return words.join(" ");
    }

    private renderText(): void {
        const userText = this.input.value;
        const chars = this.targetText.split("").map((char, i) => {
            const typed = userText[i];

            if (typed === undefined) {
                return `<span>${char}</span>`;
            }
            if (typed === char) {
                return `<span class="correct">${char}</span>`;
            }
            return `<span class="incorrect">${char}</span>`;
        });

        // Highlight current character
        if (userText.length < this.targetText.length) {
            const currentIndex = userText.length;
            chars[currentIndex] = `<span class="current">${this.targetText[currentIndex]}</span>`;
        }

        this.textDisplay.innerHTML = chars.join("");
    }

    private startTimer(): void {
        if (this.startTime) return;

        this.startTime = Date.now();
        this.timerInterval = setInterval(() => {
            this.timeLeft--;
            this.timerEl.textContent = this.timeLeft.toString();

            if (this.timeLeft <= 0) {
                this.endTest();
            }
        }, 1000);
    }

    private calculateWPM(): number {
        if (!this.startTime) return 0;
        const minutesElapsed = (60 - this.timeLeft) / 60;
        return minutesElapsed > 0 ? Math.round(this.correctChars / 5 / minutesElapsed) : 0;
    }

    private calculateAccuracy(): number {
        return this.totalTypedChars > 0
            ? Math.round((this.correctChars / this.totalTypedChars) * 100)
            : 100;
    }

    private updateStats(): void {
        this.wpmEl.textContent = this.calculateWPM().toString();
        this.accuracyEl.textContent = this.calculateAccuracy() + "%";
    }

    private resetStats(): void {
        this.timeLeft = 60;
        this.timerEl.textContent = "60";
        this.wpmEl.textContent = "0";
        this.accuracyEl.textContent = "100%";
        this.correctChars = 0;
        this.totalTypedChars = 0;
        this.startTime = null;
        if (this.timerInterval) clearInterval(this.timerInterval);
    }

    private endTest(): void {
        this.input.disabled = true;
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.updateStats();
    }

    private handleInput(): void {
        if (!this.startTime) this.startTimer();

        const userText = this.input.value;
        this.totalTypedChars = userText.length;
        this.correctChars = userText
            .split("")
            .filter((char, i) => char === this.targetText[i]).length;

        this.renderText();
        this.updateStats();

        if (userText === this.targetText) {
            this.endTest();
        }
    }

    private handleRestart(): void {
        this.input.value = "";
        this.init();
    }

    private bindEvents(): void {
        this.input.addEventListener("input", () => this.handleInput());
        this.restartBtn.addEventListener("click", () => this.handleRestart());
    }
}

// Start the app
new TypingTest();