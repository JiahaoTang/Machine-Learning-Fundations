import numpy as np
import matplotlib.pyplot as plt

def sign(x):
	if(x > 0):
		return 1
	else:
		return -1

def correctRate(inputX, inputY, w):
	correct = 0
	wrong = 0
	for i in range(inputX.shape[0]):
		if sign(np.dot(inputX[i], w)) == inputY[i]:
			correct += 1
		else:
			wrong += 1
	return correct / (correct + wrong)

def main():
	rate = []
	for time in range(2000):
		# Read train data from database
		data = np.loadtxt('hw1_18_train.txt')
		np.random.shuffle(data)
		dataSize = data.shape[0]
		#Iterate for 2000 times
		inputX = np.ndarray((dataSize, 5))
		inputY = np.ndarray((dataSize, 1))
		for i in range(dataSize):
			inputX[i][0] = 1
			inputX[i][1] = data[i][0]
			inputX[i][2] = data[i][1]
			inputX[i][3] = data[i][2]
			inputX[i][4] = data[i][3]
			inputY[i]    = data[i][4]

		# Initlized weight and continuous correct number.
		w = np.array([0, 0, 0, 0, 0], dtype='float')
		step = 0
		corRate = 0
		updateTimes = 0

		while updateTimes <= 50:
			for j in range(dataSize):
				if sign(np.dot(inputX[j], w)) != inputY[j] and (correctRate(inputX, inputY, w + inputX[j]*inputY[j]) > corRate):
					w = w + inputX[j] * inputY[j]
			updateTimes += 1


		# Read test data from database
		testData = np.loadtxt('hw1_18_test.txt')
		testDataSize = testData.shape[0]
		#Iterate for 2000 times
		inputTestX = np.ndarray((testDataSize, 5))
		inputTestY = np.ndarray((testDataSize, 1))
		for i in range(testDataSize):
			inputTestX[i][0] = 1
			inputTestX[i][1] = testData[i][0]
			inputTestX[i][2] = testData[i][1]
			inputTestX[i][3] = testData[i][2]
			inputTestX[i][4] = testData[i][3]
			inputTestY[i]    = testData[i][4]

		testCorRate = correctRate(inputTestX, inputTestY, w)
		print(testCorRate)
		rate.append(testCorRate)

	num = len(set(rate))
	plt.hist(rate, bins=num)
	plt.show()

if __name__ == "__main__":
	main()
