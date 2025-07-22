# quiz_game.py

questions = {
    "What is the capital of India?": "Delhi",
    "What is the output of 3+5?": "8",
    "Who developed Python?": "Guido van Rossum",
    "Which keyword is used to define a function in Python?": "def"
}

score = 0

print("Welcome to the Python Quiz Game!\n")

for question, answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {answer}.\n")

print(f"🎉 Your final score is {score}/{len(questions)}")
