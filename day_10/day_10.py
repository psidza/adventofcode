# Part 1
with open("input.txt", "r") as data_input:
    adaptors = data_input.readlines()
    adaptors = sorted([int(adaptor.rstrip()) for adaptor in adaptors])

# preppending 0 and appending 3 to the list
adaptors.insert(0, 0)
adaptors.append(adaptors[-1] + 3)

# generating list of difference in voltage between adapters
diff = [adaptors[i] - adaptors[i - 1] for i in range(1, len(adaptors))]

print(f"Part 1 | Number of 1-jolt differences times number of 3-jolt differences: {diff.count(1) * diff.count(3)}")

# Part 2