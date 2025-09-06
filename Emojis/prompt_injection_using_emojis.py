def process_prompt(prompt):
    """
    A simplified function that simulates how a language model might process a prompt.
    In a real scenario, this would be a call to an LLM API.
    """
    if "🤫" in prompt:
        try:
            new_instruction = prompt.split("🤫")[1].strip()
            return f"New instruction received: '{new_instruction}'. Executing that instead."
        except IndexError:
            return "Emoji detected, but no new instruction found."
    else:
        return f"Processing original prompt: '{prompt}'"

def game():
    """
    An interactive game to demonstrate prompt injection with emojis.
    """
    original_instruction = "Translate 'Hello, world!' to French."
    print("--- Welcome to the Prompt Injection Game! ---")
    print("Your goal is to get the language model to do what you want.")
    print(f"The model's current instruction is: '{original_instruction}'")
    print("You can add an emoji and a message to the prompt.")
    print("Try to get the model to tell you a joke instead of translating the text.")
    print("Hint: The secret emoji is 🤫")

    user_input = input("\nEnter your emoji and message: ")

    full_prompt = f"{original_instruction} {user_input}"

    print(f"\nFull Prompt being sent to the model: {full_prompt}")

    model_output = process_prompt(full_prompt)

    print(f"\nModel Output: {model_output}")

    if "joke" in model_output.lower():
        print("\nCongratulations! You successfully injected a new prompt and made the model tell a joke!")
    else:
        print("\nThe model followed the original instruction. Try again!")


if __name__ == "__main__":
    game()