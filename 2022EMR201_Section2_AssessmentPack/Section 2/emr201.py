"""
    EMR201 Support Module - SECTION 2

    :copyright: Copyright 2020-2021 by the Department of EECE,
                University of Pretoria. All rights reserved.
"""

# ----------------------------------------------------------------------
# Section 2 support

test_hero_stats = [
    ["OOMPA", "SPEED", "STRENGTH", "ENDURANCE", "COURAGE", "POWER", "LOOMPA"],
    ["BASE (UP)", 5, 10, 15, 20, 25],
    ["LC (SPORT)", 30, 35, 40, 45, 50],
    ["STRIP (JOL)", 55, 60, 65, 70, 75],
    ["FAUZI (EAT)", 80, 85, 90, 95, 100]
]


def load_record(filename) -> list:
    with open(filename, encoding="utf-8") as file:
        line = file.read()
        lines = line.split("\n")
        record = []
        for i in range(len(lines)):
            record.append(lines[i].split(","))
    return record


if __name__ == "__main__":
    pass
