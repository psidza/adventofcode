with open("input.txt", "r") as data_input:
    colors = ["shiny gold"]
    for color in colors:
        data_input.seek(0)
        for line in data_input:
            if color in line and not line.lstrip().startswith(color):
                if " ".join(line.split()[0:2]) not in colors:
                    colors.append(" ".join(line.split()[0:2]))
    print(len(colors) - 1)
    print(colors)