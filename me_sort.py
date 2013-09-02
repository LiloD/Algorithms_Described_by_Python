# -*- coding:utf-8 -*-
'''
The Algorithm to find the Kth big element in a array
Average Time is O(n)
Worst Case will be regenerate to O(n²)
'''
from quick_sort import QuickSort
import math

def mediansort(ar,p,q):
		
	if p < q:
		#mid = math.floor((q-p-1)/2+p)
		#selectKth(ar,p,q,(mid-p+1))
		k =int(math.floor((q-p-1)/2)+1)
		mid = selectKth(ar,p,q,k)

		mediansort(ar, p, mid)
		mediansort(ar, mid+1, q)

	return ar
	


def selectKth(ar,left,right,k):
	#1 <= k <= right-left
	#idx = selectPivotIndex(ar,left,right);
	if left<right:
		pivot_index = QuickSort.subroutine(ar, left, right)
		
		#pay attention to this condition
		#the Kth means (k-1)th in a array(given that array start with 0)
		index = left+(k-1)
		if pivot_index == index:
			return pivot_index

		if (index < pivot_index):
			return selectKth(ar,left,pivot_index,k)
		else:
			return selectKth(ar,pivot_index+1,right,(index-pivot_index))
	return

if __name__ == "__main__":
	list3 = [5,3,1,614,2,55,23,651]
	mediansort(list3,0,len(list3))
	print list3