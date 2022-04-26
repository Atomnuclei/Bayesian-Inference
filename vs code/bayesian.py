from numpy import random, array, exp, sqrt, pi
import matplotlib.pyplot as plt

from pylab import plot,show
import seaborn as sns


x_points=random.normal(0,2,size=100)
sns.displot(x_points,kind='kde')
#gaussian_dist=random.normal(size=100)
#print(gaussian_dist)


def sumsq(array):
    'doc string: it returns the sum of the squares of the elements in the array'
    
    summation=0
    for x in array:
        summation+= x*x
    return summation

#documentation

def a_fun(a,sum_of_squares_of_data,array_lenght):
    
    return 1/(2* pi*a)**(array_lenght/2)*exp(-sum_of_squares_of_data/(2*a))


a_fun(1,sumsq(x_points),len(x_points))