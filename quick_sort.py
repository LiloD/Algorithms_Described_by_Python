'''
This is the Quick Sort implement by Python
This QS Alg have no Optimiztion
QS alse use Divide and Conquer Strategy 
it sorts the input in place(effient in usage of storage)
it's very practical
by Zhizhuo Ding
'''

import random
import cProfile

class QuickSort:
	
	@staticmethod
	def execute_randomize(array,p,q):
		pass	

	@staticmethod
	def execute(array,p,q):
		#this condition here ensure the end of the recursion call
		if p<q:
			r = QuickSort.subroutine(array, p, q)
			QuickSort.execute(array, p, r)
			QuickSort.execute(array, r+1, q)
		return array	



	@staticmethod
	def subroutine(array,p,q):
		'this is the partition subroutine for Quick Sort'
		#init index of upper subarray and lower subarray and the pivot
		#in fact i,j represent the upper bound of this two subarray 
		pivot = array[p] #pivot can be other element in array
		i = p
		for j in xrange(p+1,q):
			if array[j] < pivot:
				i += 1
				array[i],array[j] = array[j],array[i]
		
		array[i],array[p] = array[p],array[i]
		return i


#small test
if __name__ == "__main__":
	list1 = []
	for i in xrange(0,10000):
		list1.append(random.randint(0,10000))
	#random.shuffle(list1)
	cProfile.run("list1=QuickSort.execute(list1,0,len(list1))", None, -1)
	print list1 
				