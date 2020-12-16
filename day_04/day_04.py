import re

with open("input.txt", "r") as input_data:
    temp = [data.replace("\n", " ").split() for data in input_data.read().split("\n\n")]  # noqa
    passports = []
    for person in temp:
        passports.append(dict(data.split(":") for data in person))

    # part1
    valid_passports = 0
    for passport in passports:
        if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and not passport.get("cid", 0)):  # noqa
            valid_passports += 1
    print(f"Part 1 | Number of valid passwords {valid_passports}")

    # part2
    valid_passports = 0
    for person in passports:
        if (
            (1920 <= int(person.get("byr", 0)) <= 2020)
            and (2010 <= int(person.get("iyr", 0)) <= 2020)
            and (2020 <= int(person.get("eyr", 0)) <= 2030)
            and person.get("hgt", 0)
            and (
                (person["hgt"][-2:] == "cm" and 150 <= int(person["hgt"][:-2]) <= 193)
                or (person["hgt"][-2:] == "in" and 59 <= int(person["hgt"][:-2]) <= 76)
            )
            and person.get("hcl", 0)
            and (re.match(r"#[\da-f]{6}", person["hcl"]))
            and person.get("ecl", 0)
            and (person["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            and person.get("pid", 0)
            and (re.match(r"\d{9}$", person["pid"]))
        ):
            valid_passports += 1

    print(f"Part 2 | Number of valid passwords {valid_passports}")
