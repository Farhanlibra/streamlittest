

import streamlit as st





def main():
    st.set_page_config(page_title="my app") 
    
    st.header("ask your pdf")
    st.button("test")

    pdf= st.file_uploader("upload your PDF", type="pdf")

    
    

    if __name__ == '__main__':
        main()