import reedsolo

def normalize_bits(bit_string):
	bit_string = bit_string.strip().replace(" ", "")
	if bit_string == "" or any(ch not in "01" for ch in bit_string):
		raise ValueError("Input must contain only 0 and 1.")
	return bit_string

def group_bits(bit_string, size=8):
	return " ".join(bit_string[i:i + size] for i in range(0, len(bit_string), size))

def parity_bit_method(data_bits, parity_type="even"):
	data_bits = normalize_bits(data_bits)
	ones_count = data_bits.count("1")
	if parity_type == "even":
		parity = "0" if ones_count % 2 == 0 else "1"
	elif parity_type == "odd":
		parity = "1" if ones_count % 2 == 0 else "0"
	else:
		raise ValueError("parity_type must be 'even' or 'odd'.")
	transmitted = data_bits + parity
	return parity, transmitted

def block_parity_method(data_bits, cols=8):
	data_bits = normalize_bits(data_bits)
	if cols <= 1:
		raise ValueError("cols must be greater than 1.")
	pad_len = (cols - (len(data_bits) % cols)) % cols
	padded = data_bits + ("0" * pad_len)
	rows = [list(padded[i:i + cols]) for i in range(0, len(padded), cols)]
	row_parity_bits = []
	for row in rows:
		row_parity = str(sum(int(b) for b in row) % 2)
		row.append(row_parity)
		row_parity_bits.append(row_parity)
	col_count = cols + 1
	col_parity_row = []
	for c in range(col_count):
		col_sum = sum(int(rows[r][c]) for r in range(len(rows)))
		col_parity_row.append(str(col_sum % 2))
	matrix_lines = [" ".join(row) for row in rows]
	matrix_lines.append("-" * (2 * col_count - 1))
	matrix_lines.append(" ".join(col_parity_row))
	transmitted_stream = "".join("".join(row) for row in rows) + "".join(col_parity_row)
	return {
		"padded_data": padded,
		"pad_len": pad_len,
		"rows_with_parity": rows,
		"column_parity_row": col_parity_row,
		"transmitted_stream": transmitted_stream,
		"stream_group_size": col_count,
		"display": "\n".join(matrix_lines),
	}

def xor_bits(a, b):
	return "".join("0" if x == y else "1" for x, y in zip(a, b))

def crc_remainder(data_bits, polynomial_bits):
	data_bits = normalize_bits(data_bits)
	poly = normalize_bits(polynomial_bits)
	degree = len(poly) - 1
	working = list(data_bits + ("0" * degree))
	for i in range(len(data_bits)):
		if working[i] == "1":
			for j in range(len(poly)):
				working[i + j] = "0" if working[i + j] == poly[j] else "1"
	remainder = "".join(working[-degree:])
	codeword = data_bits + remainder
	return remainder, codeword

def checksum_ones_complement(data_bits, word_size=16):
	data_bits = normalize_bits(data_bits)
	if word_size <= 1:
		raise ValueError("word_size must be greater than 1.")
	if len(data_bits) % word_size != 0:
		pad_len = word_size - (len(data_bits) % word_size)
		data_bits += "0" * pad_len
	else:
		pad_len = 0
	mask = (1 << word_size) - 1
	words = [data_bits[i:i + word_size] for i in range(0, len(data_bits), word_size)]
	running_total = 0
	steps = []
	for idx, word in enumerate(words, start=1):
		word_val = int(word, 2)
		before = running_total
		raw_sum = before + word_val
		folded = (raw_sum & mask) + (raw_sum >> word_size)
		while folded > mask:
			folded = (folded & mask) + (folded >> word_size)
		steps.append(
			{
				"step": idx,
				"before": format(before, f"0{word_size}b"),
				"word": word,
				"raw_sum": format(raw_sum, f"0{word_size + 1}b"),
				"after_fold": format(folded, f"0{word_size}b"),
			}
		)
		running_total = folded
	checksum_val = (~running_total) & mask
	checksum_bits = format(checksum_val, f"0{word_size}b")
	transmitted = data_bits + checksum_bits
	return {
		"padded_data": data_bits,
		"pad_len": pad_len,
		"word_size": word_size,
		"words": words,
		"steps": steps,
		"sum_before_complement": format(running_total, f"0{word_size}b"),
		"checksum": checksum_bits,
		"transmitted": transmitted,
	}

def hamming_encode(data_bits):
	data_bits = normalize_bits(data_bits)
	m = len(data_bits)
	r = 0
	while 2 ** r < (m + r + 1):
		r += 1
	n = m + r
	code = ["0"] * (n + 1)
	j = 0
	for i in range(1, n + 1):
		if (i & (i - 1)) != 0:
			code[i] = data_bits[j]
			j += 1
	for i in range(r):
		p = 2 ** i
		parity = 0
		for k in range(1, n + 1):
			if k & p:
				parity ^= int(code[k])
		code[p] = str(parity)
	return "".join(code[1:])

def hamming_detect_correct(codeword_bits):
	codeword_bits = normalize_bits(codeword_bits)
	n = len(codeword_bits)
	code = ["0"] + list(codeword_bits)
	r = 0
	while 2 ** r <= n:
		r += 1
	error_pos = 0
	for i in range(r):
		p = 2 ** i
		parity = 0
		for k in range(1, n + 1):
			if k & p:
				parity ^= int(code[k])
		if parity != 0:
			error_pos += p
	corrected = code[:]
	if 1 <= error_pos <= n:
		corrected[error_pos] = "1" if corrected[error_pos] == "0" else "0"
	return {
		"error_position": error_pos,
		"corrected_codeword": "".join(corrected[1:]),
	}

def reed_solomon_demo(text, nsym=8):
	codec = reedsolo.RSCodec(nsym)
	encoded = codec.encode(text.encode("utf-8"))
	decoded = codec.decode(encoded)
	decoded_bytes = decoded[0] if isinstance(decoded, tuple) else decoded
	return {
		"encoded_bytes": encoded,
		"decoded_text": decoded_bytes.decode("utf-8"),
		"parity_symbols": nsym,
	}

def print_header(title):
	print("\n" + "=" * 64)
	print(title)
	print("=" * 64)

def main():
	crc_polys = {
		"8": "100000111",
		"16": "11000000000000101",
		"32": "100000100110000010001110110110111",
	}
	while True:
		print("\n=== Experiment 10: Error Detection/Correction Menu ===")
		print("1. Parity Bit Method")
		print("2. Block Parity Bit (2D)")
		print("3. CRC-8 / CRC-16 / CRC-32")
		print("4. Checksum (One's Complement)")
		print("5. Hamming Code")
		print("6. Reed-Solomon Coding Method")
		print("7. Exit")
		choice = input("Enter choice (1-7): ").strip()
		try:
			if choice == "1":
				bits = input("Enter data bits: ")
				ptype = input("Parity type (even/odd): ").strip().lower() or "even"
				parity, transmitted = parity_bit_method(bits, ptype)
				print_header("Parity Bit Method")
				print(f"Data bits        : {group_bits(normalize_bits(bits))}")
				print(f"Parity bit       : {parity}")
				print(f"Transmitted bits : {group_bits(transmitted)}")
			elif choice == "2":
				bits = input("Enter data bits: ")
				cols_text = input("Columns per row (default 8): ").strip()
				cols = int(cols_text) if cols_text else 8
				result = block_parity_method(bits, cols)
				print_header("Block Parity Bit (2D)")
				print(f"Padded data      : {group_bits(result['padded_data'])}")
				print(f"Pad bits added   : {result['pad_len']}")
				print("\nRows with row parity + bottom column parity row:")
				print(result["display"])
				print(
					f"\nTransmitting stream: "
					f"{group_bits(result['transmitted_stream'], result['stream_group_size'])}"
				)
			elif choice == "3":
				bits = input("Enter data bits: ")
				crc_type = input("Choose CRC type (8/16/32): ").strip()
				if crc_type not in crc_polys:
					raise ValueError("CRC type must be 8, 16, or 32.")
				remainder, codeword = crc_remainder(bits, crc_polys[crc_type])
				print_header(f"CRC-{crc_type}")
				print(f"Data bits        : {group_bits(normalize_bits(bits))}")
				print(f"Generator poly   : {crc_polys[crc_type]}")
				print(f"CRC remainder    : {remainder}")
				print(f"Transmitted bits : {group_bits(codeword)}")
			elif choice == "4":
				bits = input("Enter data bits: ")
				size_text = input("Enter word size for splitting (default 16): ").strip()
				word_size = int(size_text) if size_text else 16
				result = checksum_ones_complement(bits, word_size)
				print_header(f"Checksum ({result['word_size']}-bit One's Complement)")
				print(
					f"Padded data      : "
					f"{group_bits(result['padded_data'], result['word_size'])}"
				)
				print(f"Pad bits added   : {result['pad_len']}")
				print(f"Words ({result['word_size']}-bit)   :")
				for word in result["words"]:
					print(f"  {word}")
				print("\nChecksum calculation steps:")
				for step in result["steps"]:
					print(
						f"  Step {step['step']}: {step['before']} + {step['word']} "
						f"= {step['raw_sum']} -> fold = {step['after_fold']}"
					)
				print(f"Sum before comp. : {result['sum_before_complement']}")
				print(f"Checksum         : {result['checksum']}")
				print(
					f"Transmitted bits : "
					f"{group_bits(result['transmitted'], result['word_size'])}"
				)
			elif choice == "5":
				data = input("Enter data bits for Hamming encode: ")
				encoded = hamming_encode(data)
				print_header("Hamming Code")
				print(f"Data bits        : {normalize_bits(data)}")
				print(f"Encoded codeword : {encoded}")
				ans = input("Test error detection/correction? (y/n): ").strip().lower()
				if ans == "y":
					recv = input("Enter received codeword bits: ")
					result = hamming_detect_correct(recv)
					pos = result["error_position"]
					if pos == 0:
						print("No single-bit error detected.")
					else:
						print(f"Error detected at bit position: {pos}")
						print(f"Corrected codeword          : {result['corrected_codeword']}")
			elif choice == "6":
				text = input("Enter text for Reed-Solomon encoding: ")
				nsym_text = input("Parity symbols count (default 8): ").strip()
				nsym = int(nsym_text) if nsym_text else 8
				result = reed_solomon_demo(text, nsym)
				print_header("Reed-Solomon Coding Method")
				print(f"Original text    : {text}")
				print(f"Parity symbols   : {result['parity_symbols']}")
				print(f"Encoded bytes    : {list(result['encoded_bytes'])}")
				print(f"Decoded text     : {result['decoded_text']}")
			elif choice == "7":
				print("Exiting...")
				break
			else:
				print("Invalid choice. Please enter 1 to 7.")
		except Exception as exc:
			print(f"Error: {exc}")

if __name__ == "__main__":
	main()