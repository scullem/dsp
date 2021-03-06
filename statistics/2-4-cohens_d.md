[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>* **Step 1** - Import libraries, read in nsfg dataset, and create dataframes to subset out live first births and live other births:
>>```python
import thinkstats2
import nsfg
import pandas as pd
import math
nsfg = nsfg.ReadFemPreg()
first = nsfg[(nsfg.outcome == 1) & (nsfg.birthord == 1)]
other = nsfg[(nsfg.outcome == 1) & (nsfg.birthord != 1)]
```
>>* **Step 2** - Recreate the function defined in Thinkstats to compute Cohen's d:
>>```python
def CohenEffectSize(group1, group2):
  diff = group1.mean() - group2.mean()
  var1 = group1.var()
  var2 = group2.var()
  n1, n2 = len(group1), len(group2)
  pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
  d = diff / math.sqrt(pooled_var)
  return d
```
>>* **Step 3** - Call Cohen's d function on totalwgt_lb for first and other subsets to calculate effect size of the difference in total birth weight between first births and other births:
>>```python
CohenEffectSize(first.totalwgt_lb, other.totalwgt_lb)
```
>>* **Step 4** - Interpret result. The effect size as the difference in means for birth weight between first and other live births is approximately -.089 standard deviations. Ignoring the direction of the difference, this is approximately 3 times the value of the same metric applied to pregnancy length. This suggests that birth weight might be more likely than pregnancy length to have a correlation with birth order. Although these cutoffs are arbitrary, a rule of thumb can be applied to interpret a Cohen's d value of .2 as a small effect, .5 as a medium effect, and .8 as a large effect (http://rpsychologist.com/d3/cohend/). Given that the birth weight value is less than .2, I would not draw the conclusion that that birth order is correlated with birth weight for a live birth.
