#Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random
import time
def tel_joke():
    jokes= [
        "Why do Python programmers prefer dark mode? 👉 Because light attracts bugs! 🪲",
        "Why did the Python function break up with the loop? 👉 It felt trapped in an infinite relationship! 😆",
        "Why don’t Python programmers like nature? 👉 Too many bugs!",
        "What do you call a snake that works with data?👉 A Pythonista! 🐍",
        "Why did the developer go broke?👉 Because they used float too much! 💸" ,
        "What’s a Python programmer’s favorite breakfast?👉 sliced bread! 🍞" ,
        "Why did the Python programmer get locked out of their house?👉 They forgot their keys()! 🔑" ,
        "How does a Python loop flirt?👉 It just keeps repeating itself! 😉" ,
        "Why did the Python developer stay calm?👉 Because they had good try-except handling!" ,
        "What do you call a Python list with lots of errors? 👉 A mist! 😅" 
     ]


    joke = random.choice(jokes)
    print("\nWelcome to the Python Joke Generator! 🤖🐍")
    print("Here's your joke for today:")
    print("-" * 50)
    print(joke)
    print("-" * 50)
tel_joke()
