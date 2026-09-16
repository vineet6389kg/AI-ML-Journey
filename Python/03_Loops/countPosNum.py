numbers = [1,3,-2,-6,3,3,8,-7,-2]

positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count += 1
print("Total Count of Positive Number is ", positive_num_count)