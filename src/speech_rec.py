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
r.dynamic_energy_threshold = True

doc_pronunciations = ["doc", "dark", "dog", "start", "block", "duck"]


def adjust_mic():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)


def recognize():

    adjust_mic()
    config.current_line = ""
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=7)
        print("listening")

    try:
        print("trying")
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
            config.is_active = False
        if config.current_line != "" and (
            config.current_lang != "" or config.current_objective != ""
        ):
            tts.text_to_speech("Could you repeat that?")
    except sr.UnknownValueError:
        print("Doc could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Doc; {0}".format(e))


def background_listening(limit: int):
    # Callback for background listening
    def callback(recognizer, audio):
        try:
            config.current_line = r.recognize_wit(audio, key=WIT_AI_KEY)
            print(config.current_line)
            for pronunciation in doc_pronunciations:
                if pronunciation in config.current_line:
                    config.is_active = True
                    print("Hi! -  " + config.current_line)
                    stop(stop_listening)
                    break
        except sr.UnknownValueError:
            print("Doc could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Doc; {0}".format(e))

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=limit)


def stop(listener):
    print("stopping")
    listener(wait_for_stop=False)
