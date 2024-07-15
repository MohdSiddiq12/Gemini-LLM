import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Gemini model and get reponses

model = genai.GenerativeModel('gemini-pro')

def get_gemini_resonse(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("input: ", key = "input")
submit = st.button("Ask the Question")

##when submit is clicked
if submit:
    response=get_gemini_resonse(input)
    st.subheader("The Response is")
    st.write(response)