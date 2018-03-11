import numpy
import random

def neural_network():
	for i in range(100):
		i0 = random.randint(0,1)
		i1 = random.randint(0,4)
		q0 = random.randint(0,6)
		q1 = random.randint(0,2)
		b = random.randint(0,1)
		x = i0 * q0 + i1 + q1 + b
		sigmoid = 1 / (1 + numpy.exp(-x))
		print('[',sigmoid,']')

neural_network()
