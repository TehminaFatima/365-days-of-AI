import numpy as np

dice_rolls = np.random.randint(1, 7, size=1000) # Simulate rolling a six-sided die 1000 times
unique, counts = np.unique(dice_rolls, return_counts=True) # Count the occurrences of each die face

print("Dice rolls: ", dice_rolls )
print("Unique values: ", unique)
print("Counts: ", counts)