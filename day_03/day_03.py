with open("input.txt", "r") as input_file:
    forrest = [line.rstrip() for line in input_file]


def count_trees(forrest, right, down):
    (pos_x, pos_y, num_trees) = (0, 0, 0)
    while (pos_y + down) < len(forrest):
        if forrest[pos_y + down][(pos_x + right) % len(forrest[0])] == "#":
            num_trees += 1
        pos_x += right
        pos_y += down
    return num_trees


# part_1
single_slope = count_trees(forrest, 3, 1)
print(f"Part 1 | Numbers of trees encountered in one slope: {single_slope}")

# part_2
input_slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


multiple_encounters = [(count_trees(forrest, slope[0], slope[1])) for slope in input_slopes]

product_of_encounters = 1
for encounter in multiple_encounters:
    product_of_encounters *= encounter

print(f"Part 2 | Product of numbers of trees encountered in multiple slope: {product_of_encounters}")
