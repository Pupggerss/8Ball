import random

def shake_8ball():
    responses = [
        "It is certain!",
        "Most likely!",
        "Outlook good!",
        "Yes!",
        "Signs point to yes!",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Very doubtful."
    ]
    return random.choice(responses)

# Main script
if __name__ == "__main__":
    question = input("Ask the Magic 8Ball a question: ")
    answer = shake_8ball()
    print(f"The Magic 8 Ball says: {answer}")
