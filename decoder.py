import matplotlib.pyplot as plt

def nrzl(encoded):
    signal = [0 if item == -1 else item for item in encoded]
    print("enoded signal recived: ",encoded)
    print("orignal signal: ",signal)
    return signal


def nrzi(encoded):
    encoded =  [0 if item == -1 else item for item in encoded]
    signal = []
    if encoded[0]==1:
        signal.append(0)
    else: 
        signal.append(1)
    for i in range(1,len(encoded)):
        if encoded[i] == encoded[i-1]:
            signal.append(0)
        else:
            signal.append(1)
    print("enoded signal recived: ",encoded)
    print("orignal signal: ",signal)
    return signal 


def manchester(encoded):
    signal = []
    for i in range(0,len(encoded)-2,2):
        if (encoded[i],encoded[i+1]) == (-1,1):
            signal.append(1)
        else:
            signal.append(0)
    print("enoded signal recived: ",encoded)
    print("orignal signal: ",signal)
    return signal 
