import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Parâmetros do processo
# -----------------------------
A = 0.3                # Área do tanque (m²)
Rv = 19.5              # Resistência da válvula (min/m²)
h0 = 0.2604            # Nível inicial do tanque (m)
qe0 = 0.015            # Vazão de entrada inicial (m³/min)

qemax = 0.040          # Vazão máxima (m³/min)
qemin = 0              # Vazão mínima (m³/min)

qe = qe0
h = h0

# -----------------------------
# Parâmetros da simulação
# -----------------------------
delta_t = 0.1          # Passo de tempo (min)
tempo_total = 500       # Tempo total (min)
n = int(tempo_total / delta_t)

# -----------------------------
# Parâmetros do controlador PI
# -----------------------------
setpoint = 0.35        # Nível desejado (m)
Kc = 0.00095          # Ganho proporcional
tau_I = 20             # Tempo integral (min)
erro = 0
erro1 = 0

# -----------------------------
# Função do modelo do tanque
# -----------------------------
def tanque(h, qe):
    q = h / Rv
    dh_dt = (qe - q) / A
    return dh_dt

# -----------------------------
# Função do controlador PI
# -----------------------------
def controlePI(CV, MV, setpoint):
    global erro, erro1
    erro = setpoint - CV
    erro1 += erro * delta_t
    return MV + Kc * (erro + erro1 / tau_I)

# -----------------------------
# Inicializações com NumPy
# -----------------------------
tempos = np.linspace(0, tempo_total, n)
niveis = np.zeros(n)
entradas = np.zeros(n)

# Condições iniciais
h = h0
MV = qe0

# -----------------------------
# Simulação
# -----------------------------
for i in range(n):
    niveis[i] = h
    entradas[i] = MV

    dh_dt = tanque(h, MV)
    h += dh_dt * delta_t

    #mudanca de setpoint
    if tempos[i] >= 150:
        setpoint = 0.38  # Novo setpoint

    # Segunda mudança de setpoint após 4 minutos
    if tempos[i] >= 250:
        setpoint = 0.32  # Novo setpoint

    MV = controlePI(h, MV, setpoint)
    MV = np.clip(MV, qemin, qemax)  # Garante que está nos limites

plt.figure(figsize=(10, 6))
plt.plot(tempos, niveis)
plt.xlabel('Tempo (min)')
plt.ylabel('Nível (m)')
plt.title('Resposta do Nível do Tanque')
plt.grid(True)
plt.show()
