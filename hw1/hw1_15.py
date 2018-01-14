import numpy as np

def sign(x):
	if(x > 0):
		return 1
	else:
		return -1

def main():
	data = np.loadtxt('hw1_15_train.txt')
	# Initlized weight and continuous correct number.
	w = np.array([0, 0, 0, 0], dtype='float')
	correctNum = 0
	isFinished = 0
	step = 0
	i = 0
	dataSize = data.shape[0]

	while not isFinished:
		res = w[0] * data[i][0] + w[1] * data[i][1] + w[2] * data[i][2] + w[3] * data[i][3]
		if sign(res) == data[i][4]:
			correctNum += 1
			i += 1
		else:
			w += np.array([data[i][0], data[i][1], data[i][2], data[i][3]]) * data[i][4]
			step += 1
			correctNum = 0
			print("step {}: index {} is wrong".format(step, i))
			i = 0

		if correctNum == dataSize:
			isFinished = 1
		print(w)

	print('The final weight is {}.'.format(w))
	print('Total train times is {}.'.format(step))

if __name__ == "__main__":
	main()
