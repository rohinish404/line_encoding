import encoder
import decoder
import analog
import numpy as np

ch = 'yes'
while ch == "yes":
    w = input("You want to encode or decode: ")
    if w.lower() == "encode":
        a = input("You want to convert a digital signal or an analog signal: ")
        if a.lower() == "digital":
            n = int(input("enter the number of bits: "))
            signal = encoder.sig(n)
            b=input("what type of encoding you want (NRZ-L, NRZ-I,Manchester, Differential Manchester, AMI): ")
            if b.lower() == "nrz-i":
                encoder.nrzi(signal)
            elif b.lower() == "nrz-l":
                encoder.nrzl(signal)
            elif b.lower() == "manchester":
                encoder.manchester(signal)
            elif b.lower() == "differential manchester":
                encoder.diffmanch(signal)
            elif b.lower() == "ami":
                x = input("scrambler needed? (yes/no): ")
                if x.lower()=="yes":
                    x1 = int(input("which scrambler (8/4): "))
                    if x1==8:
                        encoder.eight_zero(signal)
                    else:
                        encoder.four_zero(signal)
                else:
                    encoder.ami(signal)
            else:
                print("enter correct technique")
        elif a.lower() == 'analog':
            t = np.linspace(0, 1, 1000, endpoint=False)
            analog_signal = np.sin(2 * np.pi * 5 * t)  
            quantization_bits = 2
            digital_values = analog.pcm_encode(analog_signal, quantization_bits)
        else:
            print("enter correct signal")
    elif w.lower() == "decode":
        n = int(input("enter the number of bits: "))
        signal = encoder.sig(n)
        b=input("what type of decoding you want (NRZ-L, NRZ-I,Manchester): ")
        if b.lower() == "nrz-i":
            decoder.nrzi(signal)
        elif b.lower() == "nrz-l":
            decoder.nrzl(signal)
        elif b.lower() == "manchester":
            decoder.manchester(signal)
    ch = input("want to do more encoding (yes/no):")

        
