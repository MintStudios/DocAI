import config
import tts
import searchdoc
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


def adjust_mic():
    with m as source:
        r.adjust_for_ambient_noise(source)


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
            if config.current_lang != "" and config.current_objective != "":
                tts.text_to_speech(
                    f"Pulling up {config.current_objective} in the {config.current_lang} documentation"
                )
                searchdoc.search()
                config.current_objective = ""
                config.current_lang = ""

        except sr.UnknownValueError:
            print("Doc could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Doc service; {0}".format(e))

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=limit)
