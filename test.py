import random
import cProfile

if __name__ == "__main__":
	list1 = []
	for i in xrange(0,10000):
		list1.append(random.randint(0,10000))
	
	#random.shuffle(list1)
	cProfile.run("list1.sort()", None, -1)
	print list1