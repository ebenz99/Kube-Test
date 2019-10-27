import random
#import numpy as np
import os
import sys
import time
import requests

def main():
	# mylist = [random.randint(0,20) for i in range(0,100)]
	# np.save("nums.npy",np.asarray(mylist))
	# time.sleep(300)
	mname = "THIS IS ETHAN WORKKINGc"
	URL = "https://ptsv2.com/t/ethan-place/post"
	PARAMS = {'name':mname}
	r = requests.post(url = URL, params = PARAMS)


if __name__ == "__main__":
	main()
