import streamlit as st
from controllers.translator_controller import run_translator

def main():
    st.set_page_config(page_title="Real-Time Translator", layout="centered")
    run_translator()

if __name__ == "__main__":
    main()
