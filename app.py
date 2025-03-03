

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader




def main():
    load_dotenv()
    st.write("welcome")
    st.header("ask your pdf")
    st.button("test")
    pdf = st.file_uploader("upload pdf", type="pdf")
    
    if pdf is not None:
          pdf_reader=PdfReader(pdf)
          text=""
          for page in pdf_reader.pages:
                text+=page.extract_text()
                st.write(text)

    userquestion= st.text_input("ask a question")
    


if __name__ == '__main__':
        main()
