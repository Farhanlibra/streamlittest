

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS



def main():
    load_dotenv()
    st.write("welcome")
    st.header("ask your pdf")
    st.button("test")
    pdf = st.file_uploader("upload pdf", type="pdf")
    
    if pdf is not None:
        pdf_reader=PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text +=page.extract_text()
            st.write(text)

    
#convert text into chunks
    text_spliter=CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks=text_spliter.split_documents(text)
    st.write(chunks)

#embeddings

    embeddings=OpenAIEmbeddings()
    knowledgebase=FAISS.from_texts(chunks, embeddings)
    
    userquestion= st.text_input("ask a question")
    
    if userquestion:
        docs = knowledgebase.similarity_search(userquestion)

if __name__ == '__main__':
     main()
