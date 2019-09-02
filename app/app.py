import random
import numpy as np

def main():
	list = [random.randint(0,20) for i in range(0,100)]
	np.save("nums.npy",np.asarray(list))
	a = np.load("nums.npy")
	print(a)

if __name__ == "__main__":
	main()
