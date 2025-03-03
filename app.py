

import streamlit as st
from dotenv import load_dotenv




def main():
    load_dotenv()
    st.write("welcome")
    st.header("ask your pdf")
    st.button("test")
    pdf = st.file_uploader("upload pdf", type="pdf")
    
    if pdf is not None:
          pdf_reader=pdf_reader(pdf)
          text=""
          for page in pdf_reader.pages:
                text+=page.extract_text()
                st.write(text)

    

if __name__ == '__main__':
        main()
