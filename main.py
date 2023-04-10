import speech_recognition as sr


def main():
    sound = 'opname.wav'

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Geluid wordt verwerkt...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="nl-NL")
            print(text)

        except Exception as e:
            print(e)
            print("Geluid is niet herkend.")


if __name__ == "__main__":
    main()