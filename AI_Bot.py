print("Hi there, I am your friendly chatbot")
name=input("\nWhat's your name? ")
print("Nice to meet you", name)

while True:
    print("Let us check your mood!")
    print("Type 'exit' to stop")
    while True:
        mood=input("\nHow are you feeling today? ")
        if mood.lower() == "exit":
            break
        elif "good" in mood.lower() or "great" in mood.lower() or "nice" in mood.lower():
            print("Glad to hear that!")
        elif "bad" in mood.lower() or "low" in mood.lower() or "sad" in mood.lower():
            print("Hope you feel better soon")
        else:
            print("Yes, I know. Sometimes, it's not easy to express how you feel in words.")

print("That was a fun session. Bye", name)



