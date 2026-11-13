# Actividad Formativa 4: Implementación y Análisis de un Sistema de Modulación en Amplitud (AM)

**Estudiante:** Ana Karina Villanueva Haro  
**Materia:** Sistemas de Comunicación / Telecomunicaciones  

## Descripción del proyecto
Este repositorio contiene la simulación en Python de un sistema de modulación en amplitud de doble banda lateral con portadora completa (**AM DSB-LC**). El objetivo es analizar el comportamiento de una señal modulada tanto en el **dominio del tiempo** como en el **dominio de la frecuencia (FFT)**, evaluando su desempeño frente a condiciones reales de transmisión: ruido, atenuación y distorsión por sobremodulación.

## Requisitos e instalación
El script está desarrollado en Python 3 y requiere las siguientes librerías científicas:
* `numpy`
* `scipy`
* `matplotlib`

Para instalarlas ejecuta en tu terminal:
```bash
pip install numpy scipy matplotlib
```

## Ejecución
Para correr la simulación y generar las gráficas de análisis:
```bash
python ACTIVIDAD4.py
```

## Escenarios analizados
1. **Señal Mensaje $m(t)$:** Onda cosenoidal de baja frecuencia ($50\text{ Hz}$).
2. **Modulación AM Ideal:** Portadora de $1000\text{ Hz}$ modulada con un índice $k_a = 0.8$.
3. **Espectro de Frecuencia (FFT):** Identificación de la portadora ($1000\text{ Hz}$) y las bandas laterales ($950\text{ Hz}$ y $1050\text{ Hz}$).
4. **Ruido Blanco Gaussiano (AWGN):** Impacto de interferencias aditivas en la amplitud de la señal.
5. **Atenuación:** Pérdida del $70\%$ de la amplitud simulando la distancia en el canal.
6. **Distorsión por Sobremodulación:** Inversión de fase producida al utilizar un índice $k_a = 1.8 > 1$.
