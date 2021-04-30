from gtts import gTTS
from pydub import AudioSegment, playback
import os


def text_to_speech(speech):
    tts = gTTS(speech, lang="en")
    tts.save("voice.mp3")
    audio = AudioSegment.from_mp3("voice.mp3")
    playback.play(audio)
    os.remove("voice.mp3")
