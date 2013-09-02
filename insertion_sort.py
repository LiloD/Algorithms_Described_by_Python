import cProfile
import random
'''
this is the insertion sort Algorithm implemented by Python
Pay attention to the break condition of inner loop
if you've met the condition(the key value find a place to insert)
you must jump out of the loop right then
Quick Sort is Moderately fast for small input-size(<=30)
but weak for Large Input 

by Zhizhuo Ding
'''


class InsertionSort:
	"Algorithm---Insertion Sort"

	@staticmethod
	def execute(array):
		array = list(array)
		for i in xrange(1,len(array)):
			key = array[i]
			for j in range(0,i)[::-1]:
				if key < array[j]:
					array[j+1] = array[j]
				if key >= array[j]:
					array[j+1] = key
					break
		#return carefully at a right place
		return array

	@staticmethod
	def execute_ver2(array):
		'''donot use the additional key value,
		all elements in array rearrange where they're
		fairly effient in its usage of storage
		'''
		array = list(array)
		for i in xrange(1,len(array)):
			for j in range(0,i)[::-1]:
				'''
				here,because that we don't use additional varible to
				keep the key(which is array[i] on the beginning)
				the value will change in this case
				so we can only compare array[j+1] with array[j]
				not compare array[i] with [array[j]]
				'''
				if array[j+1] < array[j]:
					array[j],array[j+1] = array[j+1],array[j]
		return array

if __name__ == "__main__":
	list1 = []
	for i in xrange(0,10000):
		list1.append(random.randint(0,10000))
	cProfile.run("list1 = InsertionSort.execute_ver2(list1)", None, -1)
	print list1

	