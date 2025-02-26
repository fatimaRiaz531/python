import streamlit as st
import time

Quiz questions (expanded to 20 Python-related questions)
questions = [
{"question": "What does HTML stand for?",
"options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "None of these"],
"answer": "Hyper Text Markup Language"},
{"question": "Which language is used for web development?",
"options": ["Python", "Java", "JavaScript", "All of the above"],
"answer": "All of the above"},
{"question": "What does CSS stand for?",
"options": ["Cascading Style Sheets", "Colorful Style Sheets", "Computer Style Sheets", "Creative Style Sheets"],
"answer": "Cascading Style Sheets"},
{"question": "What is the correct file extension for Python files?",
"options": [".py", ".python", ".pt", ".px"],
"answer": ".py"},
{"question": "What is the output of print(2 + 3 * 5)?",
"options": ["25", "17", "10", "None of these"],
"answer": "17"},
{"question": "Which keyword is used to define a function in Python?",
"options": ["def", "define", "function", "func"],
"answer": "def"},
{"question": "What is the purpose of the 'pass' statement in Python?",
"options": ["To skip an iteration", "To define an empty block", "To exit a loop", "To raise an exception"],
"answer": "To define an empty block"},
{"question": "What is the result of bool('False') in Python?",
"options": ["True", "False", "None", "Error"],
"answer": "True"},
{"question": "Which data structure is immutable in Python?",
"options": ["List", "Tuple", "Dictionary", "Set"],
"answer": "Tuple"},
{"question": "What is the correct syntax to create an empty set in Python?",
"options": ["{}", "set()", "[]", "()"],
"answer": "set()"},
{"question": "What is the output of 'Hello' + 'World'?",
"options": ["Hello World", "HelloWorld", "Hello+World", "Error"],
"answer": "HelloWorld"},
{"question": "Which method is used to remove the last element from a list?",
"options": ["pop()", "remove()", "delete()", "discard()"],
"answer": "pop()"},
{"question": "What is the output of 3 ** 2 in Python?",
"options": ["6", "9", "5", "Error"],
"answer": "9"},
{"question": "Which module is used to generate random numbers in Python?",
"options": ["random", "math", "statistics", "numpy"],
"answer": "random"},
{"question": "What is the correct way to open a file named 'data.txt' in read mode?",
"options": ["open('data.txt', 'r')", "open('data.txt', 'w')", "open('data.txt', 'a')", "open('data.txt')"],
"answer": "open('data.txt', 'r')"},
{"question": "What is the output of len([1, 2, 3, 4])?",
"options": ["3", "4", "5", "Error"],
"answer": "4"},
{"question": "Which operator is used for exponentiation in Python?",
"options": ["^", "", "//", "%"],
"answer": " "},
{"question": "What is the output of 'Python'[-1]?",
"options": ["P", "n", "o", "Error"],
"answer": "n"},
{"question": "Which function is used to take input from the user in Python?",
"options": ["input()", "read()", "get()", "scan()"],
"answer": "input()"},
{"question": "What is the purpose of the init method in Python classes?",
"options": ["To initialize an object", "To define a class", "To delete an object", "To inherit a class"],
"answer": "To initialize an object"},
]

Initialize session state
if 'current_question' not in st.session_state:
st.session_state.current_question = 0
if 'score' not in st.session_state:
st.session_state.score = 0
if 'game_over' not in st.session_state:
st.session_state.game_over = False
if 'user_name' not in st.session_state:
st.session_state.user_name = None

Title and subtitle
st.title("Growth Mindset Web Challenge")
st.subheader("Created by Fatima")

Get user's name
if st.session_state.user_name is None:
user_name = st.text_input("Enter your name to start the quiz:")
if st.button("Start Quiz"):
if user_name.strip() == "":
st.error("Please enter your name to proceed.")
else:
st.session_state.user_name = user_name
st.rerun()

Display quiz content only if the user has entered their name
if st.session_state.user_name:
st.write(f"Welcome, {st.session_state.user_name} ! Let's begin the quiz.")
if not st.session_state.game_over:
question_data = questions[st.session_state.current_question]
st.subheader(f"Question {st.session_state.current_question + 1}: {question_data['question']}")

selected_option = st.radio("Select an answer:", question_data['options'], index=None)
if st.button("Submit") and selected_option is not None: # Ensure user selects an option
if selected_option == question_data['answer']:
st.session_state.score += 1
st.balloons()
st.success("Good job! 🎉")
else:
st.error("You selected the wrong answer 😢")

# Add a delay before moving to the next question
time.sleep(2) # Wait for 2 seconds

# Move to the next question
st.session_state.current_question += 1
if st.session_state.current_question == len(questions):
st.session_state.game_over = True
st.rerun()
# Display final score and feedback when the game is over
if st.session_state.game_over:
total_questions = len(questions)
score = st.session_state.score
percentage = (score / total_questions) * 100
# Provide feedback based on performance
if percentage >= 80:
feedback = f"{st.session_state.user_name}, you did amazing! 🎉 Keep shining!"
elif percentage >= 50:
feedback = f"{st.session_state.user_name}, good effort! 💪 Try again to improve."
else:
feedback = f"{st.session_state.user_name}, keep practicing! 🌱 You'll get better with time."
# Display final score and feedback
st.error(f"Game Over 😢 {st.session_state.user_name}, you scored {score}/{total_questions}.")
st.info(feedback)
# Exit button
if st.button("Exit Quiz"):
st.write(f"Thank you for playing, {st.session_state.user_name}! 👋")
st.stop()
# Restart button
if st.button("Restart Quiz"):
st.session_state.current_question = 0
st.session_state.score = 0
st.session_state.game_over = False
st.session_state.user_name = None
st.rerun()