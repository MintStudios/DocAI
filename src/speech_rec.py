import config
import parse
import speech_recognition as sr

WIT_AI_KEY = ""

try:
    import apikeys

    WIT_AI_KEY = apikeys.WIT_AI_KEY
except ModuleNotFoundError as e:
    print("Try inserting a wit.ai key.")

m = sr.Microphone()
r = sr.Recognizer()


def recognize(microphone: sr.Microphone, recognizer: sr.Recognizer):
    """
    Recognizes voice

    Args:
        m (Microphone): SpeechRecognition's Microphone class. Requires PyAudio.
        r (Recognizer): SpeechRecognition's Recognizer class.
    """

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    with microphone as source:
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        config.current_line = recognizer.recognize_wit(audio, key=WIT_AI_KEY)
        print("Doc thinks you said " + config.current_line)
    except sr.UnknownValueError:
        print("Doc could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Doc service; {0}".format(e))


def background_listening(limit: int):
    """
    Starts background listening.

    Args:
        limit (int): Limit for which the AI stops listening to parse information.
    """
    # Callback for background listening
    def callback(recognizer, audio):
        try:
            config.current_line = r.recognize_wit(audio, key=WIT_AI_KEY)
            parse.parse()
            print("Doc thinks you said " + config.current_line)
        except sr.UnknownValueError:
            print("Doc could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Doc service; {0}".format(e))

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=limit)
