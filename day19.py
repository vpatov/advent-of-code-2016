from math import log
elves = 3017957
test_cases = {1:1,2:1,3:3,4:1,5:3,6:5,7:7,8:1,9:3,10:5,11:7}

def ff(n):
	up = 2
	cur = 1
	i = 0
	while (i < n):
		while(cur < up and i < n):
			yield cur
			i += 1
			cur += 2
		cur = 1
		up *= 2

def f(n):
	return list(ff(n))[-1]
print("Part I")
print(f(elves))
