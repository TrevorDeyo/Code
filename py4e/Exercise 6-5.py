text = "X-DSPAM-Confidence:    0.8475"
start_pos = text.find(':') + 1
number_str = text[start_pos:].strip()
number = float(number_str)
print(number_str)