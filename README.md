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

The values presented for the PID controller are the initial values used in the system configuration. The proportional gain (**Kc**) was set to **10**, the integral time (**TauI**) to **4 minutes**, and the derivative time (**TauD**) to **0.1 minute**.

The presented graph shows the PID control applied to the water level in a tank, with a change in the setpoint over time. Initially, the water level starts around 0.40m. After 40 minutes, an abrupt change in the setpoint is observed, indicated by the dashed red line, signaling an increase in the desired water level. In response, the system rapidly increases the water level to approximately 0.50m, with the PID controller trying to adjust the value according to the reference. After this increase, the water level shows small oscillations around the new setpoint.

![image](https://github.com/user-attachments/assets/f345a3a8-3750-4521-ac8f-c5651a8223a6)

The graph shown illustrates the PID control applied to the water level in a tank, with a change in the setpoint over time, and is configured with a proportional gain \( K_c = 0.1 \).

As in the previous graph, the water level starts around 0.40 meters (represented by the blue line) until a change in the setpoint occurs, indicated by the dashed red line, which rises to 0.50 meters after 40 minutes. The PID system responds quickly to the increase in the setpoint, causing the water level to rise to the new desired value.

![image](https://github.com/user-attachments/assets/7b64de55-c2a9-4698-89c2-e00b6f9cff7f)


### Conclusion

The study of PID control applied to the water level in a tank demonstrated the effectiveness of this control method in maintaining the water level close to the desired value (setpoint). The PID control continuously adjusts the manipulated variable (inlet flow rate) to correct the error between the measured value and the desired value, using proportional, integral, and derivative actions.

Through the analysis of the presented graphs, we can observe how the system responds to changes in the setpoint. Initially, the water level starts around 0.40 meters and, after the abrupt change in the setpoint to 0.50 meters, the PID system rapidly increases the water level to the desired value. However, PID control also exhibits small oscillations around the setpoint after this increase, which is expected due to the interaction of the three components of the controller (P, I, and D).

Additionally, the configuration of the PID controller with a proportional gain Kc = 0.1 was sufficient to provide a quick system response, but it also showed that fine-tuning the control might be necessary to reduce oscillations and improve stability. Adjusting the PID parameters, such as \( \tau_I \) and \( \tau_D \), can further optimize the system’s performance and ensure that the water level remains stable without large fluctuations.

Therefore, PID control is a powerful tool for dynamic systems like this, offering an efficient way to control variables, but also requiring careful adjustments of parameters to achieve the desired performance and minimize issues like excessive oscillations.
