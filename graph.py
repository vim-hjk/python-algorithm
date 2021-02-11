import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/gulim.ttc").get_name()

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [7.736, 6.284, 6.336, 7.177, 7.025, 6.224, 6.191, 6.26, 6.134, 7.062]
plt.title('AR Program Loading time', fontproperties = font_name)

plt.axis([1, 10, 1, 10])
plt.plot(x_values, y_values, 'r')

plt.xlabel('Iteration')
plt.ylabel('Time')

plt.legend()

plt.grid(True)
plt.show()