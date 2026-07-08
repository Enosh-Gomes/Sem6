def format_with_spaces(text, delimiters=None):
	if delimiters is None:
		delimiters = ["FLAG", "ESC", "VV"]
	result = []
	i = 0
	while i < len(text):
		matched = False
		for delim in delimiters:
			if text[i:i+len(delim)] == delim:
				result.append(delim)
				i += len(delim)
				matched = True
				break
		if not matched:
			result.append(text[i])
			i += 1
	return " ".join(result)

def character_count_framing(data, total_frame_size=5):
	if total_frame_size <= 1:
		raise ValueError("total_frame_size must be greater than 1")
	payload_size = total_frame_size - 1
	frames = []
	for i in range(0, len(data), payload_size):
		payload = data[i:i + payload_size]
		count = len(payload) + 1
		frame = "[" + str(count) + "]" + "".join(f"[{ch}]" for ch in payload)
		frames.append(frame)
	return frames

def byte_stuffing(data, flag="FLAG", esc="ESC"):
	stuffed_data = data.replace(esc, esc + esc).replace(flag, esc + flag)
	return f"{flag}{stuffed_data}{flag}"

def bit_stuffing(data_bits, flag="01111110"):
	if any(bit not in "01" for bit in data_bits):
		raise ValueError("Bit stuffing input must contain only 0 and 1")
	stuffed = []
	one_count = 0
	for bit in data_bits:
		stuffed.append(bit)
		if bit == "1":
			one_count += 1
			if one_count == 5:
				stuffed.append("0")
				one_count = 0
		else:
			one_count = 0
	return f"{flag}{''.join(stuffed)}{flag}"

def physical_layer_violation(data_bits, start_symbol="VV", end_symbol="VV"):
	if any(bit not in "01" for bit in data_bits):
		raise ValueError("Physical layer violation input must contain only 0 and 1")
	return f"{start_symbol}{data_bits}{end_symbol}"

def main():
	while True:
		print("\n=== Framing Methods Menu ===")
		print("1. Character Count")
		print("2. Byte Stuffing")
		print("3. Bit Stuffing")
		print("4. Physical Layer Violation")
		print("5. Exit")
		choice = input("Enter your choice (1-5): ").strip()
		if choice == "1":
			data = input("Enter text data: ")
			size = int(input("Enter total frame size (including count, e.g., 5): "))
			frames = character_count_framing(data, size)
			print("\n" + "="*50)
			print("Character Count Frames:")
			print("="*50)
			for idx, frame in enumerate(frames, start=1):
				print(f"\nFrame {idx}:")
				print(f"  {frame}")
			print("\nReceiver rule: read first count C, then read next C-1 characters.")
			print("="*50)
		elif choice == "2":
			data = input("Enter text data: ")
			framed = byte_stuffing(data)
			formatted = format_with_spaces(framed, ["FLAG", "ESC"])
			print("\n" + "="*60)
			print("Byte Stuffed Frame:")
			print("="*60)
			print(f"\nOriginal data:     {data}")
			print(f"\nByte stuffed:      {framed}")
			print(f"\nWith spaces:       {formatted}")
			print(f"\nFrame structure:   [FLAG] + [stuffed data] + [FLAG]")
			print("="*60)
		elif choice == "3":
			bits = input("Enter bit data (0/1): ").strip()
			framed = bit_stuffing(bits)
			formatted = format_with_spaces(framed, ["0", "1"])
			print("\n" + "="*60)
			print("Bit Stuffing Frame:")
			print("="*60)
			print(f"\nOriginal bits:     {bits}")
			print(f"\nBit stuffed:       {framed}")
			print(f"\nWith spaces:       {formatted}")
			print(f"\nFrame structure:   [01111110] + [stuffed bits] + [01111110]")
			print("="*60)
		elif choice == "4":
			bits = input("Enter bit data (0/1): ").strip()
			framed = physical_layer_violation(bits)
			formatted = format_with_spaces(framed, ["VV"])
			print("\n" + "="*60)
			print("Physical Layer Violation Frame:")
			print("="*60)
			print(f"\nOriginal bits:     {bits}")
			print(f"\nFramed output:     {framed}")
			print(f"\nWith spaces:       {formatted}")
			print(f"\nFrame structure:   [VV] + [data] + [VV]")
			print("="*60)
		elif choice == "5":
			print("Exiting...")
			break
		else:
			print("Invalid choice. Please enter 1 to 5.")

if __name__ == "__main__":
	main()