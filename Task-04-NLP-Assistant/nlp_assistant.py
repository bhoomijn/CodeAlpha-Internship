def generate_response(user_message):
    message = user_message.lower().strip()

    if message in {"hi", "hello", "hey"}:
        return "Hello! How can I help you today?"
    if "how are you" in message:
        return "I am doing well and ready to help you."
    if "your name" in message:
        return "I am a simple Python assistant."
    if "time" in message:
        return "I don't have a real clock, but I am here to help you."
    if "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day."
    if "weather" in message:
        return "I cannot check live weather, but I can help with other tasks."
    if "python" in message:
        return "Python is a powerful programming language used for automation, web apps, and data analysis."
    if "task" in message or "project" in message:
        return "You can organize tasks by breaking them into simple steps and tracking progress."
    if "thank you" in message:
        return "You are welcome!"
    return "I am not sure how to respond to that. Please ask something else."


def main():
    print("Simple NLP Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        response = generate_response(user_input)
        print(f"Assistant: {response}")


if __name__ == "__main__":
    main()
