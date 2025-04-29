from gtts import gTTS
import pygame
import os

def speak_text(text, language):
    tts = gTTS(text=text, lang=language)
    filename = "temp_audio.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(filename)
