import random

questions = [
    {"question": "What is the largest planet in our solar system ?", "answer": "Jupiter"},
    {"question": "Who developed the theory of relativity ?", "answer": "Einstein"},
    {"question": "What element does 'O' represent on the periodic table ?", "answer": "Oxygen"},
    {"question": "Who painted the Mona Lisa ?", "answer": "Da Vinci"},
    {"question": "What is the speed of light in vacuum (in km/s) ?", "answer": "300000"},
]

def quiz():
    score = 0
    random.shuffle(questions)  # Shuffle the questions
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").strip().lower()
        if answer == q["answer"]:
            score += 5
        else:
            score -= 2
    return score

def main():
    print("Welcome to the Challenging Quiz!")
    print("Each correct answer will award you 5 points.")
    print("Each incorrect answer will deduct 2 points.")
    print("Let's get started!\n")
    score = quiz()
    total_questions = len(questions)
    max_score = total_questions * 5
    passing_score = max_score * 0.6
    print("\nYour total score is:", score)
    if score >= passing_score:
        print("Congratulations! You passed the quiz.")
    else:
        print("You failed the quiz. Better luck next time.")

if __name__ == "__main__":
    main()

