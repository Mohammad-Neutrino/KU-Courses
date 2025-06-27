import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# decision function
def z1(x1, x2):
    return 4 * x1 + 6 * x2 - 24

#  sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def calculate_accuracy(data, w1, w2, b):
    TP, TN, FP, FN = 0, 0, 0, 0
    for (x1, x2, label) in data:
        z_value = w1 * x1 + w2 * x2 + b
        prediction = 1 if z_value >= 0 else 0
        if label == 1 and prediction == 1:
            TP += 1
        elif label == 0 and prediction == 0:
            TN += 1
        elif label == 0 and prediction == 1:
            FP += 1
        elif label == 1 and prediction == 0:
            FN += 1
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    return accuracy


# data format: (x1, x2, label); label = 1 (positive) or 0 (negative)
data = [ (1.5, 4, 1), (2, 2, 1), (3, 3, 1), (4, 5, 1), (3, 7, 1), (8, 5, 1), (8, -1, 1), 
       (-1, 3, 0), (-1, 5, 0), (4, 1, 0), (5, 1, 0), (-5, 1, 0), (-3, 5, 0), (-2, -2, 0), (7, -1, 0)
       ]



# initial weights and bias
w1, w2, b = 4, 6, -24  

print(f"initial decision function: z(x1, x2) = {w1:.2f}x1 + {w2:.2f}x2 + {b:.2f}") 
accuracy = calculate_accuracy(data, w1, w2, b)
print(f"initial accuracy: {accuracy * 100:.2f}%")


learning_rate = 0.01
epochs = 1000

# gradient descent to optimize weights and bias
for epoch in range(epochs):
    dw1, dw2, db = 0, 0, 0  
    for (x1, x2, label) in data:
        z = w1 * x1 + w2 * x2 + b
        p = 1 / (1 + np.exp(-z)) 
        error = p - label  
        dw1 += error * x1
        dw2 += error * x2
        db += error

    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2
    b -= learning_rate * db
    
print(f"optimized decision function: z(x1, x2) = {w1:.2f}x1 + {w2:.2f}x2 + {b:.2f}")    
accuracy = calculate_accuracy(data, w1, w2, b)
print(f"optimized accuracy: {accuracy * 100:.2f}%")


# decision boundary (z = 0)
x1_values = np.linspace(-6, 9, 100)  
x2_values = (24 - 4 * x1_values) / 6  
plt.plot(x1_values, x2_values, color = "orchid", label = "Decision Boundary (z = 0)")

positive_points = [(x1, x2) for (x1, x2, label) in data if label == 1]
negative_points = [(x1, x2) for (x1, x2, label) in data if label == 0]
plt.scatter(*zip(*positive_points), color = "g", marker = "+", s = 100, label = "Positive")
plt.scatter(*zip(*negative_points), color = "r", marker = "x", s = 70, label = "Negative")

plt.text(3.2, 3.2, r'${\bf A}$')
plt.xticks(np.arange(-6, 10, 1))
plt.yticks(np.arange(-4, 9, 1))

plt.xlabel("x1")
plt.ylabel("x2")
plt.axhline(0, color = "k", ls = "--", linewidth = 0.5) 
plt.axvline(0, color = "k", ls = "--", linewidth = 0.5) 
plt.grid(True, ls = "--", alpha = 0.5)
plt.legend(fontsize = 8)
plt.tight_layout()
plt.savefig('DecisionLine.png', dpi = 400)
plt.show()