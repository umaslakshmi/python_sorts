'''
base case: len(arr) = 0 or 1 -> return
start at first/second elements
put in order
move forward by one place
if anything was swapped, repeat with arr from first element to last-1
'''
#0:00:00.003000 time
import random
import datetime

def bubblesort(x):
	swapped = True;
	if(len(x) == 0 or len(x) == 1):
		return x

	#index1 = x[0]
	#index2 = x[1]

	counter = 0
	while swapped:
		swapped = False
		for i in range(0,len(x)-counter-1):
			if x[i] > x[i+1]:
				temp = x[i]
				x[i] = x[i+1]
				x[i+1] = temp
				swapped = True
		counter += 1

	return x

a = []
for i in range(0,101):
	a.append(random.randint(0,10000))

t = datetime.datetime.now()

x = bubblesort(a)

w = datetime.datetime.now()

time = w-t
print time

print x