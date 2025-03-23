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


### Solving the system's PID

![image](https://github.com/user-attachments/assets/6a239630-eaa0-4462-9a30-29764add1835)

I tested different values of **Kc** to see where the system would settle. Initially, **Kc was 2**. Since there were many oscillations — indicating that the value was too high — I reduced it to **0.00048**. It was necessary to increase the simulation time to **300 minutes** to better visualize where the system would stabilize, which occurred at around **150 minutes**. Therefore, I inserted a change in the loop to increase the setpoint by **+3**, i.e., sp = 38 when t >= 150.

The next step was to increase the simulation time to **400 minutes** to better visualize the settling behavior. It was observed that the system had very slow responses — the settling time for the second setpoint was 300 minutes, and the first one didn’t even become stable due to oscillations. So, I increased the value of **Kc** to **0.00048**, and we can see that the system reached stability in both setpoints. In the first, the system settled in approximately **100 seconds**; in the second, the response time was reduced and the system settled in **250 seconds**.

Then, at **250 seconds**, I introduced another setpoint change of **-6**, that is, setpoint = 32. There were some oscillations, and the settling time for the first setpoint was **150 seconds**. For the second, the system practically did not stabilize, and in the third, it settled in about **360 seconds**. Since there were oscillations before the system stabilized, it was a sign that **Kc** was too low, so I increased it to **0.00095**. This showed an improvement in response time. For better visualization, I reduced the previously extended simulation time from **700 to 500 seconds**.

It is worth noting that in the third setpoint, there were no changes in response speed — it remained at **360 seconds**. In the second setpoint, the response time decreased to **220 seconds**, while in the first, it was also reduced to **150 seconds**.

Another important point is that **overshoots** occurred. In the first and third setpoints, there were **two positive and two negative overshoots**. In the second setpoint, **two positive and one negative overshoot** were observed.
