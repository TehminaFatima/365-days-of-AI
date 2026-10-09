import numpy as np

# Generate a reproducible random dataset
np.random.seed(42)

dataset = np.random.randint(0, 101, size=(1000, 3))

print("Dataset shape:", dataset.shape)
print("\nFirst 10 rows:")
print(dataset[:10])

print("\nNumber of students:", dataset.shape[0])
print("Number of subjects:", dataset.shape[1])

# Create two arrays
array_1 = np.array([[70, 80, 90],
                    [60, 75, 85]])

array_2 = np.array([[88, 92, 78],
                    [95, 81, 89]])

# Vertical stacking: add rows
vertical_stack = np.vstack((array_1, array_2))

# Horizontal stacking: add columns
horizontal_stack = np.hstack((array_1, array_2))

print("Array 1:\n", array_1)
print("\nArray 2:\n", array_2)

print("\nVertical Stack:\n", vertical_stack)
print("Vertical Stack Shape:", vertical_stack.shape)

print("\nHorizontal Stack:\n", horizontal_stack)
print("Horizontal Stack Shape:", horizontal_stack.shape)
# Split the dataset into two parts
first_half = dataset[:500]
second_half = dataset[500:]

# Stack vertically to reconstruct the dataset
combined_vertical = np.vstack((first_half, second_half))

# Add another feature column horizontally
attendance = np.random.randint(50, 101, size=(1000, 1))

combined_horizontal = np.hstack((dataset, attendance))

print("Original Dataset Shape:", dataset.shape)
print("Vertical Stack Shape:", combined_vertical.shape)
print("Horizontal Stack Shape:", combined_horizontal.shape)

# Split the dataset into four equal parts
sub_arrays = np.split(dataset, 4, axis=0)

print("Number of sub-arrays:", len(sub_arrays))

for i, sub_array in enumerate(sub_arrays):
    print(f"\nSub-array {i + 1}:")
    print("Shape:", sub_array.shape)
    print("First 3 rows:\n", sub_array[:3])

    # Select the first group
group_1 = sub_arrays[0]

# Calculate average marks for each subject
subject_averages = np.mean(group_1, axis=0)

print("Group 1 average marks:")
print("Python:", subject_averages[0])
print("Mathematics:", subject_averages[1])
print("AI:", subject_averages[2])

# Recombine all groups
recombined_dataset = np.concatenate(sub_arrays, axis=0)

print("\nRecombined Dataset Shape:", recombined_dataset.shape)
print("Dataset reconstructed successfully:",
      np.array_equal(dataset, recombined_dataset))

# Select students who scored above 80 in Python
python_high_scores = dataset[dataset[:, 0] > 80]

print("Students scoring above 80 in Python:")
print(python_high_scores[:10])
print("Total students:", len(python_high_scores))

# Select students who scored above 70 in all three subjects
high_performers = dataset[np.all(dataset > 70, axis=1)]

print("\nStudents scoring above 70 in all subjects:")
print(high_performers[:10])
print("Total high-performing students:", len(high_performers))

# Select students who scored below 40 in Mathematics
low_math_scores = dataset[dataset[:, 1] < 40]

print("\nStudents scoring below 40 in Mathematics:")
print(low_math_scores[:10])
print("Total students:", len(low_math_scores))

subject_names = ["Python", "Mathematics", "AI"]

print("Dataset Analysis")

for i, subject in enumerate(subject_names):
    marks = dataset[:, i]

    print(f"\n{subject}:")
    print("Average:", round(np.mean(marks), 2))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
    print("Standard Deviation:", round(np.std(marks), 2))

# Count students scoring 50 or above in all subjects
passing_students = dataset[np.all(dataset >= 50, axis=1)]

print("\nStudents scoring at least 50 in every subject:",
      len(passing_students))