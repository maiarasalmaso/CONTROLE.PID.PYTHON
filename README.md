# PID CONTROL USING PYTHON
The theoretical material was produced based on the book Process Dynamics and Control by the author Dale E. Seborg. 

### Conceptualizing
The image illustrates a closed-loop PID control system, which will be our focus. Here, the controller adjusts the manipulated variable (inlet flow rate) to maintain the controlled variable (tank level) at the desired setpoint. The transmitter measures the level (ym) and sends the signal to the controller, which compares it with the setpoint (ysp), calculates the error, and applies proportional, integral, and derivative control actions. The controller then generates an output signal (p) to adjust the control valve, ensuring that the tank level remains stable and close to the desired value.

![image](https://github.com/user-attachments/assets/9826e1e1-2770-433d-b61f-fe96b448ab45)

We will study the proportional, integral, and derivative control of a storage tank. Our goal is to define a setpoint (the tank's level height) and control it through a manipulated variable, which will be the inlet flow rate. Below, we can analyze the system we are studying along with its dynamic model equation, initial conditions, and parameters. 

The dynamic model equation of a system is obtained from the analysis of mass, energy, and momentum balances. In this material, we will not perform this analysis, as our focus is solely on studying PID control.

![image](https://github.com/user-attachments/assets/2562c030-9dbe-410b-a7fd-b707e8626b13)

![image](https://github.com/user-attachments/assets/2d5e9c67-1268-4119-858a-398a291154c5)

![image](https://github.com/user-attachments/assets/aecb441b-317f-41d1-b709-2ac80fd53263)

![image](https://github.com/user-attachments/assets/1af3b2cb-fbd6-4da6-96a9-5e52dc545017)

#### PID CONTROL 

The PID control is based on correcting the error between the desired value (setpoint) and the measured value (actual tank level). This control uses three main actions:

Proportional Control (P): Responds instantly to the current error. If the tank level is below the setpoint, the controller increases the inlet flow rate proportionally to the error. The problem with proportional control alone is that it can generate a permanent error (offset), where the level never exactly reaches the setpoint.

Integral Control (I): Considers the accumulated error over time, eliminating the offset caused by proportional control. If the tank level remains below the setpoint for an extended period, the integral term accumulates this error and increases the control action to correct the difference. However, excessive tuning of the integral gain can cause oscillations in the tank level.

Derivative Control (D): Acts on the rate of change of the error, predicting future trends and adjusting the control action to reduce oscillations. In the case of the tank, if the level is rising rapidly, the derivative term can reduce the inlet flow rate before the system exceeds the setpoint. However, it is sensitive to noise in the measurement and should be used with caution.

#### PID Equation Parameters

![image](https://github.com/user-attachments/assets/5ef9dfa5-1dab-4af9-bc39-f577480e898f)


- **(p(t))** → Controller output signal (e.g., control signal for adjusting the inlet valve).  
- **(bar{p})** → Mean value of the control signal (can be an operating point).  
- **(K_c)** → Proportional gain, which adjusts the intensity of the correction based on the error.  
- **(e(t) = y_{sp} - y_m)** → Error between the setpoint and the controlled variable.  
- **(tau_I)** → Integral time constant, responsible for eliminating persistent errors.  
- **(tau_D)** → Derivative time constant, which improves response by anticipating error changes.  


### Solving the system's ODE

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import solve_ivp

    
    # Given parameters
    A = 0.3  # m^2
    Rv = 19.5  # min/m^2
    qe_0 = 0.015  # m^3/min
    h_0 = 0.2925  # m

    

    # Differential equation function
    def dh_dt(t, h):
    q = (1 / Rv) * h  # Outflow equation
    return (qe_0 - q) / A  # ODE


    # Time span for simulation
    t_span = (0, 10)  # Simulating for 10 minutes
    t_eval = np.linspace(0, 10, 100)  # Time points for evaluation


    # Solving the ODE
    solution = solve_ivp(dh_dt, t_span, [h_0], t_eval=t_eval, method='RK45')


    # Extracting results
    t_values = solution.t
    h_values = solution.y[0]


    # Plotting results
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, h_values, label="Water Level h(t)")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Water Level (m)")
    plt.title("Water Level Over Time in the Tank")
    plt.legend()
    plt.grid()
    plt.show()
    
### Solving witch PID
