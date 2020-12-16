with open("input.txt", "r") as f:
    num = [int(line.strip()) for line in f]

# part_1
res = [i for i in num if (2020 - i) in num]
print(f"Part 1 | Found a match! {res[0]} * {res[1]} = {res[0] * res[1]}")

# part_2
res2 = [[2020 - i - j, i, j] for i in num for j in num if (2020 - i - j) in num]
print(f"Part 2 | Found a match! {res2[0][0]} * {res2[0][1]} * {res2[0][2]} = {res2[0][0] * res2[0][1] * res2[0][2]}")
