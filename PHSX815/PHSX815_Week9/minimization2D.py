#####################################################################################
#                                                                                   #
#  Original Code taken from:                                                        #
#  http://scipy-lectures.org/intro/scipy/auto_examples/plot_2d_minimization.html    #
#                                                                                   #
#  Modified By:                                                                     #
#  Mohammad Ful Hossain Seikh                                                       #
#  @University of Kansas                                                            #
#  March 31, 2021                                                                   #
#                                                                                   #
#####################################################################################


"""
=========================================
Optimization of a two-parameter function
=========================================

"""
import numpy as np
from scipy import optimize
from scipy.optimize import fmin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axisartist import SubplotZero


# Define the function that we are interested in
def f(x):
    return (x[0] + 0.5)**2 + (x[1] - 1.0)**2 + x[0]*x[1]
print (fmin(f, [1, 2]))   



# Make a grid to evaluate the function (for plotting)
x = np.linspace(-4, 2)
y = np.linspace(-2, 4)
xg, yg = np.meshgrid(x, y)

for iter in range(50):
    x_min = optimize.minimize(f, x0 = [0, 0])


p1 = x_min.x[0]
p2 = x_min.x[1]
z = (p1 + 0.5)**2 + (p2 - 1.0)**2 + p1*p2

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(xg, yg, f([xg, yg]), rstride = 1, cstride = 1, cmap = plt.cm.jet, linewidth = 0, antialiased = False)
ax.scatter(p1, p2, z, color = 'red', label = 'Minimum Point')
plt.plot([], [], ' ', label = r'Minimum x, $x_m = {:.5f}$'.format(p1))
plt.plot([], [], ' ', label = r'Minimum y, $y_m = {:.5f}$'.format(p2))
plt.plot([], [], ' ', label = r'Minimum z = f(x, y), $z_m = {:.5f}$'.format(z))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title(r'2D function $z = f (x, y) = (x + 0.5)^2 + (y - 1)^2 + xy$')
plt.legend()
plt.savefig('Minimum_Function_3D.pdf')


fig2, ax2 = plt.subplots()
plt.imshow(f([xg, yg]), extent = [-4, 2, -2, 4], origin = "lower")
plt.scatter(p1, p2, color = 'red', label = 'Minimum Point')
plt.plot([], ' ', label = r'Minimum x, $x_m = {:.5f}$'.format(p1))
plt.plot([], ' ', label = r'Minimum y, $y_m = {:.5f}$'.format(p2))
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.suptitle('Minimum of a 2D Function')
plt.title(r'$f (x, y) = (x + 0.5)^2 + (y - 1)^2 + xy$')
plt.grid(color='c', alpha = 0.5, linestyle='dashed', linewidth = 0.5)
plt.colorbar()
plt.legend()
plt.savefig('Minimum_Point_2D.pdf')

plt.show()


