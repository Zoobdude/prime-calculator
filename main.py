from threading import Thread # imports threading module


def isPrime(n): # checks if prime - returns Boolean
	if n <= 3: # if n is less than or equal to 3 
		return n > 1 # if it is greater than 1 (2 or 3) then it is prime - returns 2 ,   if it is 1 or less then it is not prime
	if not n%2 or not n%3: # % sign checks if n divided by the number has a remainder
		# if it has a remainder then it is not divisible by the number (2 or 3)
		# if it doesn't have a remainder then it is exactly divisible by that number (2or3) - making it not prime
		return False # returns false if the number has no remainder when divided by 2 or 3
	# all primes are in the form 6k ± 1, where k is any integer greater than 0
	k = 1
	stop = int(sqrt(n)) # all factor pairs will have one digit that is smaller than the sqrt of n, this is because after the factor pair x*x the factor pairs start repeating themselves, for example 100 is divisible by 2×50, 4×25, 5×20, 10×10, 20×5, 25×4, 50×2 note that after 10x10 (the square roots of 100) the factors start to repeat themselves - this means that you only need to check for factors up to the sqrt of n
	while (6*k) <= stop: # counts in 6k (from 6k±1) up to the sqrt of n
		if not n%((6*k)-1) or not n%((6*k)+1): # checks if dividing by 6k±1 results in a whole number - not prime 
			return False # if n can be divided by any of the tested numbers then it is not prime so False is returned
		k = k + 1 # increments k by 1 in order to test all possible factors of 6k±1
	return True # if all of the tested possible factors do not work then the number is prime

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
