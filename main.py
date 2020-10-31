import matplotlib.pyplot as plt
import numpy as np

def normal(mu,sigma2) :
  # Add code to generate a normal random variable here
  

expectation, variance = 1, 0.5
indices, svariance = np.zeros(200), np.zeros(200)
val = normal( expectation, variance )
n, ssum, ssum2 = 1, val, val*val
for i in range(1,200) : 
  # Add code to calculate the variance from n normal random variables here and to thus 
  # set the elements of the list called average.  Also write code to set the elements 
  # of the list called indices. 
  
  
  
# This will plot the graph for the data
plt.plot( indices, svariance, 'b.' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.plot( [0,200], [variance,variance], 'r-')
plt.savefig("variance_normal.png")
