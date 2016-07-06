import datetime
import random

#time = 0:00:09.698000

def selection_sort(a):
	index = 0

	if len(a) == 0 or len(a) == 1:
		return a

	min_index = index
	while (len(a)-index) > 1:
		for i in range(index, len(a)):
			if a[i] < a[min_index]:
				min_index = i

		temp = a[index]
		a[index] = a[min_index]
		a[min_index] = temp

		index += 1
		min_index = index

x = []
for i in range(0, 10000):
	x.append(random.randint(0,10000))

# x = [7,8,5,2,4,6,3]

start = datetime.datetime.now()
selection_sort(x)
end = datetime.datetime.now()
total_time = end-start
print total_time
# print x