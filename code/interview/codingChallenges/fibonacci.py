saved_values = {}

def fibonacci(target):
	if target == 0:
		return 0
	if target == 1:
		return 1
	return fibonacci(target - 2) + fibonacci(target - 1)

def fibonacci_better(target):
	if target == 0:
		return 0
	if target == 1:
		return 1

	if (target - 2) not in saved_values:
		saved_values[target - 2] = fibonacci_better(target - 2)
	if (target - 1) not in saved_values:
		saved_values[target - 1] = fibonacci_better(target - 1)

	return saved_values[target - 2] + saved_values[target - 1]

print fibonacci_better(50)
