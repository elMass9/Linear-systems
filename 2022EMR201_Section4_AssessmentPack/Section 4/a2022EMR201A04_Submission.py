"""
    2022EMR201 Assignment 4
    -----------------------
    Assessment ID:          2022EMR201A04
    Date:                   2022-07-11
    Surname and initials:   Nyama, K
    Student number:         18232826
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.scimath import sqrt
from scipy import integrate
from math import pi
import math
import cmath


# -- QUESTION 1 --------------------------------------------------------

# Q1.1: Complete the matrix equation.
def store_matrix_vals() -> list:
    """Stores the resistance matrix & voltage vector values into a list.

    Args:
        No Arguments

    Returns:
        matrix_vals: list of arrays [ Array of Resistance Matrix Values,
                                      Array of Voltage Vector Values]
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Create the list of np.arrays (R,V) to return
    matrix_vals = None
    matrix_vals=[]
    R = np.array([[30,-10,0,0],
                  [-10,30,-20,0],
                  [0,-20,50,-30],
                  [0,0,-30,50]])
    V = np.array([[40],
                  [15],
                  [-20],
                  [-15]])
    matrix_vals=[R,V]
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return matrix_vals


# Q1.2: Determine the value of the current.
def solve_for_i(matrix_vals: list) -> np.array:
    """Determines the value of the current vector, by solving the matrix
    equations.

    Args:
        matrix_vals (list): list of arrays [Array of Resistance Matrix Values,
                                            Array of Voltage Vector Values]

    Returns:
        i (numpy.array): an array of the determined current vector values.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Solve the i vector
    i = None
    i = np.linalg.solve(matrix_vals[0], matrix_vals[1])
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return i


# -- QUESTION 2 --------------------------------------------------------

# Q2.1: Complete the node matrix.
def store_nodal_vals() -> list:
    """Stores the conductance matrix & current vector elements into a list.

    Args:
        No Arguments

    Returns:
        matrix_vals: list of arrays [ Array of Conductance Matrix Elements,
                                      Array of Current Vector Elements]
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Create the list of np.arrays (G,I) to return
    node_matrix_vals = None
    node_matrix_vals = []
    G = np.array([[0.001,-0.25e-3,-0.25e-3],
                  [-0.25e-3,0.001,-0.25e-3],
                  [-0.25e-3,-0.25e-3,0.0005]])
    I = np.array([[20e-3],[5e-3],[5e-3]])
    node_matrix_vals=[G,I]
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return node_matrix_vals


# Q2.2: Determine the value of the voltage.
def solve_for_v(node_matrix_vals: list) -> np.array:
    """Determines the elements of the voltage vector, by solving the matrix
    equations.

    Args:
        node_matrix_vals (list): list of arrays [Array of Conductance Matrix Elements,
                                                 Array of Current Vector Elements]

    Returns:
        v (numpy.array): an array of the determined voltage vector elements.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Solve the v vector
    v = None
    v=np.linalg.solve(node_matrix_vals[0], node_matrix_vals[1])
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return v


# -- QUESTION 3 --------------------------------------------------------

# Q3.1: Sort the Prices in ascending order (i.e. low to high) using the Bubble algorithm.
def sort_price_asc(stock_list: list) -> list:  # JL: ammended the docstring
    """Sorts the product price list in ascending order.

     Args:
        stock_list (list):  list of lists containing the list of product
                            names, followed by the list of product quantity,
                            followed by list of prices.

    Returns:
        new_stock_list (list):  list of lists containing the original lists of product
                                names and quantities, followed by the newly sorted list of
                                product prices.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Amend the prod & new price & quantity lists to a single list
    new_stock_list = None
    new_stock_list=[]
    n=len(stock_list[2])
    swap=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(stock_list[2][j]>stock_list[2][j+1]):
                swap = True
                stock_list[2][j], stock_list[2][j+1] = stock_list[2][j+1], stock_list[2][j]
        if not swap:
            return stock_list
    new_stock_list=stock_list
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return new_stock_list


# Q3.2: Sort the Quantities in descending order (i.e. high to low) using the Comb algorithm
def sort_quantities_desc(stock_list: list) -> list:  # JL: ammended the docstring
    """Sorts the product price list in descending order

     Args:
        stock_list (list):  list of lists containing the list of product
                            names, followed by the list of product quantity,
                            followed by list of prices.

    Returns:
        new_stock_list (list):  list of lists containing the list of product
                                names, followed by the newly sorted list of
                                product quantities, and then the original prices list.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

 # Amend the prod & price lists to a single list.
    new_stock_list = None
    new_stock_list=[]
    n=len(stock_list[1])
    swap=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(stock_list[1][j]<stock_list[1][j+1]):
                swap = True
                stock_list[1][j], stock_list[1][j+1] = stock_list[1][j+1], stock_list[1][j]
        if not swap:
            return stock_list
    new_stock_list=stock_list
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return new_stock_list


# Q3.3: Return the index of a specific product quantity using the Jump search algorithm
def search_quant(stock_list: list, prod_quantity: int) -> list:
    """ Searches for the given product quantity using the Jump search algorithm and returns the indices of
     where to find the product within the stock list.
     Args:
        stock_list (list):  list of lists containing the list of product
                            names, followed by the list of product quantity
                            sorted in descending order, followed by list of prices.
        prod_quantity (int): quantity to search for.
    Returns:
        quant_index (tuple): The indices of where to find the specified quantity
                             in the stock_list.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    quant_index = (None, None)
    index=0
    n=len(stock_list[1])
    step = math.sqrt(n)
    while stock_list[1][int(min(step, n)-1)] > prod_quantity:
        index = step
        step += math.sqrt(n)
        if index >= n:
            break
    while(stock_list[1][int(index)]>prod_quantity):
        index+=1
        if(index==min(step,n)):
            break
    if(stock_list[1][int(index)]==prod_quantity):
        quant_index = (1,index)
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return quant_index


# Q3.4: Return the index of a specific product name using the Linear search algorithm
def search_prod(stock_list: list, prod_name: str) -> tuple:
    """Searches for the given product name and returns the indices of
    where to find the product within the stock list.

     Args:
        stock_list (list):  list of lists containing the list of product
                            names, followed by the list of product quantity,
                            followed by list of prices.
        prod_name (str): name of product to search for.

    Returns:
        prod_index (tuple): The indices of where to find the product name
                            in the stock list.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Store the result
    prod_index = None
    prod_index =(None, None)
    n=len(stock_list[0])
    for i in range(n):
        if(stock_list[0][i]==prod_name):
            prod_index = (0,i)
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return prod_index



# -- QUESTION 4 --------------------------------------------------------

# Q4.1: Initialize initial starting conditions and store with constants
# & variables. (2 marks)
def spring_init_var(
    arm_length: int,
    body_mass: int,
    fric_coeff: float,
    spring_coeff: float,
    tau0: float,
    time_step: float,
    dur_sim_time: int,
) -> dict:
    """Store the constants and variables with initial conditions in a
    dictionary.

    Args:
        arm_length (int): Length of the rod in m.
        body_mass (int): Mass of the block in kg.
        fric_coeff  (float): Fricion coeficient in Nm*(rad/s)^(-1).
        spring_coeff (float): Spring coefficient in Nm/rad.
        tau0 (float): Initial torque (in Nm) used to calculate init_angle.
        time_step (float): Time step in s.
        dur_sim_time (int): Total time duration of the simulation in s.

    Returns:
        pend_init (dict): dictionary containing all constants & initial
                          conditions = {'arm_length' : int,
                                        'body_mass' : int,
                                        'fric_coeff': float,
                                        'spring_coeff': float,
                                        'time_step' : float,
                                        'dur_sim_time' : int,
                                        'time' : np.array,
                                        'init_angle' : float,  (in rad)
                                        'init_angular_v' : int}
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------

    # Store the variables, constants & initial parameters in this
    # dictionary using the specified dictionary keys:
    pend_init = None
    arr=np.arange(0,dur_sim_time,time_step)
    pend_init = {'arm_length':arm_length,
                 'body_mass':body_mass,
                 'fric_coeff':fric_coeff,
                 'spring_coeff':spring_coeff,
                 'time_step':time_step,
                 'dur_sim_time':dur_sim_time,
                 'tau0':tau0,
                 'time':arr,
                 'init_angle':tau0/spring_coeff,
                 'init_angular_v':0
                 }
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return pend_init

# Q4.2: Euler method for solving the torsion spring system. (5 marks)
def euler_solver(pend_init: dict):
    """Using Euler's method and Taylors expansion, solve for the rod and mass
    position and angular velocity.

    Args:
        pend_init: dict = {'arm_length'  : int,
                           'body_mass' : int,
                           'fric_coeff' : float,
                           'spring_coeff' : int,
                           'time_step' : float, 
                           'dur_sim_time' : int, 
                           'time' : np.array, 
                           'init_angle' : float, 
                           'init_angular_v' : int}
        where,  arm_length (int): Length of the arm in m.
                body_mass (int): Mass of the block in kg.
                fric_coeff  (float): Fricion coeficient in Nm*(rad/s)^(-1).
                spring_coeff (float): Spring coefficient in Nm/rad.
                time_step (float): Time step in s.
                dur_sim_time (int): Total time duration of the simulation in s.
                time (np.array): Simulation step array.
                init_angle (int): Initial angle of the mass block in radians.
                init_angular_v (int): initial angular velocity of rod.

    Returns:
        euler_output (np.array): array recording the euler output of the
                                 angle position and angular velocity for
                                 the rod and mass.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    # Write code for solving the torsion spring system problem using euler's
    # method and taylors expansion:
    euler_output = None
    def eulerFunc(z,tyd,damp,mass,spring,arm,dsndsdf):
        x1,x2=z
        guy1=damp*x2
        guy2=spring*x1
        exponentFunc=arm**2
        y1_DOT = x2
        y2_DOT = -((guy1)+(guy2))/(mass*(exponentFunc))
        theDots = [y1_DOT,y2_DOT]
        return theDots
    yInt=[pend_init["init_angle"],pend_init["init_angular_v"]]
    y1,y2=integrate.odeint(eulerFunc,yInt,pend_init["time"], args=(pend_init["fric_coeff"],pend_init["body_mass"],pend_init["spring_coeff"],pend_init["arm_length"], pend_init["dur_sim_time"])).T
    temp_euler=[]
    for i in range(len(y1)):
        temp_euler.append([y1[i],y2[i]])
    euler_output=np.array(temp_euler)
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return euler_output


# Q4.3: Plot the Euler Method Result. (4 marks)
def euler_plot(euler_output: np.array, pend_init: dict, showplotflag: bool = False):
    """Create a single plot of angular velocity and angle position of the
    torsion spring system with respect to time.

    Args:
        euler_output: array of the angle position and angular velocity of
                      the torsion spring system.
        pend_init: dict = {'arm_length' : int,
                            'body_mass' : int,
                            'fric_coeff' : float,
                            'spring_coeff' : float,
                            'time_step' : float,
                            'dur_sim_time' : int,
                            'time' : np.array,
                            'init_angle' : float,
                            'init_angular_v' : int}
        where,  arm_length (int): Length of the rod in m.
                body_mass (int): Mass of the block in kg.
                fric_coeff  (float): Fricion coeficient in Nm*(rad/s)^(-1).
                spring_coeff (float): Spring coefficient in Nm/rad.
                time_step (float): Time step in s.
                dur_sim_time (int): Total time duration of the simulation in s.
                time (np.array): Simulation step array.
                init_angle (int): Initial angle of the mass in radians.
                init_angular_v (int): initial angular velocity of mass.

    Returns:
        fig: a matplotlib figure of the angle position and angular velocity
             of the torsion spring system wrt time.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    fig = plt.figure()
    plt.title('Plot of the Position Angle & Angular Velocity wrt Time for the torsion spring system using Eulers Method')
    plt.xlabel('Time [s]')
    plt.ylabel('Magnitude')
    plt.plot(pend_init['time'],euler_output[:,0],color='green')
    plt.plot(pend_init['time'],euler_output[:,1],color='blue')
    plt.legend(['Angular Velocity','Angular Position'])
    plt.grid()
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    plt.show(block=showplotflag)
    return fig


# -- QUESTION 5 --------------------------------------------------------

# Q5.1: Define the ODEs for the series RLC circuit.
def generate_odes_eq(
    X: np.array, t: float, R: float, L: float, C: float, t_open: int
) -> np.array:
    """Calculates the ODEs for the series RLC circuit.

     Args:
        X  (np.array): the state vector containing the value of the state
                       variables [x1,x2].
        t  (float): the instantaneous time.
        R  (float): the resistance component value.
        L  (float): the inductance component value.
        C  (float): the capacitance component value.
        t_open (int): the time at which the switch is opened again.

    Returns:
        X_dot (np.array): the derivative of the state variable x1
                          followed by the derivative of the state
                          variable x2.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    X_dot = None
    x1,x2=X
    if(t<0 or t>t_open):
        x2=0
        x2dot=0
        x1dot=x2
    else:
        x1dot=x2
        x2dot=(-1*(R*C*x2+x1))/(L*C)
    X_dot=[x1dot, x2dot]
    X_dot=np.array(X_dot)
    # x1_dot = x2
    # if(t==0):
    #     x2_dot = (0-x1-(R*C*x2))/(L*C)
    # elif(t>=0 and t<=t_open):
    #     x2_dot = (-20-x1-(R*C*x2))/(L*C)
    # elif(t==t_open):
    #     x2_dot = (-20-x1-(R*C*x2))/(L*C)
    # X_dot = np.array([x1_dot,x2_dot])
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return X_dot


# Q5.2: Solve the ODEs for the series RLC circuit.
def solve_odes(
    generate_odes_eq,
    X0: np.array,
    R: float,
    L: float,
    C: float,
    t_step: float,
    t_start: int,
    t_stop: int,
):
    """Solves the ODEs for the series RLC circuit, returning
    the values for the state variables x1 and x2.

     Args:
        generate_odes_eq (function): the function defined in Q5.1 that
                                     generates the ODEs.
        X0 (np.array): initial state
        R  (float): the resistance component value.
        L  (float): the inductance component value.
        C  (float): the capacitance component value.
        t_step (float): the time step for the simulation.
        t_start (int): the start time for the simulation.
        t_stop (int): the end time for the simulation.

    Returns:
        X_1 (np.array): an array of the solved state variable x1 values
                        for the series RLC circuit integrated over the
                        specified time period.
        X_2 (np.array): an array of the solved state variable x2 values
                        for the series RLC circuit integrated over the
                        specified time period.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    # Store the solved state variable values as output variables
    X_1 = None
    X_2 = None
    time = np.arange(t_start,t_stop,t_step)
    X_1,X_2 = integrate.odeint(generate_odes_eq,X0,time, args=(R,L,C,t_stop)).T
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return X_1, X_2


# Q5.3: Determine the transient response of the RLC circuit.
def determine_damp_type(R: float, L: float, C: float, init: tuple):
    """Determines the transient response of the series RLC circuit &
    the transient equation constants/variables.

     Args:
        R  (float): the resistance component value.
        L  (float): the inductance component value.
        C  (float): the capacitance component value.
        init (tuple): the initial inductance current conditions.

    Returns:
        damp_type (string): the determined damp type (i.e. underdamped,
                            overdamped, critically damped).
        constants (np.array): an array of the constant values of the
                              transient response equation (A1, A2).
        roots (tuple): the root values of the transient response equation
                       (s1,s2).
        alpha (float): the alpha value of the series RLC circuit.
        omega_0 (float): the omega zero value of the series RLC circuit.
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    damp_type = None
    constants = None
    roots = None
    alpha = None
    omega_0 = None
    roots=()
    constants=[]
    alpha = R/(2*L)
    omega_0 = 1/(math.sqrt(L*C))
    omega_d = sqrt(omega_0**2-alpha**2)
    if(alpha>omega_0):
        s1=-alpha+sqrt(alpha**2-omega_0**2)
        s2=-alpha-sqrt(alpha**2-omega_0**2)
        B=(init[1]-s1*init[0])/(s2-s1)
        A=init[0]-B
        damp_type='overdamped'
    if(alpha==omega_0):
        s1=-alpha+sqrt(alpha**2-omega_0**2)
        s2=-alpha-sqrt(alpha**2-omega_0**2)
        A=(init[1]+(alpha*init[0]))
        B=init[0]
        damp_type='critically damped'
    if(alpha<omega_0):
        s1=-alpha+cmath.sqrt(alpha**2-omega_0**2)
        s2=-alpha-cmath.sqrt(alpha**2-omega_0**2)
        B=(init[1]+init[0])/(omega_d)
        A=init[0]
        damp_type='underdamped'
    roots=(s1,s2)
    constants=np.array([A,B])
    # roots = ()
    # constants = []
    # s1=-alpha+(cmath.sqrt(alpha**2 - omega_0**2))
    # s2=-alpha-(cmath.sqrt(alpha**2 - omega_0**2))
    # roots=(s1,s2)
    # if isinstance(s1,complex) and isinstance(s2,complex):
    #     damp_type='underdamped'
    #     a=0
    #     b = -8/abs(math.sqrt(alpha**2 - omega_0**2))
    # elif s1==s2:
    #     damp_type='critically damped'
    #     a = -320
    #     b = -8+(alpha*a)
    #     constants = np.array([a,b])
    # else:
    #     damp_type='overdamped'
    #     b = (-8+(320*s1))/(-s1+s2)
    #     a = -320 - b
    #     constants = np.array([a,b])

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return damp_type, constants, roots, alpha, omega_0


# Q5.4: Plot the RLC circuit response.
def rlc_plot(
    X1: np.array,
    t_step: float,
    t_start: int,
    t_stop: int,
    showplotflag: bool = False
):
    """Create a single plot of the voltage across the capacitor wrt time.

    Args:
        X1 (np.array): the array of voltage values over time.
        t_step (float): the time step for the simulation.
        t_start (int): the start time for the simulation.
        t_stop (int): the end time for the simulation (i.e. time switch is
                      opened).
        

        Returns:
        fig: a matplotlib figure of the i(t) and v(t).
    """
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ----------
    
    # ==== Generate the relevant plots ====
    fig = plt.figure()
    time = np.arange(t_start,t_stop,t_step)
    plt.xlabel('Time [s]')
    plt.ylabel('v(t) [V]')
    plt.plot(time,X1,color='blue',label='C Voltage')
    plt.legend()
    plt.grid(True)
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    plt.show(block=showplotflag)
    return fig
