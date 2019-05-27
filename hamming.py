import math


def no_of_hamming_bits(data_length):
    r = 1
    while 2**r < data_length + r +1:
        r +=1
    return r

def generate_message(data,r):
    x = []
    c = 0
    j = 0
    for i in range(1,len(data)+r+1):
        if i == (2**c):
            x.append(0)
            c = c + 1

        else:
            x.append(int(data[j]))
            j = j + 1
    return x


def encode(data,r):
    c = 0
    for i in range(1,len(data)+1):
        if i == (2**c):
            index = i-1
            j = index
            x = []

            while j<len(data):
                x.extend(data[j:j+(2**c)])
                j = j+ 2**(c+1)
            data[index] = sum(x)%2

            c = c+1
    a = ""
    for i in data[::-1]:
        a = a + str(i)

    return a
                
def hamming(data):
    r = no_of_hamming_bits(len(data))
    x = generate_message(data[::-1],r)
    ans = encode(x,r)
    return ans
    


if __name__ == "__main__":
    data = input("Enter binary data:")
    print("Hamming code: ",hamming(data))
