a = input('Введите cтроку: \n')
b = a
a = a.split(' ')
C = 0.1
K = int(input('Введите ключ: \n'))
new_a = []
for i in range(0, len(a)):
    h = int(len(a[i])*((K*C) % 1))
    new_a.append(h)
print('Метод умножения.\nРезультат:', new_a)


CRC_POLYMINAL = 0x04C11DB7
def encodeCRC(input_data: str, crc_pol: int = CRC_POLYMINAL) -> int:
    binary_data = ""
    for i in range(len(input_data)):
        binary_data += bin(ord(input_data[i]))[2:]

    poly_pow = len(bin(crc_pol)[2:]) - 1
    binary_data += "0" * poly_pow

    crc_xor = int(binary_data[:poly_pow + 1], 2) ^ crc_pol
    offset = 1
    crc_xor_str = bin(crc_xor)[2:]
    while offset < len(binary_data) - poly_pow:
        if len(crc_xor_str) == poly_pow + 1:
            crc_xor = int(crc_xor_str, 2) ^ crc_pol
            crc_xor_str = bin(crc_xor)[2:] + binary_data[poly_pow + offset]
        else:
            crc_xor_str += binary_data[poly_pow + offset]
        offset += 1
        if offset == len(binary_data) - poly_pow:
            crc_xor = int(crc_xor_str, 2)
    return crc_xor
print('CRC32. \nРезультат:', encodeCRC(b))