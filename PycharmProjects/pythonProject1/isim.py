import time
import matplotlib.pyplot as plt

# Loop-based summation
def sum_of_n_loop(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i
    stop = time.time()
    return the_sum, stop - start

# Formula-based summation
def sum_of_n_formula(n, repetitions=100):
    start = time.perf_counter()
    for _ in range(repetitions):
        the_sum = n * (n + 1) / 2  # Repeat the calculation to amplify time
    stop = time.perf_counter()

    avg_time = (stop - start) / repetitions  # Average time over repetitions
    return the_sum, avg_time

# Test values of n
n_values = [10**i for i in range(1, 10)]

# Measure times for both methods
loop_times = []
formula_times = []

for n in n_values:
    _, loop_time = sum_of_n_loop(n)
    _, formula_time = sum_of_n_formula(n)

    loop_times.append(loop_time)
    formula_times.append(formula_time)

print(loop_times)
print(formula_times)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, loop_times, label='Loop-based Summation', marker='o')
plt.plot(n_values, formula_times, label='Formula-based Summation (avg over repetitions)', marker='o')

plt.title('Time Complexity of Loop vs Formula-based Summation with Amplified Time')
plt.xlabel('n (Number of Terms)')
plt.ylabel('Time (seconds)')
plt.xscale('log')  # Log scale to better visualize differences
plt.yscale('log')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()