[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> * **Step 1** - Import necessary libraries, read in nsfg pregnancy dataset, and create a subset dataset for only live births:
```python
import thinkstats2
import nsfg
import pandas as pd
import numpy as np
import math
import thinkplot
#Read data
nsfg = nsfg.ReadFemPreg()
live = nsfg[nsfg.outcome == 1]
```
>> * **Step 2** - Calculate quick summary stats for the agepreg and totalwgt_lb variables to identify what ranges makes sense for the scatter plot axes. **Note:** It looks like the age axis can be set from 10-50 and the weight axis can be set from 0-16:
```python
#10 - 50
live.agepreg.describe()
#0-16
live.totalwgt_lb.describe()
```
>> * **Step 3** - Create a scatter plot and a hexbin plot to examine the potential relationship between age and birth weight. **Note:** The scatter and hexbin for the two variables plotted against each other is a horizontal blob.
```python
#Scatter
thinkplot.Scatter(live['agepreg'], live['totalwgt_lb'])
thinkplot.Show(xlabel = 'Mother\'s Age', ylabel = 'Birth Weight', axis = [10, 50, 0, 16])
#Hexbin
thinkplot.HexBin(live['agepreg'], live['totalwgt_lb'])
thinkplot.Show(xlabel = 'Mother\'s Age', ylabel = 'Birth Weight', axis = [10, 50, 0, 16])
```
>> * **Step 4** - Plot the 25th, 50th, and 75th percentiles of birth weight against age in one consolidated chart as a second way to visualize a potential relationship between the two variables. **Note:** All of the three plotted lines are flat, horizontal lines.
```python
live_sub = live.dropna(subset = ['agepreg', 'totalwgt_lb'])
bins = np.arange(10, 50, 5)
indices = np.digitize(live_sub.agepreg, bins)
groups = live_sub.groupby(indices)
age = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
	weight = [cdf.Percentile(percent) for cdf in cdfs]
	label = '%dth' % percent
	thinkplot.Plot(age, weight, label = label)
thinkplot.Show(xlabel = 'Mother\'s Age', ylabel = 'Birth Weight', axis = [10, 50, 0, 16])
```
>> * **Step 5** - Calculate the Pearson and Spearman Rank correlations (using pandas Series functionality) as an additional check on whether the two variables are correlated. **Note:** The Pearson correlation comes in at 0.068 and the Spearman Rank correlation comes in at 0.094.
```python
#Pearson correlation (default method)
live['agepreg'].corr(live['totalwgt_lb'])
#Spearman correlation
live['agepreg'].corr(live['totalwgt_lb'], method = 'spearman')
```
>> * **Step 6** - Interpret results. There is no indication of a correlation between the age of the mother and birth weight. This is suggested by both the flat, horizontal shapes of the scatter, hexbin, and percentile plots and the correlations calculations that are practically 0.
