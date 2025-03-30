#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆
import time

def quiz_game():
    questions = [
        {
            "question": "Which of these is a mutable data type in Python?",
            "options": ["A) Tuple", "B) List", "C) String", "D) Integer"],
            "answer": "B"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A) Steven Spielberg", "B) James Cameron", "C) Christopher Nolan", "D) Quentin Tarantino"],
            "answer": "C"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Rome", "D) Paris"],
            "answer": "D"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        }
    ]
    
    score = 0
    
    print("Welcome to the Quiz! 🏆\n")
    time.sleep(1)# to make a small delay before asking another question 
    
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}\n")
        
        time.sleep(1)
    
    print(f"Your final score: {score}/{len(questions)}")
    print("🏆 Thanks for playing! 🏆\n")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()
    else:
        print("Goodbye! 👋")

quiz_game()
