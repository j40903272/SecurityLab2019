# coding=UTF-8

from AES import AES
import numpy as np

key = 0x3220db6534d687f844c41b6de5a4c737
aes = AES(key, 1, 0)
inp_row = np.array([172,47,117,192,67,251,195,103,9,211,21,242,36,87,70,216])
cipher_text, trace = aes.encrypt(inp_row)
assert ([173,205,44,52,32,86,75,184,193,231,36,82,28,6,44,234] == cipher_text).all()
print("AES Test PASS")
