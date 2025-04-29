import streamlit as st

# Full Language Name to Language Code Mapping
LANGUAGES = {
    'Afrikaans': 'af',
    'Arabic': 'ar',
    'Bengali': 'bn',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Dutch': 'nl',
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Nepali': 'ne',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Russian': 'ru',
    'Spanish': 'es',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Urdu': 'ur',
    'Vietnamese': 'vi'
}

def build_ui():
    set_background_local("images/rail1.avif")
    
    st.title(" Real-Time Annoucement Translator")
    st.write("Speak → Translate → Listen!")

    # Dropdown with full language names
    source_language = st.selectbox("🎤 Select your spoken language:", list(LANGUAGES.keys()))
    target_language = st.selectbox("🌍 Select the language to translate into:", list(LANGUAGES.keys()))
    
    record = st.button("🎙️ Start Recording")

    # Return the selected language codes (not names)
    return record, LANGUAGES[source_language], LANGUAGES[target_language]

def display_translation(original_text, translated_text):
    st.subheader("🔊 Original Speech Recognized:")
    st.info(original_text)
    
    st.subheader("🌍 Translated Text:")
    st.success(translated_text)

def set_background(image_url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{image_url}");
             background-size: cover;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
import base64

def set_background_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()

    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
