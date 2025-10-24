# Prompt Injection Detectors

This directory contains various Python scripts designed to detect potential Prompt Trigger Attacks (PTAs). Each script employs a different approach, showcasing the evolution and challenges in building robust prompt injection defenses.

## weak_detector.py (Keyword-based Detection)

This Python script, `weak_detector.py`, is a simple tool designed to detect potential Prompt Trigger Attacks (PTAs). It uses a basic heuristic approach to identify common attack patterns in user-provided prompts.

### How it Works

The detector operates on two main principles:

1.  **Trigger Phrase Matching:** It checks the user's prompt against a predefined list of common trigger phrases associated with prompt injection. The prompt is first normalized (converted to lowercase and punctuation is removed) to make the matching more effective.

2.  **Suspicious Character Detection:** It scans the prompt for characters that are often used to manipulate or inject commands, such as newlines (`\n`), tabs (`\t`), and code-related symbols (`#`, `;`, `{`, `}`).

If either a trigger phrase or a suspicious character is found, the script flags the prompt as a potential attack.

### Usage

To use the detector, you can import the `detect_pta` function into your own Python code or run the script directly from the command line to see the example outputs.

```bash
python weak_detector.py
```

### Examples

The script includes several test cases that demonstrate its functionality:

*   A benign prompt that should not be flagged.
*   An obvious attack that is easily caught.
*   A more subtle attack that is also detected.
*   A benign prompt containing suspicious characters that gets flagged.

### Limitations

This detector is a very basic implementation and can be easily bypassed. It relies on a fixed list of keywords and characters, making it vulnerable to more sophisticated attacks that use obfuscation, synonyms, or complex sentence structures. It should be considered a proof-of-concept and not a production-ready security solution.

## better_detector.py (LLM-based Detection)

This script, `better_detector.py`, offers a more advanced approach to detecting Prompt Trigger Attacks (PTAs) by leveraging the capabilities of a Large Language Model (LLM), specifically the Gemini-2.5-flash model. Instead of relying on static keyword matching, it delegates the detection task to the LLM itself.

### How it Works

The script employs a hybrid approach to detect Prompt Trigger Attacks:

1.  **Rule-based Heuristics:** Before engaging the LLM, the script first performs a rapid check using a predefined list of keywords and patterns commonly associated with prompt injection attempts (e.g., "ignore previous instructions", "reveal system prompt"). The user prompt is normalized to lowercase, preserving newlines and tabs for more robust pattern matching. If a match is found, a warning is immediately returned, preventing unnecessary LLM calls.

2.  **LLM-based Detection:** If no rule-based injection is detected, the script then sends the user prompt to the Gemini-2.5-flash model. A carefully crafted "system prompt" instructs the LLM to act as an assistant for detecting prompt injection attacks. The LLM is asked to respond with a concise warning message if it identifies the prompt as malicious, or to provide the desired output if the prompt is benign. This method aims to be more robust against obfuscation and novel attack techniques compared to simple keyword matching alone.

### Usage

Before running, ensure you have an `API_KEY` for the Gemini API set in a `.env` file in the same directory.

Install necessary libraries:
```bash
pip install openai python-dotenv
```

Run the script and enter your prompt when prompted:
```bash
python better_detector.py
```

### Limitations

While this hybrid method is more sophisticated and robust than purely keyword-based detection, it is still not foolproof. Rule-based heuristics can be bypassed by novel obfuscation techniques, and LLMs can sometimes be "jailbroken" or tricked into ignoring their system prompts. Performance and accuracy depend heavily on the underlying LLM's capabilities and the effectiveness of both the rule set and the system prompt. Requires an active internet connection and API access to the LLM.
