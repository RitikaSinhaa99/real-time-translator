from models.speech_model import recognize_speech
from models.translation_model import translate_text
from models.tts_model import speak_text
from views.translator_view import build_ui, display_translation

def run_translator():
    record, source_lang, target_lang = build_ui()

    if record:
        original_text = recognize_speech()
        translated_text = translate_text(original_text, target_lang)
        
        display_translation(original_text, translated_text)
        speak_text(translated_text, target_lang)
