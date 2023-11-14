import numpy as np
import matplotlib.pyplot as plt

def pcm_encode(signal, quantization_bits):
    quantization_levels = 2 ** quantization_bits - 1
    quantization_step = 2 / quantization_levels

    quantized_signal = np.round(signal / quantization_step) * quantization_step

    digital_values = ((quantized_signal + 1) / 2 * quantization_levels).astype(int)

    return digital_values

def pcm_decode(digital_values, quantization_bits):
    quantization_levels = 2 ** quantization_bits - 1

    quantization_step = 2 / quantization_levels

    reconstructed_signal = (digital_values / quantization_levels - 0.5) * 2 * quantization_step
    

    return reconstructed_signal


t = np.linspace(0, 1, 1000, endpoint=False)  
analog_signal = np.sin(2 * np.pi * 5 * t)  


quantization_bits = 2
digital_values = pcm_encode(analog_signal, quantization_bits)


print("Digital Values after PCM encoding:")
print(digital_values)  


reconstructed_signal = pcm_decode(digital_values, quantization_bits)
print(reconstructed_signal)

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, analog_signal, label='Analog Signal')
plt.title('Original Analog Signal')
plt.legend()

plt.subplot(2, 1, 2)
plt.stem(t, digital_values.flatten(), markerfmt='C1o', basefmt='C0-', label='Digital Values')
plt.title('PCM Encoded Digital Values')
plt.legend()

plt.tight_layout()
plt.show()
