from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai 
import streamlit as st
import os
from langchain.prompts import PromptTemplate

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def summarize(text):
      generic_template='''
      Summarize the following text :
      text :{text}
      '''

      prompt = PromptTemplate(
          input_variables=['text'],
          template=generic_template
      )
      llm_prompt = prompt.format(text=text)
      #Initialize the LLLM MOdel
      llm_model = genai.GenerativeModel("gemini-1.5-flash")
      summary = llm_model.generate_content(llm_prompt,)
      
      return summary.text


st.set_page_config(page_title="Text Summarization")
st.header("Text Summarization using LLM Model")
text = st.text_area("Paste the text which you summarize... ", height=300)
submit = st.button("Summarize")
with st.spinner("Generating Text..."):
  if submit:
      response = summarize(text)
      st.subheader("Summarize Text")
      st.text_area("Response: ",value=response , height=400)

