#Define Responses------> nel progetto uso la tabella
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I don't understand that command."
}



#Create the main loop
def get_user_input():
    return input("You: ").lower()

def respond(command):
    return responses.get(command, responses["default"])

def calculate(command):
    parts = command.split()
    x, operator, y = int(parts[1]), parts[2], int(parts[3])

    if operator =="+":
        return str(x+y)
    elif operator =="-":
        return str(x-y)
    elif operator =="*":
        return str(x*y)
    elif operator =="/":
        return str(x/y)
    else:
        return "Invalid operator."
    
responses["calculate"] = calculate    


def main():
    print("Welcome to the Chatbot!")

    while True:
        user_input=get_user_input()

        if user_input == "exit":
            print("Goodbye! Have a great day!")
            break

        response = calculate(user_input)
        #response = respond(user_input)
        print("Bot: ", response)

if __name__== "__main__":
    main()
