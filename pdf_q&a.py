import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key=os.getenv("GOOGLE_GEMINI_API_KEY")

import google.generativeai as genai
genai.configure(api_key=gemini_api_key)


st.set_page_config(page_title="📄 PDF Q&A")
st.title("📄 Chat with your PDF")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
st.subheader("Ask the question")
user_question = st.text_input("Enter your question")

pdf=PdfReader(uploaded_file)

from typing_extensions import Concatenate

#extracting text
raw_text=''
for i,pages in enumerate(pdf.pages):
  content=pages.extract_text()
  if content:
    raw_text+=content

#splitting text
text_splitter=CharacterTextSplitter(
    separator='\n',
    chunk_size=500,
    chunk_overlap=100,
    length_function=len
)
text=text_splitter.split_text(raw_text)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=gemini_api_key)

document_search=FAISS.from_texts(text,embeddings)

from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=gemini_api_key,
)
chain=load_qa_chain(model,chain_type='stuff')

docs=document_search.similarity_search(user_question)
result=chain.invoke({"input_documents":docs,"question":user_question})
st.write("Answer")
st.write(result["output_text"])

