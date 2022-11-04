keepGoing = True
i = 0
n = 0
memory = [""]
while keepGoing == True:
	if isPrime(n) == True:
		memory  = memory + [str(n)]
	n = n + 1
	print(n)
	if i == 1000000:
		stop = input("Enter 'x' to stop")
		if stop == "x":
			keepGoing = False
		else:
			i = 0
	i = i + 1

print(memory)
