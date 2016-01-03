[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> * **Step 1** - Import necessary libraries:
```python
import random
import thinkstats2
import thinkplot
```
>> * **Step 2** - Create a function to generate a list of random numbers between 0 and 1 of any desired length and call the function to get a list of 1000 random numbers:
```python
def randn(n):
	import random
	l = []
	for i in range(n):
		rand = random.random()
		l.append(rand)
	return l
rand1k = randn(1000)
```
>> * **Step 3** - Generate a cdf of the 1000 random numbers and plot cdf to visually inspect the result:
```python
cdf = thinkstats2.Cdf(rand1k, label = 'random cdf')
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel = 'value', ylabel = 'CDF')
```
>> * **Step 4** - Generate a pmf of the 1000 random numbers and plot pmf to visually inspect the result:
```python
pmf = thinkstats2.Pmf(rand1k, label = 'random pmf')
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel = 'value', ylabel = 'PMF')
```
>> * **Step 5** - Interpret results. If the numbers are random, we would expect the cdf to be a straight diagonal line, which is a characteristic of a uniform distribution where every value has the same probability of showing up. For the pmf, we would expect to see a rectangular shape, indicating a uniform distribution and the fact that no value has a higher probability than any other value. In this particular case, with exactly 1000 numbers randomly generated, no number should have higher than 1/1000, or .001 probability of being selected. Both of these conditions can be seen in the pdf and cdf plots generated, leading to the conclusion that the distribution is uniform and the numbers are random.
