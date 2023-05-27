import pyaudio
import wave


class AudioPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.chunk = 1024

    def play(self):
        wf = wave.open(self.file_path, 'rb')
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
        data = wf.readframes(self.chunk)
        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)

        stream.stop_stream()
        stream.close()
        audio.terminate()


file_path = "melodiya.wav"
player = AudioPlayer(file_path)
