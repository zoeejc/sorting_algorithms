#!/usr/bin/env python3

def merge_sort(arr):
	if len(arr) > 1:
		left_arr = arr[:len(arr)//2]
		right_arr = arr[len(arr)//2:]

		# recursion
		merge_sort(left_arr)
		merge_sort(right_arr)

		# merging
		i = 0 # left
		j = 0 # right
		k = 0 # merged arr index
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1


arr = [6, 8, 4, 5, 7, 2, 3, 9, 1, 0, 3]
print(f"Array before sorting: {arr}")
merge_sort(arr)
print(f"Array after sorting: {arr}")
