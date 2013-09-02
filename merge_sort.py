'''
Merge Sort is a typical Divide-and-Conquer Algorithm
It's  faster than quick sort 
It average time cost is O(nlogn)
It merge the subarray from bottom to top

by Zhizhuo Ding
'''
import cProfile
import random


class MergeSort:
	'Algorithm---Merge Sort'

	@staticmethod
	def execute(array):
		#make sure the array is mutable
		#array = list(array)
		l = len(array)
		result = []
		if l == 1:
			#this place we define the end of the recursion
			return array
		else:
			#divide the array
			mid = l/2
			lower_list = array[0:mid]
			upper_list = array[mid:l]
			#conquer each subarray
			#recursively call the function
			result = MergeSort.subroutine(MergeSort.execute(lower_list),MergeSort.execute(upper_list))
			return result 



	@staticmethod
	def subroutine(a1,a2):
		merged_list = []
		'''2 index for two array'''
		index_a1 = 0
		index_a2 = 0
		
		while (len(merged_list) < len(a1) + len(a2)):
			'''Pay attention to this loop skills'''
			if index_a1 == len(a1):
				merged_list.extend(a2[index_a2:])
				break

			elif index_a2 == len(a2):
				merged_list.extend(a1[index_a1:])
				break

			elif a1[index_a1]<=a2[index_a2]:
				merged_list.append(a1[index_a1])
				index_a1 += 1 

			elif a1[index_a1]>=a2[index_a2]:
				merged_list.append(a2[index_a2])
				index_a2 += 1

		return merged_list
		'''
		merged_list = []
		while len(merged_list) == len(a1)+len(a2):
			index_a1 = 0
			index_a2 = 0
			if a1[index_a1]<a2[index_a2] and index_a1 < len(a1) and index_a2 < len(a2):
				merged_list.append(a1[index_a1])
				index_a1 += 1 
			elif a1[index_a1]>=a2[index_a2] and index_a1 < len(a1) and index_a2 < len(a2):
				merged_list.append(a2[index_a2])
				index_a2 += 1
			elif index_a1 == len(a1):
				merged_list.extend(a2[len(a1):])
			elif index_a2 == len(a2):
				merged_list.extend(a1[len(a2):])

		return merged_list
		'''

if __name__ == "__main__":
	list1 = []
	for i in xrange(0,10000):
		list1.append(random.randint(0,10000))
	cProfile.run("list1=MergeSort.execute(list1)", None, -1)
	print list1 