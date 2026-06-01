knowledge_base = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What brings you here?",
    "how are you": "I'm functioning optimally, thank you for asking!",
    "what is your name": "I'm a Rule-Based AI Chatbot, built for efficiency.",
    "what can you do": "I can respond to predefined queries instantly using O(1) dictionary lookups.",
    "help": "Try saying: hello, how are you, what is your name, what can you do, or bye.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Happy to assist.",
    "weather": "I don't have live weather data, but you can check a forecast service.",
    "time": "I don't have a clock, but your system knows the time!",
}

while True:
    user_input = input("You: ").strip().lower()
    if user_input == "exit":
        print("Bot: Shutting down. Goodbye!")
        break
    response = knowledge_base.get(user_input, "I don't understand that. Type 'help' to see available commands.")
    print(f"Bot: {response}")
