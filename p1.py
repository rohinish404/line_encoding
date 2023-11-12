import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def nrzl(signal):
    signal.append(signal[-1])
    new_signal = [-1 if item == 0 else item for item in signal]
    plot(signal,new_signal)
    return signal


def nrzi(signal):
    signal.append(signal[-1])
    encoded_data = [1]
    for bit in signal:
        if bit == 0:
            encoded_data.append(encoded_data[-1])
        else:
            encoded_data.append(1-encoded_data[-1])
    encoded_data = [-1 if item == 0 else item for item in encoded_data]
    plot(signal,encoded_data[1:])
    return encoded_data


def manchester(signal):
    encoded_data = []
    for bit in signal:
        encoded_data.extend([-1,1] if bit==1 else [1,-1])
    encoded_data.append(encoded_data[-1])    
    plot(encoded_data,encoded_data)
    return encoded_data

def swap(my_array):
    return [my_array[1], my_array[0]]

def diffmanch(signal):
    encoded_data = []
    encoded_data.extend([-1,1] if signal[0]==1 else [1,-1])
    # last_bit = signal[0]  
    for i,bit in enumerate(signal[1:]):
        if bit == 0:
            print("bit=0")
            print(encoded_data[i:i+2])
            encoded_data.extend(encoded_data[i:i+2])
        else:
            print("bit=1")
            print([encoded_data[i+1], encoded_data[i]])
            encoded_data.extend([encoded_data[i+1], encoded_data[i]])
        i+=1
        # last_bit = bit
    plot(encoded_data, encoded_data)
    return encoded_data


def plot(data_sequence,encoded_data):
    df = pd.DataFrame({'Time': range(len(data_sequence)), 'Voltage Level': encoded_data})

    print(df)
    sns.lineplot(x='Time', y='Voltage Level', drawstyle='steps-post', marker='o', data=df)
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(data_sequence)-1)
    plt.grid()  
    plt.ylabel('Voltage Level')
    plt.title('Encoding Plot')
    plt.show()


a = input("You want to convert a digital signal or an analog signal")
signal = [1,0,1,0,1]
if a.lower() == "digital":
    b=input("what type of encoding you want (NRZ-L, NRZ-I,Manchester, Differential Manchester, AMI): ")
    if b.lower() == "nrz-i":
        nrzi(signal)
    elif b.lower() == "nrz-l":
        nrzl(signal)
    elif b.lower() == "manchester":
        manchester(signal)
    elif b.lower() == "differential manchester":
        diffmanch(signal)
    elif b.lower() == "ami":
        print("ami")
    else:
        print("enter correct twechnique")
else:
    print("enter correct signal")
    
