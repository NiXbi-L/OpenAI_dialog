import speech_recognition as sr

from Converter import Convert

def Recognition():
    Convert()
    # создаем объект для распознавания речи
    r = sr.Recognizer()

    # указываем файл для распознавания речи
    audio_file = sr.AudioFile("voice.wav")

    # открываем файл с помощью объекта sr.AudioFile
    with audio_file as source:

        # записываем звук из файла в объект AudioData
        audio = r.record(source)

    try:
        # используем Google Speech Recognition для распознавания речи
        text = r.recognize_google(audio, language="ru-RU")

        # выводим распознанный текст
        return text

    except sr.UnknownValueError:
        return "Не удалось распознать речь"

    except sr.RequestError as e:
        return "Не удалось получить ответ от сервиса распознавания речи; {0}".format(e)