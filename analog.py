import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, endpoint=False) 

def plot(analog_signal,digital_values):
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, analog_signal, label='Analog Signal')
    plt.title('Original Analog Signal')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.stem(t, digital_values.flatten(), markerfmt='C1o', basefmt='C0-', label='Digital Values')
    plt.title('PCM Encoded Digital Values')
    plt.legend()
    plt.tight_layout()
    plt.show()

def pcm_encode(signal, quantization_bits):
    quantization_levels = 2 ** quantization_bits - 1
    quantization_step = 2 / quantization_levels
    quantized_signal = np.round(signal / quantization_step) * quantization_step
    digital_values = ((quantized_signal + 1) / 2 * quantization_levels).astype(int)
    plot(signal,digital_values)
    print("Digital Values after PCM encoding:",digital_values)
    return digital_values


 





