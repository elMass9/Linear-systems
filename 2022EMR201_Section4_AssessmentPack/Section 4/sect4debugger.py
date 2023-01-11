from a2022EMR201A04_Submission import generate_odes_eq
import a2022EMR201A04_Submission as s
import numpy as np

if __name__ == "__main__":
    # ------------------------------------------------------------------
    # Question 1
    # ------------------------------------------------------------------
    # Question 1.1
    print(" store_matrix_vals ".center(80, "-"))
    matrix_vals = s.store_matrix_vals()
    print(f"Result type:  {type(matrix_vals)}")
    print(f"Result value: {matrix_vals}")

    # Question 1.2
    print(" solve_for_i ".center(80, "-"))
    i = s.solve_for_i(matrix_vals)
    print(f"Result type:  {type(i)}")
    print(f"Result value: {i}")

    # ------------------------------------------------------------------
    # Question 2
    # ------------------------------------------------------------------
    # Question 2.1
    print(" store_nodal_vals ".center(80, "-"))
    node_matrix_vals = s.store_nodal_vals()
    print(f"Result type:  {type(node_matrix_vals)}")
    print(f"Result value: {node_matrix_vals}")

    # Question 2.2
    print(" solve_for_i ".center(80, "-"))
    v = s.solve_for_v(node_matrix_vals)
    print(f"Result type:  {type(v)}")
    print(f"Result value: {v}")

    # ------------------------------------------------------------------
    # Question 3
    # ------------------------------------------------------------------
    # Question 3.1
    print(" sort_price_asc ".center(80, "-"))
    prod_list = [
        "Saw",
        "Screwdriver",
        "Knife",
        "555-Timer",
        "Op-amp",
        "Breadboard",
        "9V-battery",
        "Microcontroller",
        "Plier",
        "Tweezer",
    ]
    price_list = [60, 50, 45, 100, 200, 20, 250, 50, 80, 110]
    quantity_list = [12, 5, 13, 1, 24, 10, 8, 3, 4, 20]
    stock_list = [prod_list, quantity_list, price_list]
    print(f"Stock List B4 Adj: {stock_list}")
    new_stock_list = s.sort_price_asc(stock_list)
    print(f"Result type:  {type(new_stock_list)}")
    print(f"Result value: {new_stock_list}")

    # Question 3.2
    print(" sort_quantities_desc ".center(80, "-"))
    stock_list = new_stock_list
    print(f"Stock List B4 Adj: {stock_list}")
    new_stock_list = s.sort_quantities_desc(stock_list)
    print(f"Result type:  {type(new_stock_list)}")
    print(f"Result value: {new_stock_list}")

    # Question 3.3
    print(" search_quant ".center(80, "-"))
    stock_list = new_stock_list
    prod_quantity = 1000  # change this to one any of the values in the list above
    print(f"Stock List B4 Adj: {stock_list}")
    quant_index = s.search_quant(stock_list, prod_quantity)
    print(f"Result type:  {type(quant_index)}")
    print(f"Result value: {quant_index}")

    # Question 3.4
    print(" search_prod ".center(80, "-"))
    stock_list = new_stock_list
    print(f"Stock List B4 Search: {stock_list}")
    prod_name = "Sdfdf"
    prod_index = s.search_prod(stock_list, prod_name)
    print(f"Result type:  {type(prod_index)}")
    print(f"Result value: {prod_index}")

    # ------------------------------------------------------------------
    # Question 4
    # ------------------------------------------------------------------
    # Question 4.1
    print(" spring_init_var ".center(80, "-"))
    arm_length = 2
    body_mass = 1
    fric_coeff = 1
    spring_coeff = 2
    time_step = 0.02
    dur_sim_time = 100 * time_step
    tau0 = 12.5663
    pend_init = s.spring_init_var(
        arm_length,
        body_mass,
        fric_coeff,
        spring_coeff,
        tau0,
        time_step,
        dur_sim_time
    )
    print(f"Result type:  {type(pend_init)}")
    print(f"Result value: {pend_init}")

    # Question 4.2
    print(" euler_solver ".center(80, "-"))
    euler_output = s.euler_solver(pend_init)
    print(f"Result type:  {type(euler_output)}")
    print(f"Result value: {euler_output}")

    # Question 4.3
    print(" euler_plot ".center(80, "-"))
    showplotflag = True
    fig = s.euler_plot(euler_output, pend_init, showplotflag=showplotflag)
    print(f"Result type:  {type(fig)}")
    print(f"Result value: {fig}")

    # ------------------------------------------------------------------
    # Question 5
    # ------------------------------------------------------------------
    # Question 5.1
    print(" generate_odes_eq ".center(80, "-"))
    X = (0,0)
    t = 1  # test different times
    R = 10
    L = 4
    C = 0.25
    t_open = 10
    t_step = 0.001
    t_start = 0
    t_stop = 10
    X0 = np.array([0, -8])
    X_dot = s.generate_odes_eq(X, t, R, L, C, t_open)
    print(f"Result type:  {type(X_dot)}")
    print(f"Result value: {X_dot}")

    # Question 5.2
    print(" solve_odes ".center(80, "-"))

    X_1, X_2 = s.solve_odes(generate_odes_eq, X0, R, L, C, t_step, t_start, t_stop)
    print(f"Result type:  {type(X_1)}")
    print(f"Result value: {X_1}")
    print(f"Result type:  {type(X_2)}")
    print(f"Result value: {X_2}")

    # Question 5.3
    print(" determine_damp_type ".center(80, "-"))
    R = 10  # test different values here, make sure to check all cases
    L = 4
    C = 0.25
    X0 = np.array([0, -8])
    damp_type, constants, roots, alpha, omega_0 = s.determine_damp_type(
        R, L, C, X0
    )
    print(f"Result type:  {type(damp_type)}")
    print(f"Result value: {damp_type}")
    print(f"Result type:  {type(constants)}")
    print(f"Result value: {constants}")
    print(f"Result type:  {type(roots)}")
    print(f"Result value: {roots}")
    print(f"Result type:  {type(alpha)}")
    print(f"Result value: {alpha}")
    print(f"Result type:  {type(omega_0)}")
    print(f"Result value: {omega_0}")

    # Question 5.4
    print(" rlc_plot ".center(80, "-"))
    showplotflag = True
    fig = s.rlc_plot(X_1, t_step, t_start, t_stop, showplotflag=showplotflag)
    print(f"Result type:  {type(fig)}")
    print(f"Result value: {fig}")
