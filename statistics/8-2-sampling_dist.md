[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> * **Step 1** - Import necessary libraries:
```python
import numpy as np
import thinkstats2
import thinkplot
import math
```
>> * **Step 2** - Define a function that generates a list of estimated lambdas based on a given number of trials and sample size for an exponential distribution. The function includes the following components:
 * Takes as input:
  * a value n that specifies the number of randomly generated numbers to be taken from the exponenential distribution in each trial
  * a value m that specifies the number of trials to be included in the experiment
  * a value lam that specifies the value of lambda for the exponential distribution in question
 * Initializes an empty list lams to collect the lambda estimate generated from each of the m trials
 * Generates a numpy array containing n randomly selected numbers from an exponential distribution with the lambda specified as an input
 * Calculates estimated lambda from the sample by dividing 1 by the mean of the array
 * Appends the estimated lambda to the list "lams" and returns that list
```python
def Estimate_exp(n, m, lam):
	lams = []
	for i in range(m):
		xs = np.random.exponential(1.0/lam, n)
		L = 1 / np.mean(xs)
		lams.append(L)
	return lams
```
>> * **Step 3** - Define a function that generates the root mean squared error based on the code provided in Thinkstats to allow calculation of standard error in the experiment(s):
```python
def RMSE(estimates, actual):
	e2 = [(estimate-actual)**2 for estimate in estimates]
	mse = np.mean(e2)
	return math.sqrt(mse)
```
>> * **Step 4** - Run an experiment using an exponential distribution with lambda of two, with 1000 trials, and a sample size in each trial of 10. Plot the resulting sampling distribution of the experiment:
```python
lams = Estimate_exp(n = 10, m = 1000, lam = 2)
cdf = thinkstats2.Cdf(lams)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel = 'estimated lambdas', ylabel = 'CDF')
```
>> * **Step 5** - Calculate the 90% confidence interval of the estimated lambdas and the standard error. **Note:** The 90% confidence interval is (1.26 , 3.94) and the standard error is 0.88:
```python
ci_90 = cdf.Percentile(5), cdf.Percentile(95)
stderr = RMSE(estimates = lams, actual = 2)
```
>> * **Step 6** - Define a function that will plot the standard error generated by a list of multiple n values in order to compare how the standard error changes if the experiment is run using different values of n:
```python
def plot_exp(n, m, lam):
	err = []
	for i in n:
		lams = Estimate_exp(i, m, lam)
		sterr = RMSE(lams, lam)
		err.append(sterr)
	thinkplot.Plot(n, err)
	thinkplot.Show(xlabel = 'sample size', ylabel = 'standard error')
```
>> * **Step 7** - Run the experiment using a list of multiple values of n, and plot the resulting standard errors against their corresponding n values, still using a lambda of 2 and 1000 trials per experiment.
```python
n_list = range(100, 1100, 100)
plot_exp(n = n_list, m = 1000, lam = 2)
```
>> * **Step 8** - Interpret results. It is clear that looking at the downward sloping line of the plot that as the sample size increases the standard error decreases significantly.

	
