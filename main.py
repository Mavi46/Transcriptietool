import speech_recognition as sr
import ftplib

ftp_host = "Vraag IP aan Haci"
ftp_user = "Vraag gebruikersnaam aan Haci"
ftp_pass = "Vraag wachtwoord aan Haci"

def ftp_getter():
    # Connect to FTP server
    ftp = ftplib.FTP(ftp_host, ftp_user, ftp_pass)
    # Set the current directory
    ftp.cwd('upload')
    # Download file from FTP server
    with open('downloaded_opname.wav', 'wb') as f:
        ftp.retrbinary('RETR ' + 'opname.wav', f.write)
    transcribe_tool()

def transcribe_tool():
    sound = 'downloaded_opname.wav'

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
    ftp_getter()