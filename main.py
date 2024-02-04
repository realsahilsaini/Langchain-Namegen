import os
import streamlit as st
import langchain_helper
from dotenv import load_dotenv, dotenv_values
load_dotenv()
# print(os.getenv('OPENAI_API_KEY'))




st.title("Startup Name & Tagline  Generator")

industry = st.selectbox(
    'What is the Industry type?',
    ('Food', 'Tech', 'Aerospace', 'Energy', 'Electronics', 'Marine', 'Cybersecurity')
)


if(industry):
    response = langchain_helper.generate_name_and_tagline(industry)
    st.header(response['startup_name'])
    st.write(response['startup_tagline'])
    
    
    