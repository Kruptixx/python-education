# While Loop
def fibonacci_while(n):
	# func doesn't work for negative int and other types
	if type(n) != type(1) or n < 0:
		return None
	# return for 0 and 1
	if n < 2:
		return n

	first = 0
	second = 1
	counter = 1
	while counter < n:
		second = second + first
		print(f"count: {counter} | f={first}, s={second}")  # log
		first = first ^ second  # xor exchange
		second = second ^ first
		first = first ^ second
		# first, second = second, first  # faster than xor
		counter += 1
	return first + second


# Recursive
def fibonacci_recur(n):
	if type(n) != int or n < 0:
		return None
	return n if n < 2 else (fibonacci_recur(n - 1) + fibonacci_recur(n - 2))


# Lambda Recursive
fib = lambda n: n if n < 2 else (fib(n - 1) + fib(n - 2))


# Lambda Recursive(failsafe)
fib2 = lambda n: (None if n < 0 or type(n) != int else n) if n < 2 else \
	(fib2(n-1) + fib2(n-2))




if __name__ == "__main__":
	print("\033[92m Fibonacci Sequence")
	print("\033[95m------While Loop------")
	print(f"Final number: {fibonacci_while(int(input('Enter number: ')))}\n")
	print("------Recursive------")
	print(f"Final number: {fibonacci_recur(int(input('Enter number: ')))}\n")
	print("------Lambda Recursive------")
	print(f"Final number: {fib(int(input('Enter number: ')))}\n")
	print("------Lambda Recursive 2------")
	print(f"Final number: {fib2(int(input('Enter number: ')))}\n")