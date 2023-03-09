# This problem is based on the One Time Pad
# The encrypted message is stored in the variable 'hexcode'
# The key is only 1 byte long
# The plaintext has been easily found by looking at the printed results iteratively.

hexcode = '104e137f425954137f74107f525511457f5468134d7f146c4c'
bytecode = bytes.fromhex(hexcode)

key = b'\x00' * len(bytecode)

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

result = ""
for x in range(0, 256):
    result = xor(bytecode, key)
    print(x, "XORED RESULT:", result, end='\n')
    print(end='\n\n')
    key = chr(x).encode('latin-1') * len(bytecode)
