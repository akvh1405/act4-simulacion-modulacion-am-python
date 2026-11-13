import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# ==============================================================================
# 1. DEFINICIÓN DE PARÁMETROS Y SEÑALES DE ENTRADA
# ==============================================================================
fs = 10000          # Frecuencia de muestreo (Hz) - cumple Nyquist con holgura
t = np.linspace(0, 0.1, int(fs * 0.1), endpoint=False) # Vector de tiempo (0.1 s)

fm = 50             # Frecuencia de la señal mensaje (Hz) - Baja frecuencia
Am = 1.0            # Amplitud del mensaje

fc = 1000           # Frecuencia de la señal portadora (Hz) - Alta frecuencia
Ac = 1.0            # Amplitud de la portadora

ka = 0.8            # Índice de modulación (0 < ka <= 1 evita sobremodulación)

# Señal del mensaje m(t) y señal portadora c(t)
mensaje = Am * np.cos(2 * np.pi * fm * t)
portadora = Ac * np.cos(2 * np.pi * fc * t)

# ==============================================================================
# 2. IMPLEMENTACIÓN DE LA MODULACIÓN AM (DSB-LC)
# ==============================================================================
# Ecuación estándar de modulación AM: s(t) = Ac * [1 + ka * m(t)] * cos(2*pi*fc*t)
senal_am = Ac * (1 + ka * mensaje) * np.cos(2 * np.pi * fc * t)

# ==============================================================================
# 3. ESCENARIOS DE ANÁLISIS: RUIDO, ATENUACIÓN Y DISTORSIÓN
# ==============================================================================
# Escenario A: Ruido Blanco Gaussiano Aditivo (AWGN)
np.random.seed(42)
ruido = np.random.normal(0, 0.4, len(t))
am_con_ruido = senal_am + ruido

# Escenario B: Atenuación (pérdida del 70% de amplitud por distancia/canal)
factor_atenuacion = 0.3
am_atenuada = senal_am * factor_atenuacion

# Escenario C: Distorsión por sobremodulación (ka > 1, inversión de fase)
ka_sobre = 1.8
am_distorsionada = Ac * (1 + ka_sobre * mensaje) * np.cos(2 * np.pi * fc * t)

# ==============================================================================
# 4. CÁLCULO DEL ESPECTRO EN FRECUENCIA (FFT)
# ==============================================================================
def calcular_espectro(senal, fs):
    N = len(senal)
    yf = fft(senal)
    xf = fftfreq(N, 1 / fs)[:N // 2]
    magnitud = 2.0 / N * np.abs(yf[0:N // 2])
    return xf, magnitud

f_am, spec_am = calcular_espectro(senal_am, fs)
f_ruido, spec_ruido = calcular_espectro(am_con_ruido, fs)

# ==============================================================================
# 5. VISUALIZACIÓN DE RESULTADOS (TIEMPO Y FRECUENCIA)
# ==============================================================================
plt.figure(figsize=(14, 10))

# Gráfica 1: Señal Mensaje antes de la modulación
plt.subplot(3, 2, 1)
plt.plot(t[:500], mensaje[:500], color='blue')
plt.title('1. Señal Mensaje m(t) - Dominio del Tiempo (50 Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.grid(True)

# Gráfica 2: Señal Modulada AM Ideal
plt.subplot(3, 2, 2)
plt.plot(t[:500], senal_am[:500], color='green', label='Señal AM')
plt.plot(t[:500], Ac * (1 + ka * mensaje[:500]), 'r--', label='Envolvente')
plt.title('2. Señal Modulada AM Ideal (ka = 0.8)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.legend(loc='upper right')
plt.grid(True)

# Gráfica 3: Espectro de Frecuencia AM Ideal
plt.subplot(3, 2, 3)
plt.plot(f_am, spec_am, color='purple')
plt.xlim(800, 1200) # Zoom alrededor de la portadora (1000 Hz)
plt.title('3. Espectro de Frecuencia AM Ideal (FFT)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)

# Gráfica 4: Impacto del Ruido (Tiempo)
plt.subplot(3, 2, 4)
plt.plot(t[:500], am_con_ruido[:500], color='gray')
plt.title('4. Señal AM con Ruido Blanco Gaussiano (AWGN)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.grid(True)

# Gráfica 5: Impacto de la Atenuación
plt.subplot(3, 2, 5)
plt.plot(t[:500], senal_am[:500], 'g--', alpha=0.5, label='Original')
plt.plot(t[:500], am_atenuada[:500], color='orange', label='Atenuada (30%)')
plt.title('5. Señal AM con Atenuación')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.legend(loc='upper right')
plt.grid(True)

# Gráfica 6: Distorsión por Sobremodulación
plt.subplot(3, 2, 6)
plt.plot(t[:500], am_distorsionada[:500], color='red')
plt.title('6. Distorsión por Sobremodulación (ka = 1.8)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.grid(True)

plt.tight_layout()
plt.show()
