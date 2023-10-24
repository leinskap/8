import numpy as np
import matplotlib.pyplot as plt
with open('settings.txt', 'r') as settings:
    tmp = [float(x) for x in settings.read().split('\n')]
freq = tmp[0]
volt = tmp[1]
voltage = np.loadtxt('data.txt', dtype=float)
time = np.linspace(0, len(voltage), len(voltage))
time = time * freq
fig, ax = plt.subplots(figsize=(16,10), dpi = 100)
ax.set_xlabel('Время, c')
ax.set_ylabel('Напряжение, В')
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке')
ax.set_xlim(0, 9)
ax.set_ylim(0, 3)
ax.plot(time, voltage, label = 'V(t)', color = 'blue', linewidth = 1, marker = '.')
ax.scatter(time[::10], voltage[::10], color ='blue', marker = '.')
fig.savefig('figure.svg')
ax.legend()
ax.grid(which = 'major')
ax.grid(which = 'minor', linestyle = ':')
ax.minorticks_on()
chargeTime = round((len(voltage) - np.argmax(voltage[::-1])) * freq, 2)
dischargeTime = round(max(time) - chargeTime, 2)
ax.text(6, 2.03, 'Время зарядки конденсатора = ' + str(chargeTime) + ' c')
ax.text(6, 1.93, 'Время разрядки конденсатора = ' + str(dischargeTime) + ' c')
plt.show()
