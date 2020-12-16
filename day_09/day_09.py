with open("input.txt", "r") as data_input:
    numbers = data_input.readlines()
    numbers = [int(number.rstrip()) for number in numbers]

confirmed_numbers = []

preamble = 25

# part_1
# generate a list of numbers that result in sum of 2 numbers prior them within preamble range
for i in range(0, len(numbers) - preamble):
    for j in numbers[i : i + preamble]:
        if (numbers[i + preamble] - j) in numbers[i : i + preamble]:
            confirmed_numbers.append(numbers[i + preamble])

# comparing list of input numbers with list of confirmed_numbers
# first number that we find in that comparison it's being assigned to number_without_sum variable
number_without_sum = [number for number in numbers[preamble:] if number not in confirmed_numbers][0]
print(f"Part 1 | Number without sum is: {number_without_sum}")


# part_2
# for number_without_sum list we need to find what set of 2 or more numbers in sum gives that number
# when we find that set, we need to sum min and max element of that set
for i in range(0, len(numbers)):
    for j in range(1, len(numbers) - 1):
        contiguous_set = numbers[i:j]
        if (number_without_sum not in contiguous_set) and sum(contiguous_set) == number_without_sum:
            print(f"Part 2 | Sum of min and max elements of that list is: {min(contiguous_set) + max(contiguous_set)}")
