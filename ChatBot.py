def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, but I'm here to help!"
    elif "goodbye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input.lower():
        return "You're welcome! If you have more questions, feel free to ask."
    elif "time" in user_input.lower():
        return "I'm sorry, I don't have real-time capabilities to provide the current time."
    elif "weather" in user_input.lower():
        return "I'm not able to check the weather, but you can use a weather website or app for that!"
    elif "help" in user_input.lower():
        return "Sure, I can help you with a variety of topics. Just let me know what you're looking for!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Simple Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Simple Chatbot: Goodbye!")
            break
        
        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)

if __name__ == "__main__":
    main()
