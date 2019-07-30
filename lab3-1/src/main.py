# coding=UTF-8

import sys
import argparse
import pandas as pd
from AES import AES

parser = argparse.ArgumentParser(description='AES power Trace')
parser.add_argument('input_csv', type=str)
parser.add_argument('-b', type=float, default=1.)
parser.add_argument('-noise', type=float, default=0.)
parser.add_argument('-key', type=int, default=0x35a87c24cb868edfbb41a7432dcd53dc)
args = parser.parse_args()


aes = AES(args.key, args.b, args.noise)
df = pd.read_csv(args.input_csv, header=None)
all_cipher_text = []
all_trace = []

for i in range(len(df)):
    inp_row = df.iloc[i].values
    cipher_text, trace = aes.encrypt(inp_row)
    all_cipher_text.append(cipher_text)
    all_trace.append(trace._AddRoundKey + trace._SubBytes + trace._ShiftRows + trace._MixColumns)

with open('Ciphertext.csv', 'w') as f:
    for c in all_cipher_text:
        tmp = [str(i) for i in c]
        print(",".join(tmp), file=f)


with open('Trace.csv', 'w') as f:
    for t in all_trace:
        tmp = [str(i) for i in t]
        print(",".join(tmp), file=f)