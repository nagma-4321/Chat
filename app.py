
print("hello")

import streamlit as st

# Initialize session state for tracking
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "user_responses" not in st.session_state:
    st.session_state.user_responses = {}

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

suggestion = (
    "Please convert them to physical copies; otherwise, you might lose them due to storage issues."
)

# Layout configuration
st.set_page_config(page_title="DATE TO MEMORIES (2024 Edition)", layout="centered")

# Header design
st.markdown(
    """
    <div style="background-color:orange; padding:20px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">DATE TO MEMORIES (2024 Edition)</h1>
        <h3 style="color:white; text-align:center;">Reliving Moments, Creating Memories</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat area
st.write("### Chat")
chat_area = st.empty()

# Input area
user_input = st.text_input("Type your response here:")

def display_chat():
    """Function to display chat messages in sequence."""
    for i, (question, response) in enumerate(st.session_state.user_responses.items()):
        st.markdown(
            f"""
            <div style="background-color:#FFC7C7; padding:10px; margin:5px; border:2px solid red; border-radius:10px;">
                <b>Bot:</b> {question}
            </div>
            <div style="background-color:#E1FFC7; padding:10px; margin:5px; border:2px solid red; border-radius:10px;">
                <b>You:</b> {response}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Function to handle response and progression
def handle_response():
    if user_input.strip():
        question = questions[st.session_state.current_question_index]
        st.session_state.user_responses[question] = user_input
        if st.session_state.current_question_index == 7:  # Suggestion on memories
            st.session_state.user_responses["Bot Suggestion"] = suggestion
        st.session_state.current_question_index += 1
    else:
        st.warning("Please provide a response to proceed!")

# Process user input
if st.button("Send"):
    if st.session_state.current_question_index < len(questions):
        handle_response()
    else:
        st.info(
            f"Thank you for your responses, {st.session_state.user_responses.get(questions[0], 'Friend')}! "
            "I appreciate your thoughtful answers and wish you the best for the future."
        )

# Display chat
display_chat()

# Ask the next question
if st.session_state.current_question_index < len(questions):
    st.write(f"**Bot:** {questions[st.session_state.current_question_index]}")






        