import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

def generate_signal(t, frequencies, amplitudes):
    signal = np.zeros_like(t)
    for freq, amp in zip(frequencies, amplitudes):
        signal += amp * np.sin(2 * np.pi * freq * t)
    return signal

def add_noise(signal, noise_level):
    noise = noise_level * np.random.normal(size=signal.shape)
    return signal + noise

def perform_fft(signal):
    return fft(signal)

def perform_ifft(signal):
    return ifft(signal)

def filter_frequencies(fft_signal, cutoff_freq, sampling_rate):
    freqs = np.fft.fftfreq(len(fft_signal), d=1/sampling_rate)
    filter_mask = np.abs(freqs) < cutoff_freq
    filtered_fft = fft_signal * filter_mask
    return filtered_fft

sampling_rate = 1000
t = np.linspace(0, 1, sampling_rate, endpoint=False)
frequencies = [50, 120, 200]
amplitudes = [1, 0.5, 0.3]
noise_level = 0.2
cutoff_freq = 100

original_signal = generate_signal(t, frequencies, amplitudes)
noisy_signal = add_noise(original_signal, noise_level)

fft_signal = perform_fft(noisy_signal)
filtered_fft = filter_frequencies(fft_signal, cutoff_freq, sampling_rate)
reconstructed_signal = perform_ifft(filtered_fft)

plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(t, original_signal, label='Sinal Original')
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, label='Sinal com Ruído', color='orange')
plt.title('Sinal com Ruído')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, reconstructed_signal, label='Sinal Reconstruído', color='green')
plt.title('Sinal Reconstruído')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
