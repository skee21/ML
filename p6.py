import random
def uniform_random():
    return random.random()
def f(x):
    return x**2
samples = [uniform_random() for _ in range(10)]
f_values = [f(x) for x in samples]
I_estimate = sum(f_values) / 10
print("Random Samples (x):")
print([f"{x:.2f}" for x in samples])
print("Function values f(x):")
print([f"{x:.2f}" for x in f_values])
print("Monte Carlo Estimate of Integral I: {:.2f}".format(I_estimate))