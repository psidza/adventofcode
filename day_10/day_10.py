# Part 1
with open("input.txt", "r") as data_input:
    adapters = sorted([int(adaptor.rstrip()) for adaptor in data_input])

# preppending 0 as outlet joltage and appending new element that's sum of highest rated adaptor and 3 jolts
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)


# generating list of difference in joltage between adapters
diff = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]

print(f"Part 1 | Number of 1-jolt differences times number of 3-jolt differences: {diff.count(1) * diff.count(3)}")

# Part 2
# generating list of ways to each adaptor in the list by calculating acceptable difference in jolts
# number of acceptable joltages between 2 adaptors results in increased number of ways
number_of_ways = [1]
for i in range(1, len(adapters)):
    number_of_ways.append(0)
    for j in [1, 2, 3]:
        if i >= j and (adapters[i] - adapters[i - j] <= 3):
            number_of_ways[i] += number_of_ways[i - j]

print(f"Part 2 | Number of distinct ways: {number_of_ways[-1]}")