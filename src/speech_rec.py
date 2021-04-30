import speech_recognition as sr

WIT_AI_KEY = ""

try:
    import apikeys

    WIT_AI_KEY = apikeys.WIT_AI_KEY
except ModuleNotFoundError as e:
    print("Try inserting a wit.ai key.")

m = sr.Microphone()
r = sr.Recognizer()


def recognize(m, r):
    """
    Recognizes voice

    Args:
        m (Microphone): SpeechRecognition's Microphone class. Requires PyAudio.
        r (Recognizer): SpeechRecognition's Recognizer class.
    """

    with m as source:
        r.adjust_for_ambient_noise(source)

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))


def background_listening(limit: int):
    """
    Starts background listening.

    Args:
        limit (int): Limit for which the AI stops listening to parse information.
    """
    # Callback for background listening
    def callback(recognizer, audio):
        try:
            print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=limit)

    while True:
        pass
