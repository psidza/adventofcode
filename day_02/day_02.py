with open("input.txt", "r") as input_file:
    # transforms input file into list of lists where 4-5 r: rrrjr -> ['4-5', 'r:', 'rrrjr']
    lines = [line.rstrip().split(" ") for line in input_file]

policy1 = policy2 = 0

for line in lines:
    min_limit, max_limit = map(int, line[0].split("-"))
    letter = line[1][0]
    password = line[2]

    # part_1
    # this if checks for fillfulment of policy1 where only number of apperance of one letter is mandatory
    if max_limit >= password.count(letter) >= min_limit:
        policy1 += 1

    # part_2
    # this if checks for fillfulment of policy2 where position of predefined letter must be fillfulled,
    # we're using xor in order to verify if letter is present at exactly one position (out of 2 available)
    if bool(password[min_limit - 1] == letter) != bool(password[max_limit - 1] == letter):  # noqa
        policy2 += 1

print(f"Part 1 | Valid passwords by policy 1: {policy1}")
print(f"Part 2 | Valid passwords by policy 2: {policy2}")
