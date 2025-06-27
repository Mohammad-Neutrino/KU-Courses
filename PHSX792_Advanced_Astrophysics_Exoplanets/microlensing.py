import numpy as np
import matplotlib.pyplot as plt

t_E = 10

t = np.linspace(-10, 10, 1000)

u_0 = 0.1
u = np.sqrt(u_0**2 + (t/t_E)**2)
a = u**2 + 2
b = u*np.sqrt((u**2)+4)
A = a/b
half = max(A)/2
T = 2*1.75869

fig, ax = plt.subplots()

plt.plot(t, A, 'ko-', lw = 0.7, markersize = 2, label = r"A(u), $t_E = 3.52$ Weeks, $u_0 = 0.1$")
ax.axhline(half, color = 'k', ls = '--', lw = 0.9)
ax.axvline(-1.75869, color = 'k', ls = '--', lw = 0.9)
ax.axvline(1.75869, color = 'k', ls = '--', lw = 0.9)
plt.annotate(s = '', xy = (-1.75869, 5.01848), xytext = (1.75869, 5.01848), arrowprops = dict(arrowstyle='<|-|>'))
plt.text(-0.2, 4.6, r'$t_E$')
plt.grid(color = 'k', alpha = 0.5, linestyle = 'dotted', linewidth = 0.6)
plt.xlabel(r'Time, t (Weeks)')
plt.ylabel(r'Magnification, $A(u) = \frac{u^2 + 2}{u \sqrt{(u^2 + 4)}}$')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fancybox=True, shadow=True)
plt.savefig('microlensing.pdf')
plt.show()
