import speech_recognition as sr

WIT_AI_KEY = ""

try:
    import apikeys

    WIT_AI_KEY = apikeys.WIT_AI_KEY
except ModuleNotFoundError as e:
    print("Try inserting a wit.ai key.")


m = sr.Microphone()
r = sr.Recognizer()


def recognize():
    """
    Tool for recognizing speech using Wit.ai. Needs a key.
    """
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
