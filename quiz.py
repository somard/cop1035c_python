# Quiz Questions
questions = {
    "What is the capital of France?": "a",
    "What programming language are we learning?": "b",
    "Which year did the first man land on the Moon?": "c",
}

# Options for each question
options = [
    ["a. Paris", "b. London", "c. Berlin", "d. Madrid"],
    ["a. Java", "b. Python", "c. C++", "d. JavaScript"],
    ["a. 1972", "b. 1969", "c. 1966", "d. 1971"],
]

def quiz_game():
    score = 0
    for question, correct_answer in questions.items():
        print(question)
        # Display options for the current question
        for option in options[list(questions.keys()).index(question)]:
            print(option)
        # Get user answer
        answer = input("Enter your answer (a, b, c, d): ").lower()
        # Check if the answer is correct
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
        print()  # Print empty line for spacing
    
    # Display final score
    print(f"Quiz Over! You scored {score}/{len(questions)}.")

# Start the quiz
if __name__ == "__main__":
    quiz_game()

