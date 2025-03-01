

import streamlit as st
from pypdf import PdfReader




def main():
    st.set_page_config(page_title="my app") 
    
    st.header("ask your pdf")
    st.button("test")

    pdf= st.file_uploader("upload your PDF", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text=""
        for page in pdf_reader.pages:
            text += page.extract_text()
    

    if __name__ == '__main__':
        main()