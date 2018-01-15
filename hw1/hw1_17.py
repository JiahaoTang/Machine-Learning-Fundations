import numpy as np
import matplotlib.pyplot as plt

def sign(x):
	if(x > 0):
		return 1
	else:
		return -1

def isFinished(w, X, Y):
	for i in range(X.shape[0]):
		res = w[0] * X[i][0] + w[1] * X[i][1] + w[2] * X[i][2] + w[3] * X[i][3] + w[4] * X[i][4]
		if sign(res) != Y[i]:
			return i
	return X.shape[0]
    
def main():
	eta = 0.5
	# Read data from database
	data = np.loadtxt('hw1_15_train.txt')
	#Initialized a variable to store summary of every update times.
	updateTimesSum = 0
	#Initialized a list to store the update times.
	updateTimes = []
	#Iterate for 2000 times
	for time in range(2000):
		np.random.shuffle(data)
		inputX = np.ndarray((400, 5))
		inputY = np.ndarray((400, 1))
		for i in range(400):
			inputX[i][0] = 1
			inputX[i][1] = data[i][0]
			inputX[i][2] = data[i][1]
			inputX[i][3] = data[i][2]
			inputX[i][4] = data[i][3]
			inputY[i]    = data[i][4]

		# Initlized weight and continuous correct number.
		w = np.array([0, 0, 0, 0, 0], dtype='float')
		step = 0
		dataSize = data.shape[0]

		while True:
			returnValue = isFinished(w, inputX, inputY)

			if  returnValue == dataSize:
				break
			else:
				i = returnValue
				# w = w + x * y (update weight vector)
				w += eta * inputX[i] * inputY[i] 
				step += 1
		updateTimes.append(step)
		updateTimesSum += step


	print("The average update time is {}".format(updateTimesSum / 2000))
	num = len(set(updateTimes))
	plt.hist(updateTimes, bins=num)
	plt.show()

if __name__ == "__main__":
	main()
