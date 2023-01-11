"""
    EMR201 Support Module - SECTION 1

    :copyright: Copyright 2020-2023 by the Department of EECE,
                University of Pretoria. All rights reserved.
"""

from typing import Union
import pandas as pd

# ----------------------------------------------------------------------
# Section 1 support

available_components = {
    "resistors": [10, 27, 56, 100, 270, 360, 1000, 5600],
    "led": {"green": 4, "red": 5, "blue": 3},
    "potentiometers": [1e3, 10e3, 20e3, 50e3, 100e3],
    "capacitors": [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4],
    "inductors": [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
    "jumpers": 27,
    "battery": "1.5V rechargeable Alkaline",
    "ICs": ["OPA543", "TL084", "MCP6024"],
}


def strip_whitespace(line_list: Union[list, tuple]) -> tuple:
    email_lines = list()
    for line in line_list:
        if not isinstance(line, str):
            line = str(line)
        line.strip()
        email_lines.append(" ".join(line.split()))
    return tuple(email_lines)

def load_data(filename: str) -> pd.core.frame.DataFrame:
    return pd.read_csv(filename)


if __name__ == "__main__":
    pass
