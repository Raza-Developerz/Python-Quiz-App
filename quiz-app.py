# Simple Quiz App by Raza-Developerz
print("=== Welcome to Python Quiz App ===\n")

questions = [
    "1. Who is the creator of Python?",
    "2. What is 'cout' used for in C++?",
    "3. What is the full form of HTML?",
    "4. What type of language is Java?",
    "5. Where is code saved on GitHub?"
]

options = [
    ["A. Bill Gates", "B. Guido van Rossum", "C. Elon Musk", "D. Mark Zuckerberg"],
    ["A. To take input", "B. To display output", "C. For loops", "D. To create variables"],
    ["A. Hyper Text Markup Language", "B. High Tech Modern Language", "C. Hyper Transfer Markup Language", "D. Home Tool Markup Language"],
    ["A. Procedural", "B. Object Oriented", "C. Functional", "D. Low Level"],
    ["A. In a Folder", "B. In a Repository", "C. In a File", "D. In a Drive"]
]

answers = ["B", "B", "A", "B", "B"]

score = 0

for i in range(len(questions)):
    print(questions[i])
    for opt in options[i]:
        print(opt)

    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answers[i]}.\n")

print("=== Quiz Finished! ===")
print(f"Your Score: {score}/5")

if score == 5:
    print("Excellent! Full marks!")
elif score >= 3:
    print("Good job! Keep learning.")
else:
    print("Keep practicing, you will get better!")
