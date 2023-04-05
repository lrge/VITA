import pyaudio
import wave
import os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

class CaptadorDeTexto:
    def getTexto(self):
        # Solicitar a duração da gravação em segundos
        duracao = int(input("Digite a duração da gravação em segundos: "))

        # Solicitar o nome do arquivo de áudio a ser salvo
        nome_arquivo = input("Digite o nome do arquivo de áudio a ser salvo: ")

        # Definir as configurações da gravação
        CHUNK = 1024
        FORMATO = pyaudio.paInt16
        CANAL = 1
        TAXA_DE_AMOSTRAGEM = 44100

        # Inicializar o objeto PyAudio
        p = pyaudio.PyAudio()

        # Abre o fluxo de áudio do microfone
        stream = p.open(format=FORMATO,
                        channels=CANAL,
                        rate=TAXA_DE_AMOSTRAGEM,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* gravando por", duracao, "segundos...")

        # Gravar o áudio do microfone em um buffer
        frames = []
        for i in range(0, int(TAXA_DE_AMOSTRAGEM / CHUNK * duracao)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* gravação finalizada")

        # Parar o fluxo de áudio
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Salvar a gravação em um arquivo WAV com o nome definido pelo usuário
        wf = wave.open("C:/Users/gueve/Music/audio_py/" + nome_arquivo + ".wav", 'wb')
        wf.setnchannels(CANAL)
        wf.setsampwidth(p.get_sample_size(FORMATO))
        wf.setframerate(TAXA_DE_AMOSTRAGEM)
        wf.writeframes(b''.join(frames))
        wf.close()

        return nome_arquivo

class TranslationFactory:
    def __init__(self):
        self.translator = Translator()
        
    def get(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, msg):
        translated_text = self.translator.translate(msg, src=self.from_lang, dest=self.to_lang).text
        return translated_text

class Sintetizador:
    def Toaudio(self, texto):
        tts = gTTS(texto)
        return tts.get_wav_data()

# Capturar o áudio do usuário
captador = CaptadorDeTexto()
nome_arquivo = captador.getTexto()

# Traduzir o áudio para o inglês
factory = TranslationFactory()
factory.get("pt", "en")

with sr.AudioFile("C:/Users/gueve/Music/audio_py/" + nome_arquivo + ".wav") as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language='pt-BR')

    translated_text = factory.translate(text)

# Sintetizar a fala traduzida em áudio
sintetizador = Sintetizador()
samples = sintetizador.Toaudio(translated_text)

# Sintetizar o texto em áudio
audio_generator = synthesize_text(text)

# Salvar o áudio gerado em um arquivo WAV com o nome definido pelo usuário
wf = wave.open("C:/Users/gueve/Music/audio_py/" + nome_arquivo + "_synthesized.wav", 'wb')
wf.setnchannels(1)
wf.setsampwidth(2)
wf.setframerate(44100)
wf.writeframes(b''.join(audio_generator))
wf.close()

print("Arquivo de áudio sintetizado e salvo como:", nome_arquivo + "_synthesized.wav")
print(os.getcwd())

