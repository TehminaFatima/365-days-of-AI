import numpy as np

random_array = np.random.rand(3,3) # np.random.rand(d0, d1, ..., dn) creates an array of the given shape and populates it with random samples from a uniform distribution over [0, 1).
print("random_array" , random_array) 

random_int_array = np.random.randint(1,10,(3,3)) # np.random.randint(low, high=None, size=None, dtype=int) returns random integers from low (inclusive) to high (exclusive). If high is None (the default), then results are from [0, low). This function is an alias for random_integers.

normal_array = np.random.normal(1,1, (3,3)) #np.random.normal(loc=0.0, scale=1.0, size=None) draws random samples from a normal (Gaussian) distribution. The loc parameter is the mean, the scale parameter is the standard deviation, and the size parameter specifies the output shape.

print("normal_array " , normal_array)
print("random_int_array : " , random_int_array)

np.random.seed(42) #sets the seed for the random number generator, ensuring that the same random numbers are generated each time the code is run. This is useful for reproducibility.
seed_random_number = np.random.rand(5)
print("seed_random_number : " , seed_random_number) 

# simulate a normal distribution

normal_distribution = np.random.normal(loc=0, scale=1, size=5) # loc is the mean, scale is the standard deviation, and size is the number of samples to generate.
print("normal_distribution : " , normal_distribution)

#simulate a uniform distribution

uniform_distribution = np.random.uniform(low=0.0, high=1.0, size=5) # low is the lower boundary of the output interval, high is the upper boundary of the output interval, and size is the number of samples to generate.
print("uniform_distribution : " , uniform_distribution)