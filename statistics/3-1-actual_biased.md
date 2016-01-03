[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> * **Step 1** - Import necessary libraries and the the female respondent file using code specified in Thinkstats:
```python
import thinkstats2
import nsfg
import pandas as pd
import math
import thinkplot
import chap01soln
nsfg_resp = chap01soln.ReadFemResp()
```
>> * **Step 2** - Define the function provided in Thinkstats that uses the actual distribution of the number of households with a certain number of children to build a the biased distribution that would result from actually sampling children to find out how many below to a household with a certain number of children. Note: the code includes the following: * Takes as an input the actual pmf and the desired label for the new, biased pmf * Creates a copy of the actual pmf, assigning it the new label * For each response value and it's probability in the actual pmf, multiplies the probability by the response value. For example, all of the households with 0 children are multiplied by 0 and therefore are no longer represented in the biased pmf. If there are no children in the household, there would be no children to sample to represent 0 child households * Normalize the new pmf so that all of the new response value - probability pairings add up to 1 again
```python
def BiasPmf(pmf, label):
	new_pmf = pmf.Copy(label=label)
	for x, p in pmf.Items():
		new_pmf.Mult(x, x)
	new_pmf.Normalize()
	return new_pmf
```
>> * **Step 3** - Create pmfs for the actual and biased cases and calculate the average number of children in a household for the actual pmf and the biased pmf to compare the difference. The mean for the actual pmf is 1.02, while it is more than double at 2.40 for the biased pmf
```python
pmf_actual = thinkstats2.Pmf(nsfg_resp.numkdhh, label = 'actual')
pmf_obs = BiasPmf(pmf_actual, label = 'observed')
print('Actual Mean: ' + str(pmf_actual.Mean()))
print('Biased Mean: ' + str(pmf_obs.Mean()))
```
>> * **Step 4** - Plot the actual and biased pmfs to make a visual comparison. It is clear in comparing the two pmfs that the actual pmf is most heavily concentrated at 0 children, while the biased pmf has no observations at 0 children and is heavily weighted toward 2+ children
```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, pmf_obs])
thinkplot.Show(xlabel='class size', ylabel='PMF')
```
