import matplotlib.pyplot as plt
import numpy as np

tiempo = np.linspace (0,72,73)
velocidad = np.zeros (np.size(tiempo))
for i in range (72):
              if i == 1 or i== 62:
                  a=10
              else:a=0
              velocidad[i+1]=velocidad[i]+a
              
plt.plot (tiempo,velocidad)
plt.show()