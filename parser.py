import re
from binascii import unhexlify

def parse_curve_parameters(filename):
    with open(filename, 'r') as f:
        content = f.read()

    clean_content = re.sub(r'\s+', '', content)
    integers = re.findall(r'INTEGER\s*([0-9A-F\s]+)', content, re.IGNORECASE)
    
    hex_values = []
    for i in integers:
        cleaned = re.sub(r'\s|^00', '', i, flags=re.IGNORECASE)
        hex_values.append(cleaned)

    numbers = [int(hex_val, 16) for hex_val in hex_values]

    if len(numbers) >= 7:
        p, a, b, m, q, x, y = numbers[:7]
        return {
            'p': p,
            'a': a,
            'b': b,
            'm': m,
            'q': q,
            'x': x,
            'y': y
        }
    else:
        raise ValueError("Недостаточно параметров в файле")

#params = parse_curve_parameters('A1_sequence.txt')
#print(params)

