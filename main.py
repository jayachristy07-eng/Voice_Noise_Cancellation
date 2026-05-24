import sounddevice as sd
import numpy as np
import noisereduce as nr
import soundfile as sf
import matplotlib.pyplot as plt
print("====== Noise Cancellation System ======")
print("1. Real-Time Microphone Noise Cancellation")
print("2. Saved Audio File Noise Cancellation")
choice = input("Enter your choice (1 or 2): ")
# =========================================
# REAL-TIME MICROPHONE NOISE CANCELLATION
# =========================================
if choice == "1":
    samplerate = 44100
    duration = 5
    print("Recording... Speak now")
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    print("Recording completed")
    # Convert to 1D array
    audio_data = audio.flatten()
    # Noise reduction
    clean_audio = nr.reduce_noise(
        y=audio_data,
        sr=samplerate
    )
    # Save cleaned audio
    filename_output = input("Enter output filename: ")
    sf.write(filename_output + ".wav", clean_audio, samplerate)
    print("Clean audio saved as realtime_clean.wav")
    # Plot original waveform
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(audio_data)
    plt.title("Original Audio Waveform")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    # Plot cleaned waveform
    plt.subplot(2, 1, 2)
    plt.plot(clean_audio)
    plt.title("Noise Reduced Audio Waveform")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
# =========================================
# SAVED AUDIO FILE NOISE CANCELLATION
# =========================================
elif choice == "2":
    filename = input("Enter audio filename (example: input.wav): ")
    # Read audio file
    data, rate = sf.read(filename)
    # Convert stereo to mono if needed
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    # Noise reduction
    clean_audio = nr.reduce_noise(
        y=data,
        sr=rate
    )
    # Save cleaned audio
    filename_output = input("Enter output filename: ")
    sf.write(filename_output + ".wav", clean_audio, samplerate= 44100)
    print("Clean audio saved as file_clean.wav")
    # Plot original waveform
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(data)
    plt.title("Original Audio Waveform")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    # Plot cleaned waveform
    plt.subplot(2, 1, 2)
    plt.plot(clean_audio)
    plt.title("Noise Reduced Audio Waveform")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
else:
    print("Invalid choice")