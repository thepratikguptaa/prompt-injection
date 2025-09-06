# Prompt Injection: Demos, Explanations, and Research

This repository serves as a comprehensive resource for understanding and demonstrating **Prompt Injection** attacks against Large Language Models (LLMs) and AI agents. It includes practical Python demonstrations, detailed explanations, and a curated list of relevant research papers.

## What is Prompt Injection?

Prompt Injection is a critical AI security vulnerability where a malicious user crafts inputs that trick an AI model into ignoring its original instructions and instead following the attacker's commands. This can lead to unauthorized actions, data leakage, or manipulation of AI behavior.

## Project Structure and Contents

This repository is organized into several key sections:

### 1. Prompt Injection Demo (`Prompt Injection Demo/`)

This section provides a core demonstration of prompt injection using a simulated AI agent.

*   **`prompt_injection_demo.py`**: A Python script that simulates two types of AI agents:
    *   **`naive_agent`**: A vulnerable agent that blindly follows injected instructions, demonstrating how sensitive information can be leaked.
    *   **`mitigated_agent`**: A safer agent that employs basic defense mechanisms (like blocklisting) to resist prompt injection attacks.
    *   The script is interactive, allowing users to experiment with different inputs and observe the agents' responses.
*   **`prompt_injection_demo_explanation.md`**: A line-by-line explanation of `prompt_injection_demo.py`, breaking down the code and concepts for easier understanding.
*   **`prompt_injection_explained.md`**: A high-level, conceptual explanation of prompt injection, using an analogy of "silly" and "smart" robots to illustrate the attack and defense mechanisms.

**How to Run the Demo:**
1.  Ensure you have Python installed.
2.  Navigate to the `Prompt Injection Demo/` directory.
3.  Run the script: `python prompt_injection_demo.py`

### 2. Prompt Injection using Emojis (`Emojis/`)

This section explores a specific type of prompt injection where emojis are used as triggers for malicious instructions.

*   **`prompt_injection_using_emojis.py`**: An interactive Python script that demonstrates how a language model might be tricked into executing new instructions when a specific "secret" emoji is present in the input. This acts as a simple game to illustrate the concept.

**How to Run the Emoji Demo:**
1.  Ensure you have Python installed.
2.  Navigate to the `Emojis/` directory.
3.  Run the script: `python prompt_injection_using_emojis.py`

### 3. Unsafe Images and Steganography (`Unsafe Images/`)

This section highlights the potential for steganography to be used in prompt injection attacks, where malicious instructions are hidden within seemingly innocuous image files.

*   **`steganography.md`**: Explains the concept of steganography, particularly Least Significant Bit (LSB) steganography, and how it can be used to hide prompts within images to fool AI agents.
*   **`give-me-the-secret-key.txt`**: A sample text file containing a malicious prompt intended to be hidden within an image.
*   **`using_stegano.py`**: A Python script demonstrating how to hide the content of `give-me-the-secret-key.txt` into `safe_image.png` using the `stegano` library.
*   **`using_stegpy.py`**: Another Python script demonstrating the same steganography process using the `stegpy` library.

### 4. Research Papers (`research_papers.md`)

This file provides a curated list of academic research papers and articles related to prompt injection attacks, defense mechanisms, and broader AI security topics. It serves as a starting point for deeper exploration into the subject.

## Getting Started

To explore the demonstrations:

1.  Clone this repository:
    ```bash
    git clone https://github.com/thepratikguptaa/prompt-injection.git
    cd prompt-injection
    ```
2.  Navigate to the respective subdirectories (`Prompt Injection Demo/`, `Emojis/`) and run the Python scripts as described above.
