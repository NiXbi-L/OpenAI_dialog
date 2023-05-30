from pydub import AudioSegment
def Convert():
    # загружаем файл голосового сообщения (формат .ogg)
    ogg_file = AudioSegment.from_file("voice.ogg", format="ogg")

    # экспортируем файл голосового сообщения в формат .wav
    wav_file = ogg_file.export("voice.wav", format="wav")