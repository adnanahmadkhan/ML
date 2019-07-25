# y = mx + b
# m = best fit slope
# b = y intercept

# m = ((x'.y') - (x.y)') / ((x')^2 - (x^2)')
# b = 

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5,6,7], dtype=np.float64)
ys = np.array([9,7,4,1,-5,-6,-7], dtype=np.float64)

print("list of xs: {}".format(xs))
print("list of ys: {}".format(ys))

plt.scatter(xs, ys)
plt.show()



def best_fit_slope_and_intercept(xs, ys): 
    m =  ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
    ((mean(xs) * mean(xs)) - mean(xs*xs)) )
    
    b = mean(ys) - m*mean(xs)
    return m, b

m, b = best_fit_slope_and_intercept(xs, ys)

print("Calculated values of m & b are : m={}, b={}".format(m, b))


regression_line = np.array([m*x + b for x in xs])

predict_x = 8
print("Predicting value of y for x=8")
predict_y = (m*predict_x + b)
print("Value of y={}".format(predict_y))
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.scatter(predict_x, predict_y, color='green')
plt.show()



def squared_error(ys_orig, y_line):
    return sum((y_line - ys_orig)**2)

def coefficient_of_determination(ys_orig, y_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_reg = squared_error(ys_orig, y_line)
    squared_error_y_mean = squared_error(y_mean_line, y_line)
    return 1 - (squared_error_reg / squared_error_y_mean)

r_squared = coefficient_of_determination(ys, regression_line)
print("R squared error/Coefficient of determination is: {}".format(r_squared))
