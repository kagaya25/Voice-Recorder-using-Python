import sounddevice as sd
from scipy.io.wavfile import write
duration = 10.5  # seconds
fs = 68451 #bitrate
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
print("Recording")
sd.wait()
print("End Recording")
write("output.wav",fs,myrecording)