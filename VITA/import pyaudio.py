import pyaudio
import wave
import os
import speech_recognition as sr

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

r = sr.Recognizer()

# Abrir o arquivo de áudio gravado
with sr.AudioFile("C:/Users/gueve/Music/audio_py/" + nome_arquivo + ".wav") as source:
    audio_data = r.record(source)

    # Transcrever o áudio usando o Google Speech Recognition
    text = r.recognize_google(audio_data, language='pt-BR')

    # Imprimir o texto transcritos
    print(text)

print("Arquivo de áudio salvo como:", nome_arquivo + ".wav")
print(os.getcwd())
