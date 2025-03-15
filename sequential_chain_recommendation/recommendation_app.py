import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st
from dotenv import load_dotenv
from openai_key import another_key

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = another_key

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Define prompt templates
career_prompt = PromptTemplate(
    input_variables=['career'],
    template="I want to become the best {career}, suggest me one really good book in that field with which I can gain immense knowledge. Give me just the name of the book."
)
career_chain = LLMChain(llm=llm, prompt=career_prompt, output_key='book_name')

book_prompt = PromptTemplate(
    input_variables=['book_name'],
    template="Give me a 60-word summary of the book {book_name} with bullet points."
)
book_chain = LLMChain(llm=llm, prompt=book_prompt, output_key='summary')

# Define sequential chain
recommendation_chain = SequentialChain(
    chains=[career_chain, book_chain],
    input_variables=['career'],
    output_variables=['book_name', 'summary']
)

# Streamlit UI
st.set_page_config(page_title="Career Book Recommendation")
st.header("AI-powered Career Book Recommendation")

career_input = st.text_input("Enter your career goal:")
submit = st.button("Get Recommendation")

if submit:
    response = recommendation_chain({'career': career_input})
    st.subheader("Recommended Book:")
    st.write(response['book_name'])
    
    st.subheader("Book Summary:")
    st.write(response['summary'])
