import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

conv=[]

user_name = input(f"{Fore.MAGENTA}What is your name? {Style.RESET_ALL}")

print(f"\n{Fore.CYAN}Hello, {user_name}!")

while True:
    print(f"\n{Fore.CYAN}Enter a sentence to analyze. Type exit to stop. Type history to see all sentiments. Type reset to clear history")
    sentence = input(f"{Fore.GREEN}>> {Style.RESET_ALL}")

    if sentence.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Goodbye, {user_name}! {Style.RESET_ALL}")
        break

    elif sentence.lower() == "reset":
        conv.clear()
        print(f"{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif sentence.lower() == "history":
        if not conv:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for i, (text, polarity, sentiment) in enumerate(conv, start=1):
                if sentiment == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment== "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"

                print(f"{i}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment}{Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(sentence).sentiment.polarity
    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😭"

    conv.append((sentence, polarity, sentiment))

    print(f"{color}{emoji} {sentiment} sentiment detected! "
        f"Polarity: {polarity:.2f}")
