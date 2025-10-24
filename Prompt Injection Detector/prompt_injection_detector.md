# Prompt Injection Detector

This Python script, `prompt_injection_detector.py`, is a simple tool designed to detect potential Prompt Trigger Attacks (PTAs). It uses a basic heuristic approach to identify common attack patterns in user-provided prompts.

## How it Works

The detector operates on two main principles:

1.  **Trigger Phrase Matching:** It checks the user's prompt against a predefined list of common trigger phrases associated with prompt injection. The prompt is first normalized (converted to lowercase and punctuation is removed) to make the matching more effective.

2.  **Suspicious Character Detection:** It scans the prompt for characters that are often used to manipulate or inject commands, such as newlines (`\n`), tabs (`\t`), and code-related symbols (`#`, `;`, `{`, `}`).

If either a trigger phrase or a suspicious character is found, the script flags the prompt as a potential attack.

## Usage

To use the detector, you can import the `detect_pta` function into your own Python code or run the script directly from the command line to see the example outputs.

```bash
python prompt_injection_detector.py
```

## Examples

The script includes several test cases that demonstrate its functionality:

*   A benign prompt that should not be flagged.
*   An obvious attack that is easily caught.
*   A more subtle attack that is also detected.
*   A benign prompt containing suspicious characters that gets flagged.

## Limitations

This detector is a very basic implementation and can be easily bypassed. It relies on a fixed list of keywords and characters, making it vulnerable to more sophisticated attacks that use obfuscation, synonyms, or complex sentence structures. It should be considered a proof-of-concept and not a production-ready security solution.
