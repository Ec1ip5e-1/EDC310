

import Q1_Wichmann_Hill
import matplotlib.pyplot as plt
import math
import numpy as np


WH = Q1_Wichmann_Hill.Uniform()



class Modulate(object):
	
	def __init__(self):
		Temp = 1
		
		
	
	
	def BPSK(self, Samples):
		M=2		# Symbol constellation size
		n=1		# Number of bits
		
			# BPSK Bit-to-Symbol mapping (1=>1, 0=>-1)
		Transmitted = []
		TSymbols = []
		for i in range(Samples):
			Bit = WH.GenerateBit()
			Transmitted.append(Bit)
			if (Bit == 1):	
				TSymbols.append(1)
			elif(Bit == 0):
				TSymbols.append(-1)
			
			
			# Add noise to data symbols
		Received = []
		RSymbols = []
		for i in range(-4,12+1):	# i = Eb/No
			sigma = 1/ math.sqrt(math.pow(10, i/10)*2*n)
											# Gaussian noise
			RSymbols = TSymbols + sigma * np.random.normal(0, 0.2, Samples)
# 			print(Received)
		# Decode
			# Compare closest symbol
		
		
		

	def main(self):
		
		self.BPSK(10)
		

Mod = Modulate()
Mod.main()