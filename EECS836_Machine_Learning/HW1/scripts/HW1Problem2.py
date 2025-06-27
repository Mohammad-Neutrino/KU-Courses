from sklearn.linear_model import LinearRegression
import numpy as np

# part (a)
X = np.array([[1, 1]] * 100) # feature matrix (k, m), first 100th observations
X = np.concatenate((X, np.array([[1, 0]])), axis = 0)  # feature matrix (k, m), adding 101st observation
print('feature matrix (k, m)', X, np.shape(X))
Y = np.array([1] * 101)  # target vector (Y)
print('target vector (Y)', Y)

model = LinearRegression(fit_intercept = False)
model.fit(X, Y)
w1, w2 = model.coef_
print(f"optimal weights: w1 = {w1:.2f}, w2 = {w2:.2f}")


# part (b)
X = np.concatenate((X, np.array([[0, 1]] * 2)), axis = 0) # feature matrix (k, m), 102nd and 103rd observations
print('feature matrix (k, m)', X, np.shape(X))
Y = np.concatenate((Y, np.array([1]*2)), axis = 0) # # target vector (Y), 102nd and 103rd observations
print('target vector (Y)', Y)

model.fit(X, Y)
w1, w2 = model.coef_
print(f"optimal weights: w1 = {w1:.2f}, w2 = {w2:.2f}")