"""
    2022EMR201 Assignment 1
    -----------------------
    Assessment ID:          2022EMR201A01
    Date:                   2022-07-11
    Surname and initials:   Nyama, K
    Student number:         18232826
"""

import emr201

# -- EXAMPLE OF AVAILABLE COMPONENTS DICTIONARY ------------------------------
# available_components = {
#     "resistors": [10, 27, 56, 100, 270, 360, 1000, 5600],
#     "led": {"green": 4, "red": 5, "blue": 3},
#     "potentiometers": [1e3, 10e3, 20e3, 50e3, 100e3],
#     "capacitors": [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4],
#     "inductors": [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
#     "jumpers": 27,
#     "battery": "1.5V rechargeable Alkaline",
#     "ICs": ["OPA543", "TL084", "MCP6024"],
# }

# -- QUESTION 1 --------------------------------------------------------

# Q1.1: Create required variables (2 marks)
def create_personal_variables() -> list:
    """Create and return personal details variables.

    Returns:
        list: Personal details
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    personal_details = None  # Change this line to the desired result

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return personal_details


# Q1.2: Create the requested component variables (3 marks)
def create_component_variables() -> list:
    """Create and return component details variables.

    Returns:
        list: Component details
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    component_details = None  # Change this line to the desired result

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return component_details


# -- QUESTION 2 --------------------------------------------------------

# Q2.1 Resistors (1 mark)
def get_resistor_availability(components: dict, resistance: int) -> bool:
    """Check the availability of the required resistance in the
    components dictionary.

    Args:
        components (dict): Inventory of available components
        resistance (int): Required resistance

    Returns:
        bool: Resistor available
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    enough_resistors = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return enough_resistors


# Q2.2 LED (5 marks)
def get_led_availability(components: dict, desired_colour: str, led_number_needed: int) -> tuple:
    """Check the availability of the required LED(s).

    Args:
        components (dict): Component inventory
        desired_colour (str): Required LED Colour
        led_number_needed (int): Required LED amount

    Returns:
        tuple: (
            bool: colour available,
            bool: enough in stock,
            int: num LEDs allocated
            )
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    number_of_leds_needed = None
    desired_led_colour = None
    max_available = None
    enough_LEDs = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    # Determine the amount of LEDs allocated
    if enough_LEDs:
        led_amount_allocated = number_of_leds_needed
    else:
        led_amount_allocated = max_available
    return (desired_led_colour, enough_LEDs, led_amount_allocated)


# Q2.3 Minimum and Maximum Potentiometer Values (4 marks)
def get_potentiometer_values(components: dict):
    """Get the maximum and minimum potentiometer values.

    Args:
        components (dict): Component inventory

    Returns:
        tuple: (int: max value, int: min value)
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    max_pot = None
    min_pot = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return (max_pot, min_pot)


# Q2.4 Jumper Wires (2 marks)
def get_jumper_availability(components: dict, amount_of_jumpers_needed: int) -> tuple:
    """Check the availability of the number of jumpers.

    Args:
        components (dict): Component inventory
        amount_of_jumpers_needed (int): Required jumpers

    Returns:
        tuple: (bool: enough jumpers available, int: jumpers left)
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    enough_jumpers__available = None
    amount_of_jumpers_left = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return (enough_jumpers__available, amount_of_jumpers_left)


# Q2.5 Battery (4 marks)
def get_battery_availability(
    components: dict, charge_type: str, battery_voltage: str, battery_type: str
) -> tuple:
    """Check if the battery in stock meets the requirements.
    Make the test insensitive to case.

    Args:
        components (dict): Component inventory
        charge_type (str): Battery charge type
        battery_voltage (str): Battery voltage
        battery_type (str): Battery type

    Returns:
        tuple: (bool: battery match, str: battery status)
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    battery_match = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    if battery_match:
        battery_status = components["battery"] + " Battery"
    else:
        battery_status = "The required battery is not in stock."
    return (battery_match, battery_status)


# Q2.6 High Pass RL Filter (5 marks)
def get_inductor_val(components: dict, frequency: float) -> tuple:
    """Calculate the inductor value in uH to 2 decimal places.
    Check for inductor availability.

    Args:
        components (dict): Component inventory
        frequency (float): RL filter frequency

    Returns:
        tuple: (float: capacitor value, bool: inductor availability)
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    rounded_inductor_val = None
    inductor_is_in_range = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    if inductor_is_in_range:
        availability_status = "The inductor falls within the values stocked."
    else:
        availability_status = "The inductor is not within the values stocked."
    return (rounded_inductor_val, availability_status)


# -- QUESTION 3 --------------------------------------------------------

# Q3: Draft response email (6 marks)
def generate_response_email(
    student_number: int,
    name: str,
    surname: str,
    min_resistor: int,
    rounded_inductor_val: float,
    availability_status: str,
    number_of_resistors: int,
    resistance: int,
    number_of_leds: int,
    led_colour: str,
    number_of_min_pots: int,
    min_pot: int,
    number_of_max_pots: int,
    max_pot: int,
    number_of_jumpers_needed: int,
    battery_status: str,
) -> tuple:
    """Draft a response email.

    Args:
        student_number (int): Student number
        name (str): Student name
        surname (str): Student surname
        min_resistor (int): Minimum resistor value
        rounded_inductor_val (float): Inductor value
        availability_status (str): Inductor availability status
        number_of_resistors (int): Number of resistors
        resistance (int): Resistor value
        number_of_leds (int): Number of LEDs
        led_colour (str): LED colour
        number_of_min_pots (int): Number of smallest potentiometers
        min_pot (int): Smallest potentiometer value
        number_of_max_pots (int): Number of biggest potentiometers
        max_pot (int): Biggest potentiometer value
        number_of_jumpers_needed (int): Number of jumpers needed
        battery_status (str): Battery status

    Returns:
        tuple: (str: line_1, ..., str: line_15)
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    line_1 = None
    line_2 = None
    line_3 = None
    line_4 = None
    line_5 = None
    line_6 = None
    line_7 = None
    line_8 = None
    line_9 = None
    line_10 = None
    line_11 = None
    line_12 = None
    line_13 = None
    line_14 = None
    line_15 = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    email_draft = emr201.strip_whitespace(
        [
            line_1,
            line_2,
            line_3,
            line_4,
            line_5,
            line_6,
            line_7,
            line_8,
            line_9,
            line_10,
            line_11,
            line_12,
            line_13,
            line_14,
            line_15,
        ]
    )
    return email_draft
