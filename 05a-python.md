# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequence types, and can be used with similar types of operations. They can both contain values of any type (integer, float, string, etc.), and they are indexed by integers.
>>
>>There is one major difference between lists and tuples that is inherent to the two different sequence types. Tuples are immutable (cannot be modified once created) and lists are mutable (can be modified). So you can’t delete or sort tuples once created. Because they are immutable, tuples can be used as keys in dictionaries, whereas lists cannot. A dictionary requires that a key be "hashable". The has function that takes any kind of value and returns an integer that is used to store and look up its key-value pairs. If keys were permitted to be mutable, this could create problems in terms of recording location. As such, lists can be used as values in dictionaries but not keys.
>>
>>Because of this inherent difference, they are used somewhat differently in practice:
>>
>>* Their elements are typically accessed by different methods. Tuples are typically accessed by unpacking their elements, where lists are typically accessed by iterating over the list.
* Lists are usually homogenous (although they are able to contain mixtures of data types), and tuples are typically heterogeneous (the different entries have different meanings). 
** For example, where a list n = [1,2] might refer to a set of numbers, a tuple n = (1,2) might refer to the x-y coordinates of a location. In this case, the order (although we may care about order) of the numbers in the list can be changed without changing the meaning of each number, whereas changing the order of the numbers of the tuple would change the meaning.
* Tuples are typically handled as a coherent unit, whereas the elements of a list are often dealt with individually


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





