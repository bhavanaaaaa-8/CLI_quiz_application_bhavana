import json
import random


def load_questions(filename):
    try:
        with open(filename, "r") as file:
            questions = json.load(file)

        if not isinstance(questions, list) or not questions:
            print("Error: No questions found in the file.")
            return []

        return questions

    except FileNotFoundError:
        print("Error: Questions file not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return []


def run_quiz(questions):
    random.shuffle(questions)

    score = 0
    correct = 0
    incorrect = 0

    print("\n===== QUIZ APPLICATION =====")

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer! Please enter A, B, C, or D.")

        if answer == question["answer"].strip().upper():
            print("Correct!")
            score += 1
            correct += 1
        else:
            print(f"Incorrect! Correct answer: {question['answer']}")
            incorrect += 1

    total = len(questions)
    percentage = (score / total) * 100

    print("\n===== FINAL RESULT =====")
    print(f"Total questions: {total}")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Final score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Result: Excellent!")
    elif percentage >= 60:
        print("Result: Good job!")
    elif percentage >= 40:
        print("Result: Keep practising!")
    else:
        print("Result: More practice needed.")


def main():
    questions = load_questions("questions.json")

    if questions:
        run_quiz(questions)


if __name__ == "__main__":
    main()
    
