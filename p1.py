import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def nrzl(signal):
    signal.append(signal[-1])
    newsignal = [-1 if item == 0 else item for item in signal]
    print("Orignal signal: ",signal)
    print("Encoded signal: ",newsignal)
    plot(signal,newsignal)
    return newsignal


def nrzi(signal):
    signal.append(signal[-1])
    encoded_data = [1]
    for bit in signal:
        if bit == 0:
            encoded_data.append(encoded_data[-1])
        else:
            encoded_data.append(1-encoded_data[-1])
    encoded_data = [-1 if item == 0 else item for item in encoded_data]
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data[1:])
    plot(signal,encoded_data[1:])
    return encoded_data


def manchester(signal):
    encoded_data = []
    for bit in signal:
        encoded_data.extend([-1,1] if bit==1 else [1,-1])
    encoded_data.append(encoded_data[-1])    
    plot(encoded_data,encoded_data)
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data)
    return encoded_data


def diffmanch(signal):
    encoded_data = []
    encoded_data.extend([-1,1] if signal[0]==1 else [1,-1])
    for i,bit in enumerate(signal[1:]):
        if bit == 0:
            encoded_data.extend([encoded_data[(i*2)],encoded_data[(i*2)+1]])
        else:
            encoded_data.extend([encoded_data[(i*2)+1],encoded_data[(i*2)]])           
    plot(encoded_data, encoded_data)
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data)
    return encoded_data


def ami(signal):
    previous_nonzero = -1
    encoded_data = []
    for bit in signal:
        if bit == 0:
            encoded_data.append(0)
        else:
            if previous_nonzero == 1:
                encoded_data.append(-1)
                previous_nonzero=-1
            else:
                encoded_data.append(1)
                previous_nonzero=1
    print(encoded_data)
    plot(encoded_data,encoded_data)
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data)
    return encoded_data


def eight_zero(signal):
    counter = 0
    encoded_data = []
    for i in range (0,len(signal)):
        if signal[i]==0:
            counter +=1
            encoded_data.append(signal[i])
            if counter == 8:
                encoded_data[-5] = 'V'
                encoded_data[-4] = 'B'
                encoded_data[-2] = 'V'
                encoded_data[-1] = 'B'
                counter = 0
        else:
            counter = 0
            encoded_data.append(signal[i])
    previous_nonzero = -1
    encode = []
    for bit in encoded_data:
        if bit == 1:
            previous_nonzero = -previous_nonzero
            encode.append(previous_nonzero)
        elif bit == 0:
            encode.append(bit)
        elif bit == 'V':
            encode.append(previous_nonzero)
            previous_nonzero = -previous_nonzero
        else:
            encode.append(previous_nonzero)
    encode.append(encode[-1])
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data)
    plot(encode,encode)
    return encoded_data
            
            
def four_zero(signal):
    counter_0 = 0
    counter_1 = 0
    encoded_data = []
    for i in range (0,len(signal)):
        if signal[i] == 0:
            counter_0 +=1
            encoded_data.append(signal[i])
            if counter_0 == 4:
                if counter_1 % 2 ==0:
                    encoded_data[-4] = 'B'
                    encoded_data[-1] = 'V'
                else:
                    encoded_data[-1] = 'V'
                counter_1 = 0
                counter_0 = 0
        elif signal[i] == 1:
            counter_0 = 0
            counter_1 += 1
            encoded_data.append(signal[i])
        else:
            counter_0 = 0
            encoded_data.append(signal[i])
    previous_nonzero = -1
    encode = []
    for bit in encoded_data:
        if bit == 1:
            previous_nonzero = -previous_nonzero
            encode.append(previous_nonzero)
        elif bit == 0:
            encode.append(bit)
        elif bit == 'V':
            encode.append(previous_nonzero)
        else:
            encode.append(-previous_nonzero)
    encode.append(encode[-1])
    print("Orignal signal: ",signal)
    print("Encoded signal: ",encoded_data)
    plot(encode,encode)
    return encoded_data
    
                
def plot(data_sequence,encoded_data):
    df = pd.DataFrame({'Time': range(len(data_sequence)), 'Voltage Level': encoded_data})
    sns.lineplot(x='Time', y='Voltage Level', drawstyle='steps-post', marker='o', data=df)
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(data_sequence)-1)
    plt.grid()  
    plt.ylabel('Voltage Level')
    plt.title('Encoding Plot')
    plt.show()
    
    
def sig(x):
    signal = []
    for i in range (0,x):
        a = int(input("enter the bit"))
        signal.append(a)
    return signal

ch = 'yes'
while ch == "yes":
    a = input("You want to convert a digital signal or an analog signal")
    n = int(input("enter the number of bits: "))
    signal = sig(n)
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
            x = input("scrambler needed? (yes/no): ")
            if x.lower()=="yes":
                x1 = int(input("which scrambler (8/4): "))
                if x1==8:
                    eight_zero(signal)
                else:
                    four_zero(signal)
            else:
                ami(signal)
        else:
            print("enter correct technique")
    else:
        print("enter correct signal")
    ch = input("want to do more encoding (yes/no):")
