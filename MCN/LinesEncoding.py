import matplotlib.pyplot as plt

def create_waveform(levels, bit_duration=1):
    time = []
    signal = []
    t = 0
    for level in levels:
        time.extend([t, t + bit_duration])
        signal.extend([level, level])
        t += bit_duration
    return time, signal

def add_bit_labels(data, bit_duration):
    for i, bit in enumerate(data):
        plt.text(i * bit_duration + bit_duration / 2, 1.25, bit, ha = 'center')

def plot_waveform(time, signal, title, data, bit_duration):
    plt.figure()
    plt.step(time, signal, where='post')
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Voltage Level")
    plt.ylim(-1.5, 1.5)
    plt.grid()
    add_bit_labels(data, bit_duration)
    plt.show()

def rz_unipolar(data):
    levels = []
    for bit in data:
        if bit == '1':
            levels.extend([1, 0])
        else:
            levels.extend([0, 0])
    return create_waveform(levels, 0.5), 1

def nrz_l(data):
    levels = []
    for bit in data:
        if bit == '1':
            levels.append(-1)
        else:
            levels.append(1)
    return create_waveform(levels), 1

def nrz_i(data):
    levels = []
    level = 1
    for bit in data:
        if bit == '1':
            level = -level
        levels.append(level)
    return create_waveform(levels), 1

def manchester(data):
    levels = []
    for bit in data:
        if bit == '1':
            levels.extend([-1, 1])
        else:
            levels.extend([1, -1])
    return create_waveform(levels, 0.5), 1

def diff_manchester(data):
    levels = []
    level = -1
    for bit in data:
        if bit == '0':
            level = -level
        levels.append(level)
        level = -level
        levels.append(level)
    return create_waveform(levels, 0.5), 1

def ami(data):
    levels = []
    level = -1
    for bit in data:
        if bit == '1':
            level = -level
            levels.append(level)
        else:
            levels.append(0)
    return create_waveform(levels), 1

def pseudoternary(data):
    levels = []
    level = -1
    for bit in data:
        if bit == '0':
            level = -level
            levels.append(level)
        else:
            levels.append(0)
    return create_waveform(levels), 1

def get_data_bits():
    return input("\nEnter binary data: ")

if __name__ == "__main__":
    while True:
        print("\nLine Encoding Schemes:")
        print("\n1. RZ-Unipolar")
        print("2. NRZ-L")
        print("3. NRZ-I")
        print("4. Manchester")
        print("5. Differential Manchester")
        print("6. AMI")
        print("7. Pseudoternary")
        print("8. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            data = get_data_bits()
            (t, s), bd = rz_unipolar(data)
            plot_waveform(t, s, "RZ-Unipolar Encoding", data, bd)

        elif choice == 2:
            data = get_data_bits()
            (t, s), bd = nrz_l(data)
            plot_waveform(t, s, "NRZ-L Encoding", data, bd)

        elif choice == 3:
            data = get_data_bits()
            (t, s), bd = nrz_i(data)
            plot_waveform(t, s, "NRZ-I Encoding", data, bd)

        elif choice == 4:
            data = get_data_bits()
            (t, s), bd = manchester(data)
            plot_waveform(t, s, "Manchester Encoding", data, bd)

        elif choice == 5:
            data = get_data_bits()
            (t, s), bd = diff_manchester(data)
            plot_waveform(t, s, "Differential Manchester Encoding", data, bd)

        elif choice == 6:
            data = get_data_bits()
            (t, s), bd = ami(data)
            plot_waveform(t, s, "AMI Encoding", data, bd)

        elif choice == 7:
            data = get_data_bits()
            (t, s), bd = pseudoternary(data)
            plot_waveform(t, s, "Pseudoternary Encoding", data, bd)

        elif choice == 8:
            break

        else:
            print("Invalid choice")