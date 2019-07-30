# coding=UTF-8

from random import gauss

class Trace():
    def __init__(self, b, noise):
        self.b = b
        self.noise = noise
        self._AddRoundKey = []
        self._SubBytes = []
        self._MixColumns = []
        self._ShiftRows = []
        

    def AddRoundKey(self, state):
        self._AddRoundKey += self.sample(state)

    def SubBytes(self, state):
        self._SubBytes += self.sample(state)

    def MixColumns(self, state):
        self._MixColumns += self.sample(state)

    def ShiftRows(self, state):
        self._ShiftRows += self.sample(state)

    def hamming_weight(self, state):
        return bin(state).count("1")

    def sample(self, state):
        tmp = []
        for i in range(4):
            for j in range(4):
                noise = gauss(0, self.noise)
                leakage = self.b*self.hamming_weight(state[i][j]) + noise
                tmp += [-1+noise, leakage, -2+noise, noise]
        return tmp