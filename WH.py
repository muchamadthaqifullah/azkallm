import streamlit as st
import google.generativeai as genai
GoogleAI_API = "AIzaSyBNcXPwSvBBHlIG6Vy7vZmOsdFV1aPMslw"
# Configure the API key
genai.configure(api_key=GoogleAI_API)

# Set default parameters
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

st.title('World History Assistant')

additional_prompt = "I would like to ask about world history."
user_input = st.text_input("Ask questions about history:")
prompt = additional_prompt + " " + user_input

# When the 'Generate' button is pressed, generate the text
if st.button('Give Me The Answer'):
    response = genai.generate_text(
      **defaults,
      prompt=prompt
    )
    st.write(response.result)