import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey
#print(os.environ['OPENAI_API_KEY'])

#App Framework
st.title('Simple Prompt Based GPT :')
prompt =  st.text_input('Insert Your Prompt here!')

#Init LLMs:
llm = OpenAI(temperature=0.9)

#show results based on prompt:
if prompt:
    response = llm(prompt)
    st.write(response)
