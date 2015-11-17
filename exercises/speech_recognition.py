from translations import comparators
import speech_recognition as sr

__author__ = 'daniel'


def recognize_speech_and_compare(audio_file, text_to_compare):
    recognized_text = recognize_speech(audio_file)
    if comparators.texts_difference(text_to_compare, recognized_text) == 0:
        return True
    return False


def recognize_speech(audio_file):
    r = sr.Recognizer()
    audio = r.record(audio_file) # read the entire WAV file

    # recognize speech using Google Speech Recognition
    try:
        # using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))