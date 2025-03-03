

import streamlit as st





def main():
    
    st.write("welcome")
    st.header("ask your pdf")
    st.button("test")

    pdf= st.file_uploader("upload your PDF", type="pdf")

    
    

    if __name__ == '__main__':
        main()