with open("input.txt", "r") as input_data:
    passes = sorted(
        [
            # converting ticket number from binary to decimal where B=1 F=0 R=1 L=0 and sorting that list
            int(plane_pass.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0").strip(), 2)
            for plane_pass in input_data.readlines()  # noqa
        ]
    )
    print(f"Part 1 | Highest ticket number is {passes[-1]}")
    print(f"Part 2 | Your seat number is: {[seat for seat in range(passes[0], passes[-1]) if seat not in passes][0]}")
