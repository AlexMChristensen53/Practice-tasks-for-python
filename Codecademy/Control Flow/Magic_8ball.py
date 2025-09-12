import random

name = "Alex"
question = "Do you like poop?"
answer = ""
random_number = random.randint(1, 12)

if random_number == 1:
    answer = "Yes, definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "I think you should seek help"
elif random_number == 10:
    answer = "are you retarded?"
elif random_number == 11:
    answer = "did you leave your brain at home?"
elif random_number == 12:
    answer = "i don't think so?"
else:
    answer = "error"

if name == "":
    print(question, "answer:", answer)
if question == "":
    print(name, "" "ask me a question")
else:
    print(f"{name} asks: {question} answer: {answer}")
