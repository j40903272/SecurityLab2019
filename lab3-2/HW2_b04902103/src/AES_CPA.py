import sys
import numpy as np
import pandas as pd
from Trace import Trace
from AES import Sbox, Rcon

CipherCsv, TraceCsv = sys.argv[2], sys.argv[1]
all_trace_df = pd.read_csv(TraceCsv, header=None)
all_cipher_df = pd.read_csv(CipherCsv, header=None)
cipher_state = all_cipher_df.values


def correlationTraces(O, P):
    (n, t) = O.shape      # n traces of t samples
    (n_bis, m) = P.shape  # n predictions for each of m candidates
    DO = O - (np.einsum("nt->t", O, dtype='float64', optimize='optimal') / np.double(n)) # compute O - mean(O)
    DP = P - (np.einsum("nm->m", P, dtype='float64', optimize='optimal') / np.double(n)) # compute P - mean(P)
    numerator = np.einsum("nm,nt->mt", DP, DO, optimize='optimal')
    tmp1 = np.einsum("nm,nm->m", DP, DP, optimize='optimal')
    tmp2 = np.einsum("nt,nt->t", DO, DO, optimize='optimal')
    tmp = np.einsum("m,t->mt", tmp1, tmp2, optimize='optimal')
    denominator = np.sqrt(tmp)
    return numerator / denominator # (256, 2560)


def inv_key_schedule(lastRoundKey):
    key = np.zeros((44, 4)).astype(int)
    key[43] = lastRoundKey[-4:]
    key[42] = lastRoundKey[-8:-4]
    key[41] = lastRoundKey[-12:-8]
    key[40] = lastRoundKey[-16:-12]
    
    for i in range(39, -1, -1):
        tmp = key[i+3]
        if i%4 == 0: # non-linear transform
            tmp = np.roll(tmp, -1)
            for j in range(4):
                tmp[j] = Sbox[tmp[j]]
            tmp[0] ^= Rcon[(i+4)//4]
        key[i] = np.bitwise_xor(key[i+4], tmp)
    return key



T = Trace(1, 0)
n_sample = len(cipher_state)
lastRoundKey = np.zeros((16))
all_CorrTrace = []

for i in range(16):
    table = np.zeros((n_sample, 256))
    byte = cipher_state[:,i]
    for subkey in range(256):
        for n in range(n_sample):
            table[n, subkey] = T.hamming_weight(byte[n]^subkey)
    CorrTraces = correlationTraces(all_trace_df.values, table)
    CorrTraces[0,:] = 0
    all_CorrTrace.append(CorrTraces)
    lastRoundKey[i] = np.argmax(np.max(CorrTraces, axis=1))


key = inv_key_schedule(lastRoundKey)


tmp = np.stack([lastRoundKey, key[:4].flatten()], axis=0).astype(int)
df = pd.DataFrame(tmp)
df.to_csv("Key.csv", index=False, header=None)
    

line = []
for i in range(16):
    CorrTraces = all_CorrTrace[i]
    rank = np.argsort(np.max(CorrTraces, axis=1))
    first = rank[-1]
    leakagePoint1 = np.argmax(CorrTraces[first])
    coef1 = CorrTraces[first, leakagePoint1]
    second = rank[-2]
    leakagePoint2 = np.argmax(CorrTraces[second])
    coef2 = CorrTraces[second, leakagePoint2]
    line.append([first, coef1, leakagePoint1, second, coef2, leakagePoint2])
df = pd.DataFrame(line)
df.to_csv("Result.csv", index=False, header=None)
        
        
