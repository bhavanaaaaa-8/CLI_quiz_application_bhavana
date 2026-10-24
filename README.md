# Command-Line Quiz Application

## Description
A Python-based command-line quiz application that loads questions from a separate JSON file, randomizes question order, accepts user answers, calculates scores, and displays a final result.

## Features
- **Separate Question Storage:** Stores questions, options, and correct answers in `questions.json`.
- **Randomized Questions:** Shuffles the question order for each quiz attempt.
- **Input Validation:** Rejects invalid answers and prompts the user to enter A, B, C, or D.
- **Automatic Scoring:** Calculates correct and incorrect answers.
- **Final Results:** Displays the total questions, score, percentage, and performance message.
- **Error Handling:** Handles missing question files and invalid JSON data.

## Technologies Used
- Python 3
- JSON
- `random` module

## Project Structure
```text
quiz_project/
├── quiz.py
└── questions.json
```

## Requirements
- Python 3 installed on your computer.
- Both files saved in the same folder.

No external libraries are required.

## How to Run
1. Download or save `quiz.py` and `questions.json` in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run the following command:

```bash
python quiz.py
```

## How It Works
1. The application loads questions from the JSON file.
2. Questions are shuffled randomly.
3. Each question and its four options are displayed.
4. The user enters an answer.
5. Invalid inputs are rejected until a valid option is entered.
6. The application checks answers and updates the score.
7. A final report displays the score, percentage, and performance message.

## Scoring System
- Correct answer: +1 point
- Incorrect answer: 0 points
- Invalid input: The user is prompted again.

**Percentage formula:**

Percentage = (Correct Answers / Total Questions) × 100

## Customization
To add more questions, edit `questions.json` using the same structure as the existing questions. Each question must contain a `question`, an `options` list, and an `answer`.

## Future Improvements
- Add difficulty levels.
- Add a timer for each question.
- Save quiz results to a file.
- Allow users to choose a quiz category.
- Add negative marking and a leaderboard.

## Author
Created as a Python programming project to practise functions, loops, lists, dictionaries, JSON file handling, input validation, and score calculation.
