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

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import solve_ivp

    
    # Parâmetros do sistema
    m = 0.2  # Massa da esfera (kg)
    rho_ar = 1.225  # Densidade do ar (kg/m^3)
    A_esfera = np.pi * (0.05)**2  # Área de seção transversal da esfera (m^2)
    g = 9.81  # Aceleração devida à gravidade (m/s^2)
    CD = 1  # Coeficiente de arrasto
    k = 0.2  # Constante de proporcionalidade para a velocidade do ar (m/s), 0 para anular esse efeito
    u = 2.146*10**-5 # viscosidade dinamica do ar kg/(m.s)
    var0inicial = 3
    var0 = 3
    Fgrav = m*g

    # Parâmetros do sistema
    A = 0.3  # m^2
    Rv = 19.5  # min/m^2
    h_0 = 0.2925  # m (nível inicial de água)
    
    # Parâmetros do controlador PI
    Kc = 0.11  # Ganho proporcional
    TauI = 4  # Tempo integral (min)
    TauD = 0.1  # Tempo derivativo (min)
    MV0 = 0.015  # Valor inicial da variável manipulada (qe_0)
    setpoint_inicial = 0.4  # Setpoint inicial (m)
    setpoint_final = 0.5  # Setpoint final (m)
    MV_min = 0.0  # Valor mínimo da variável manipulada
    MV_max = 0.03  # Valor máximo da variável manipulada
    
    # Variáveis globais para o controlador PI
    erroI = 0.0
    erro_anterior = 0.0
    delta_t = 0.1  # Passo de tempo (min)
    
    # Tempo total de simulação e passo de tempo
    tempo_total = 100  # minutos
    delta_t = 0.1  # minutos
    
    # Cria um array de tempo
    t = np.arange(0, tempo_total, delta_t)


    # Função do controlador PID
    def ControlePID(CV, MV, setpoint):
        global erroI, erro_anterior
        erro = setpoint - CV  # Erro atual ACAO REVERSA!!!!!!!!!!!!!
    
        # Ação Proporcional (P)
        acao_P = Kc * erro
    
        # Ação Integral (I)
        erroI += erro * delta_t
        if i == 1:  # Resetar o termo integral no primeiro passo
            erroI = 0
        acao_I = Kc * (1 / TauI) * erroI
    
        # Ação Derivativa (D)
        derivada_erro = (erro - erro_anterior) / delta_t
        acao_D = Kc * TauD * derivada_erro
    
        # Cálculo da variável manipulada (MV)
        MV = MV0 + acao_P + acao_I + acao_D
        # Aplicar limites físicos ao MV
        MV = np.clip(MV, MV_min, MV_max)  # Limita MV entre MV_min e MV_max
    
        # Atualiza o erro anterior
        erro_anterior = erro
    
        return MV  # Return only the calculated MV value
        # Função da EDO do sistema
        def dh_dt(h, t, qe):
            q = (1 / Rv) * h  # Vazão de saída
            return (qe - q) / A  # EDO
            
        # Arrays para armazenar resultados
        h_values = np.zeros_like(t)  # Nível de água
        qe_values = np.zeros_like(t)  # Vazão de entrada (MV)
        setpoint_values = np.zeros_like(t)  # Valores do setpoint ao longo do tempo
        
        # Condição inicial
        h_values[0] = h_0
        qe_values[0] = MV0
        setpoint_values[:] = setpoint_inicial  # Setpoint inicial
        
        # Definir o instante em que o setpoint muda
        tempo_mudanca_setpoint = 40  # Tempo em que o setpoint muda (minutos)
        
        # Loop de simulação
        for i in range(1, len(t)):
            # Alterar o setpoint no tempo especificado
            if t[i] >= tempo_mudanca_setpoint:
                setpoint_values[i] = setpoint_final
            else:
                setpoint_values[i] = setpoint_inicial
        
            # Atualiza a variável manipulada (MV) usando o controlador PI
            qe_values[i] = ControlePID(h_values[i - 1], qe_values[i - 1], setpoint_values[i]) # Assign only the MV value to qe_values[i]
        
            # Resolve a EDO para o próximo passo de tempo
            sol = odeint(dh_dt, h_values[i - 1], [t[i - 1], t[i]], args=(qe_values[i],))
            h_values[i] = sol[-1][0]  # Extrai o valor escalar do array
            # Gráfico 1: Nível de água e setpoint
        plt.figure(figsize=(8, 8))
        plt.plot(t, h_values, label="Nível de Água h(t)")
        plt.plot(t, setpoint_values, 'r--', label="Setpoint")
        plt.xlabel("Tempo (minutos)")
        plt.ylabel("Nível de Água (m)")
        plt.title("Controle PID do Nível de Água no Tanque com Mudança de Setpoint")
        plt.legend()
        plt.show()
