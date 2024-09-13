#from langchain.llms import OpenAI

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyB9ty-TUKHkmkhWUtV6G_qwMNtM6mG7CQo"

# Load the Google API key from environment variables
genai.configure(api_key=GOOGLE_API_KEY)

## Function to load Gemini model and get responses related to car repair
def get_gemini_response(damage_type, damage_strength, damage_part):
    model = genai.GenerativeModel('gemini-pro')

    # Pre-defined prompt to focus the chatbot on car damage repair
    mechanic_prompt = (
        "You are a professional car repair mechanic. The car has the following damage: "
        "Please provide the possible risks that can occur due to the " f"{damage_type} damage, with a severity of {damage_strength}% on the {damage_part}. Also, suggest some solutions/precautions that should be followed. Please provide me step-by-step process to fix or remove " f"{damage_type} on a car? What are the required tools for it? Please provide a detailed cost estimation for fixing or removing " f"{damage_type} on a car?"
        "Make sure the response is only about car damage repair."
        
        
    )

    # Generate response based on the prompt
    response = model.generate_content(mechanic_prompt)
    
    return response.text

## Initialize the Streamlit app
st.set_page_config(page_title="Car Repair Mechanic - Text Response Demo")

# Display logo at the top center
st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image("Innovent logo.png", width=200)
st.markdown('</div>', unsafe_allow_html=True)

st.header("AI Car Repair Mechanic")

# Input fields for damage type, damage strength, and damage part
damage_type = st.text_input("Enter the type of damage (e.g., dent, scratch, etc.):", key="damage_type")
damage_strength = st.slider("Enter the damage strength (percentage):", 0, 100, 50, key="damage_strength")
damage_part = st.text_input("Enter the part of the car that is damaged (e.g., door, bumper, etc.):", key="damage_part")

submit = st.button("Ask the Mechanic")

## If the button is clicked, get a response related to car repair
if submit:
    if damage_type.strip() and damage_part.strip():  # Ensure inputs are provided
        response = get_gemini_response(damage_type, damage_strength, damage_part)
        st.subheader("Repair Analysis")
        st.write(response)
    else:
        st.write("Please provide all the details about the car damage to get an analysis.")
