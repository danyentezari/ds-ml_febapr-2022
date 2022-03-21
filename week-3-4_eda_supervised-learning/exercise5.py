observations = [
    12,
    10,
    4,
    6,
    15,
    8,
    19,
    5
]
# Use 'for loop' and 'len()' to calculate the 
# mean value for 'observation'


# Calculate the numerator
numerator = 0
for value in observations:
    numerator = numerator + value


# Calculate the denominator
denominator = len(observations)

# Calculate the mean
mean = numerator/denominator

print('the mean is', mean)