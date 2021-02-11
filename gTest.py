import matplotlib.pyplot as plt


X = [1, 2, 3]
Y = [1, 2, 3]

plt.plot(X, Y, label='Initialize')
plt.plot(X, [5, 7, 9], '--', label='Groung truth')
plt.legend(loc=2)
plt.show()


plt.plot([a for a in range(-60, 61)], [b*b for b in range(-60, 61)])
plt.axis('off')
plt.xlabel('W')
plt.ylabel('Cost')
plt.show()

