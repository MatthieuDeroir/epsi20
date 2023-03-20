import random

while True:
    sentence = input("Enter a sentence: ")
    if sentence.lower() == "exit" or sentence.lower() == "quit":
        break
    answers = ["Interesting!", "Tell me more!", "I see.", "Fascinating!", "Go on...", "Really?", "That's cool!", "I'm listening.", "Hmm, I'm not sure...", "Wow!"]
    print(random.choice(answers))
print("Goodbye!")

