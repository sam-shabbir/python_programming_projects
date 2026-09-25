# HW - Quiz Game (loop version)
#
# This started as HW.py, my first draft of Quiz Game.py (it only had Question 1).
# Quiz Game.py repeats the same 10 lines for every question. This version stores the
# questions as DATA in a list and uses ONE loop to ask them all, so adding a 6th
# question means adding one dictionary, not copying another block of code.

print("Welcome to the Quiz Game")

# A list of dictionaries: each dictionary holds everything about one question
questions = [
    {"question": "What is the capital of France?",
     "options": ["Berlin", "Madrid", "Paris"],
     "answer": "c"},
    {"question": "What is the largest planet in our solar system?",
     "options": ["Jupiter", "Saturn", "Neptune"],
     "answer": "a"},
    {"question": "What is the smallest country in the world?",
     "options": ["Monaco", "Vatican City", "San Marino"],
     "answer": "b"},
    {"question": "What is the capital of Japan?",
     "options": ["Seoul", "Beijing", "Tokyo"],
     "answer": "c"},
    {"question": "What is the largest ocean on Earth?",
     "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
     "answer": "c"},
]

letters = ["a", "b", "c"] # the letter shown next to each option
score = 0

# enumerate(questions, start=1) gives the question NUMBER (1, 2, 3...) and the question itself
for number, q in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {q['question']}")

    # zip() pairs each letter with an option: ("a", "Berlin"), ("b", "Madrid"), ...
    for letter, option in zip(letters, q["options"]):
        print(f"{letter}) {option}")

    # .strip() removes stray spaces, .lower() means "C" and "c" both count
    answer = input("Your answer: ").strip().lower()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        # look up the text of the right option so the player learns the answer
        correct_option = q["options"][letters.index(q["answer"])]
        print(f"Incorrect! The answer was {q['answer']}) {correct_option}")

# len(questions) instead of a hard-coded 5 - it stays right if questions are added
print(f"\nYour final score is: {score}/{len(questions)}")
