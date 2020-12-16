# part 1 solved on a proper way
import re

# dictionary of parent bags
parents = {}

# generating dictionary, where parent bags are keys and values are dictionaries that contain their children bags
with open("input.txt", "r") as data_input:
    for line in data_input:
        parent_bag = re.findall("^([a-z]+ [a-z]+)", line)[0]
        children_bags = re.findall("([1-9] [a-z]+ [a-z]+)", line)
        if parent_bag not in parents:
            # creating a dictionary for each parent within of dictionary
            parents[parent_bag] = {}
            for child_bag in children_bags:
                # adding children within dcitionary and a bag count that each child can hold {'light maroon': '5', 'pale tomato': '4', 'clear blue': '5'}
                parents[parent_bag][child_bag[2:]] = child_bag[0]

# part_1
main_bag = "shiny gold"

bags = [main_bag]  # using main_bag as a starting point

for bag in bags:
    for k, v in parents.items():
        if bag in v:
            bags.append(k)

result1 = len(set(bags)) - 1
print(f"Part 1 | Number of bag colors can eventually contain at least one {main_bag} bag: {result1}")


# part_2
main_bag = "shiny gold"
bags = [main_bag]  # using main_bag as a starting point

for bag in bags:
    for k, v in parents[bag].items():
        for i in range(int(v)):
            bags.append(k)

result2 = len(bags) - 1
print(f"Part 2 | Number of individual bags thatare required inside single {main_bag} bag: {result2}")
