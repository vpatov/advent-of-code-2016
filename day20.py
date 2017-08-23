ips = [[int(i) for i in line.strip().split('-')] for line in open('day20.txt','r').readlines()]
ips.sort()

print("Part I")
prev = 0
for pair in ips:
	first,second = pair
	if first > prev + 1:
		print(prev + 1)
		break
	prev = second
