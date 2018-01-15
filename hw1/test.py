import numpy as np

# data = np.loadtxt('hw1_15_train.txt')
# inputX = np.ndarray((400, 5))
# np.random.shuffle(data)
# inputY = np.ndarray((400))
# for i in range(400):
# 	inputX[i][0] = 1
# 	inputX[i][1] = data[i][0]
# 	inputX[i][2] = data[i][1]
# 	inputX[i][3] = data[i][2]
# 	inputX[i][4] = data[i][3]
# 	inputY[i] = data[i][4]
# print(inputX)
x = np.ndarray((5))
for i in range(5):
	x[i] = i
print(np.mean(x))

