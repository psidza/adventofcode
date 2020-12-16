with open("input.txt", "r") as input_data:
    answers = [data for data in input_data.read().split("\n\n")]

    # part_1
    result1 = sum([len(set(list(group.replace("\n", "")))) for group in answers])
    print(f"Part 1 | Number of YES answers in total: {result1}")

    # part_2
    result2 = sum([len(set.intersection(*map(set, group.split()))) for group in answers])
    print(f"Part 2 | Number of questions where everyone within one group answered YES: {result2}")
