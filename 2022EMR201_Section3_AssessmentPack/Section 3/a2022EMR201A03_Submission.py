"""
    2022EMR101 Assignment 3 Memo
    ----------------------------
    Assessment ID:  2022EMR201A03
"""

from emr201 import load_data
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn

# -- QUESTION 1 --------------------------------------------------------

# Q2.1: Define the function pascal (5 marks)
def pascal (base : int, row : int, column : int) -> int:
    """Generates the number in pascals triangle for a given row and column for
    any base number.

    Args:
        base (int): Given base number.
        row (int): Given Row.
        column (int): Given Column.

    Returns:
        int: value corresponding to the given row and column of pascals 
        triangle given a certain base 
    """
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    if column==1:
        return base
    if column==row:
        return base
    upL = pascal(base,row-1, column-1)
    upR = pascal(base,row-1, column)
    return upL + upR
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------

# -- QUESTION 2 --------------------------------------------------------

# Q2.2.1: Calculate the simple interest investment
def get_array_simple_interest(annums: int, principle: float, rate: float) -> list:
    """Calculate the simple interest for rate 0 to 0.2.

    Args:
        annums (int): Amount of years.
        principle (float): Principle amount.
        rate (float): Interest rate.

    Returns:
        list: List of simple interest for each rate from 0 to 0.2.
    """

    simple_interest = None
    
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    simple_interest=list()
    if rate >= 0 and rate<= 0.2:
        simple_interest.insert(0,principle*(1+rate*annums))
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return simple_interest
print(get_array_simple_interest(20, 1000, 0.11))
print(get_array_simple_interest(20, 1000, 0.12))
print(get_array_simple_interest(20, 1000, 0.13))

# Q2.2.2: Calculate the compound interest investment
def get_array_compound_interest(annums: int, periods: float, principle: float, rate: float):
    """Calculate the compound interest for rate 0 to 0.2.

    Args:
        annums (int): Amount of years.
        periods (float): Interest periods (n).
        principle (float): Principle amount.
        rate (float): Interest rate (r).
        
    Returns:
        list: List of compound interest for each year from 0 to 0.2.
    """

    compound_interest = None
    
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return compound_interest


# Q2.2.3) Determine the absolute difference between the two arrays. Return the result in an array.
def get_array_difference(simple_interest: list, compound_interest: list):

    """Calculate the compound interest from year 0 till annums years.

    Args:
        simple_interest (list): Simple interest vector
        compound_interest (list): Compound interest vector.

    Returns:
        list: List of absolute difference between compound interest and simple interest.
    """

    difference = None
    
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
   
   
        
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return difference

#Q2.2.4) Plot the simple and compount interest, as well as their difference
def plot_interest(rate: float, principle_simple: float, principle_compound: float, showplotflag: bool) -> matplotlib.figure.Figure:
    """Plot the simple and compound interest, as well as their difference.
        Use the previously defined functions 'get_array_simple_interest', 
        'get_array_compound_interest' and 'get_array_difference' to obtain 
        the simple and compound interest.

    Args:
        rate (float): Interest rate used.
        principle_simple (float): Principle amount for simple interest.
        principle_compound (float): Principle amount for compound interest.
        showplotflag (bool): Flag to show or hide plot figure.

    Returns:
        tuple: (
            np.ndarray: simple,
            np.ndarray: compound,
            np.ndarray: difference,
            matplotlib.figure.Figure: Figure object of plot.
        )
    """
    
    simple = None
    compound = None
    difference = None
    
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    # Interest properties
    periods = 1
    annums = 20
    # time array
    delta = 1
    t = np.arange(0, annums + 1, delta)


 
    # Plot simple against compound + the difference --------------------
    fig = plt.figure()  ## DO NOT EDIT THIS LINE
    # Write the rest of your plotting code here ------------------------

    

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    plt.show(block=showplotflag)  # DO NOT EDIT
    return (simple, compound, difference, fig)


# -- QUESTION 3 --------------------------------------------------------

#Analysis of an Amplitude Modulated (AM) signal in different domains
# (time domain and frequency domain).
def signal_analysis(
    A_c: float,
    A_m: float,
    f_c: float,
    f_m: float,
    sampling_time: float,
    signal_duration: float,
    showplotflag: bool,)-> tuple:
    """
    Args:
        A_c: Amplitude of carrier signal.
        A_m: Amplitude of message signal.
        f_c: Frequency of the carrier signal in Hz.
        f_m: Frequency of the message signal in Hz.
        sampling_time: The ticks of time which the signal is sampled.
        signal_duration: The lifespan of the signal.
        showplotflag (bool): Flag to show or hide plot figure.

    Returns:
        tuple: A tuple containing the figure instance and the axes array.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE

    time = None
    message = None
    carrier = None  
    signal = None
    

    # Create the figure with subplots
    fig, ax = plt.subplots(None, None) #Complete this statement
    
    

    # write code above this line, DO NOT EDIT BELOW THIS LINE
    plt.show(block=showplotflag)  # DO NOT EDIT

    # write code above this line, DO NOT EDIT BELOW THIS LINE
    plt.show(block=showplotflag)  # DO NOT EDIT
    return (fig, ax)


# -- QUESTION 4 --------------------------------------------------------

# Q4.1
def plot_barChart(filename: str, showplotflag: bool) -> matplotlib.figure.Axes:

    """ Plot a barchart showing the distribution of the different engineering degrees

    Args:
        filename: name of the .csv file that needs to be imported.
        showplotflag (bool): Flag to show or hide plot figure.

    Returns:
        matplotlib.figure.Axes: The axes object (containing the plot data) that is returned from the seaborn command.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE -------
    
    data = None
    final_plot = None
    

    # Write code above this line, DO NOT EDIT BELOW THIS LINE -------
    plt.show(block=showplotflag)  # DO NOT EDIT
    return final_plot

# Q4.2
def plot_boxPlot(filename: str, showplotflag: bool) -> matplotlib.figure.Axes:

    """Plot a box plot to show the distribution of the salaries of each type of engineer. Use the following rules

    Args:
        filename: name of the .csv file that needs to be imported.
        showplotflag (bool): Flag to show or hide plot figure.

    Returns:
        matplotlib.figure.Axes: The axes object (containing the plot data) that is returned from the seaborn command.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE -------

    data = None
    final_plot = None

    # Write code above this line, DO NOT EDIT BELOW THIS LINE -------
    plt.show(block=showplotflag)  # DO NOT EDIT
    return final_plot

# Q4.3
def plot_displot(filename: str, showplotflag: bool) -> seaborn.FacetGrid:
    
    """Plot a distplot of the salary distribution between the different types of engineering with reference to the level of the degree. 
    The x parameter should be the 'Salary' attribute, the column parameter should be the 'Degree' attribute and the row parameter should be the 'Level' attribute.

    Args:
        filename: name of the .csv file that needs to be imported.
        showplotflag (bool): Flag to show or hide plot figure.

    Returns:
        seaborn.FacetGrid: The grid object (containing the plot data) that is returned from the seaborn command.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE -------

    data = None
    final_plot = None     

    # Write code above this line, DO NOT EDIT BELOW THIS LINE -------
    plt.show(block=showplotflag)  # DO NOT EDIT
    return final_plot

