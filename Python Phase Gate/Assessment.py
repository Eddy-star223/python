
import random


questions = [
    {
        "Number": 1,
        "question": "What is the capital of Ghana??",
        "options": ["Nigeria", "London", "Paris", "Accra"],
        "answer": 3  
    },
    {
        "Number": 2,
        "question": "Which planet is closer to earth?",
        "options": ["Neptune", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "Number": 3,
        "question": "Who is the head of academic at semicolon?",
        "options": ["Mrs. Kim", "Mr. Sikiru", "Mr. Chibuzo", "Miss Ope"],
        "answer": 2
    },
    {
        "Number": 4,
        "question": "What is 7 + 49?",
        "options": ["49", "48", "53", "56"],
        "answer": 3
    },
    {
        "Number": 5,
        "question": "Who was the best graduating student at semicolon cohort 18?",
        "options": ["Mr Francis", "Mr. Evans", "Mr. Tobi", "Miss Ope"],
        "answer": 2
    },
    {
        "Number": 6,
        "question": "Which language is used to create websites?",
        "options": ["HTML", "Python", "C++", "Java"],
        "answer": 0
    },
    {
        "Number": 7,
        "question": "What color is the sky on a clear day?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": 1
    },
    {
        "Number": 8,
        "question": "Who is the chief priest of Semicolon cohort 25?",
        "options": ["Okafor", "Timothy", "Justice", "Ibrahim"],
        "answer": 3
    },
    {
        "Number": 9,
        "question": "Which month has 28 days?",
        "options": ["February", "All months", "January", "March"],
        "answer": 1
    },
    {
        "Number": 10,
        "question": "Who was the Second man on earth?",
        "options": ["Adam", "Enoch", "Cain", "Abel"],
        "answer": 3
    }
]


question_number = set()
removed_options = {}  
last_question_id = None
question_1_used = False
score = 0
attempted = 0


def reset():
    question_Number, removed_options, last_question
    question_1, score, attempted
    question_number = set()
    removed_options = {}
    last_question = None
    question_1_used = False
    score = 0
    attempted = 0


def get_current_questions():
    current = []
    for ques in questions:
        if ques["number"] in used_question_number:
            continue  
        if ques["number"] == last_question_number:
            continue  
        if ques["number"] == 1 and question_1_used:
            continue  
        current.append(ques)
    return current


def show_question(question):
    print("\n" + question["question"])
    labels = ['A', 'B', 'C', 'D']
    options = question["options"]

    
   