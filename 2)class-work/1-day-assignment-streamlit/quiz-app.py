import streamlit as st

# Quiz questions (20 programming-related questions)
questions = [
    {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "None of these"], "answer": "Hyper Text Markup Language"},
    {"question": "Which language is used for web development?", "options": ["Python", "Java", "JavaScript", "All of the above"], "answer": "All of the above"},
    {"question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Colorful Style Sheets", "Computer Style Sheets", "Creative Style Sheets"], "answer": "Cascading Style Sheets"},
    {"question": "Which of the following is a JavaScript framework?", "options": ["Django", "Flask", "React", "Ruby on Rails"], "answer": "React"},
    {"question": "What is the correct syntax to output 'Hello World' in Python?", "options": ["echo 'Hello World'", "print('Hello World')", "console.log('Hello World')", "print:('Hello World')"], "answer": "print('Hello World')"},
    {"question": "Which HTML element is used to define the title of a document?", "options": ["<title>", "<head>", "<meta>", "<body>"], "answer": "<title>"},
    {"question": "What is the main purpose of a database?", "options": ["To store data", "To process data", "To visualize data", "To encrypt data"], "answer": "To store data"},
    {"question": "Which of the following is a back-end programming language?", "options": ["HTML", "CSS", "JavaScript", "PHP"], "answer": "PHP"},
    {"question": "What does API stand for?", "options": ["Application Programming Interface", "Application Programming Integration", "Application Program Interface", "None of these"], "answer": "Application Programming Interface"},
    {"question": "Which of the following is a version control system?", "options": ["Git", "GitHub", "Bitbucket", "All of the above"], "answer": "All of the above"},
    {"question": "What is the purpose of the 'return' statement in a function?", "options": ["To exit the function", "To return a value", "To print a value", "Both A and B"], "answer": "Both A and B"},
    {"question": "Which of the following is not a programming language?", "options": ["Python", "Java", "HTML", "C++"], "answer": "HTML"},
    {"question": "What is the output of 2 + 2 in Python?", "options": ["2", "4", "22", "Error"], "answer": "4"},
    {"question": "Which of the following is a front-end framework?", "options": ["Django", "Flask", "Angular", "Spring"], "answer": "Angular"},
    {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Structured Question Language", "Scripting Query Language", "None of these"], "answer": "Structured Query Language"},
    {"question": "Which of the following is used to style web pages?", "options": ["HTML", "CSS", "JavaScript", "All of the above"], "answer": "CSS"},
    {"question": "What is the purpose of a loop in programming?", "options": ["To repeat a block of code", "To store data", "To define a function", "To create a variable"], "answer": "To repeat a block of code"},
    {"question": "Which of the following is a popular Python web framework?", "options": ["Django", "Flask", "Both A and B", "Ruby on Rails"], "answer": "Both A and B"},
    {"question": "What is the main function in a C program?", "options": ["start()", "main()", "run()", "execute()"], "answer": "main()"},
    {"question": "Which of the following is used for styling web pages?", "options": ["HTML", "CSS", "JavaScript", "All of the above"], "answer": "CSS"},
    {"question": "What is the purpose of comments in code?", "options": ["To explain code", "To make code run faster", "To create variables", "None of these"], "answer": "To explain code"}
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("Programming Quiz Challenge")

if not st.session_state.game_over:
    question_data = questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}: {question_data['question']}")
    
    selected_option = st.radio("Select an answer:", question_data['options'])
    
    if st.button("Submit"):
        if selected_option:  # Check if an option is selected
            if selected_option == question_data['answer']:
                st.session_state.score += 1
                st.balloons()  # Show balloons for correct answer
                st.success("Good job! 🎉")
            st.session_state.current_question += 1
            if st.session_state.current_question == len(questions):
                st.session_state.game_over = True
                st.experimental_rerun() 
        else:
            st.warning("Please select an answer before submitting.")

if st.session_state.game_over:
    st.error(f"Game Over 😢 You scored {st.session_state.score}/{len(questions)}. Try again!")

    # Buttons to restart or exit
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.game_over = False
            st.experimental_rerun()  # Restart the app

    with col2:
        if st.button("Exit"):
            st.write("Thank you for playing! Goodbye!")