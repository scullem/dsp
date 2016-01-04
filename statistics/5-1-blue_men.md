[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> * **Step 1** - Import necessary libraries:
```python
import scipy
```
>> * **Step 2** - Define a function to easily convert measurement in feet & inches to centimeters, given that the data is measured in centimeters and the question is state in feet + inches:
```python
def feet_in_to_cm(ft, inch):
	total_in = inch + ft * 12
	cm = 2.54 * total_in
	return cm
```
>> * **Step 3** - Define a function that takes two heights for a population with a given mean and standard deviation and returns the percent of the population between the two heights. The function uses the following components:
 * Takes as inputs two different heights specified in feet and inches as well as the mean and standard deviation of the population in question
 * Converts the feet and inches provided for each of the two height inputs to centimeters
 * Uses the cdf of the normal distribution with the population mean and standard deviation inputs for each of the heights provided to calculate the percentile of each and returns the difference between the second height and the first height provided
```python
def perc_pop(ft1, inch1, ft2, inch2, mu, sig):
	height1 = feet_in_to_cm(ft1, inch1)
	height2 = feet_in_to_cm(ft2, inch2)
	perc =  scipy.stats.norm.cdf(height2, loc = mu, scale = sig) - scipy.stats.norm.cdf(height1, loc = mu, scale = sig)
	return perc
```
>> * **Step 4** - Call the function to calculate the percent of the US male population that is between the height range of 5'10" and 6'1".
```python
mu_m = 178
sig_m = 7.7
perc_pop(ft1 = 5, inch1 = 10, ft2 = 6, inch2 = 1, mu = mu_m, sig = sig_m)
```
>> * **Step 5** - Interpret results. The function returns a value approximately equal to 34%. This means that 34% of the US male population is in teh appropriate height range to join Blue Man Group.
