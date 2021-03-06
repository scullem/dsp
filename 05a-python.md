# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequence types, and can be used with similar types of operations. They can both contain values of any type (integer, float, string, etc.), and they are indexed by integers.
>>
>>There is one major difference between lists and tuples that is inherent to the two different sequence types. Tuples are immutable (cannot be modified once created) and lists are mutable (can be modified). So you can’t delete or sort tuples once created. Because they are immutable, tuples can be used as keys in dictionaries, whereas lists cannot. A dictionary requires that a key be "hashable". The hash function takes any kind of value and returns an integer that is used to store and look up its key-value pairs. If keys were permitted to be mutable, this could create problems in terms of recording location. As such, lists can be used as values in dictionaries but not keys.
>>
>>Because of this inherent difference, they are used somewhat differently in practice:
>>
>>* Their elements are typically accessed by different methods. Tuples are typically accessed by unpacking their elements, where lists are typically (not always) accessed by iterating over the list.
* Lists are usually homogenous (although they are able to contain mixtures of data types), and tuples are typically heterogeneous (the different entries have different meanings). 
 * For example, where a list n = [1,2] might refer to a set of numbers, a tuple n = (1,2) might refer to the x-y coordinates of a location. In this case, the order (although we may care about order) of the numbers in the list can be changed without changing the meaning of each number, whereas changing the order of the numbers of the tuple would change the meaning.
* Tuples are typically handled as a coherent unit, whereas the elements of a list are often dealt with individually


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they are both mutable, can support some of the same operations (sum(), len(), in, etc.) and can contain a mix of data types. Performance is faster in a set for determining if an object is present in the set but lists work better if there is a need to iterate over the elements. The improved speed for finding an element in sets is because the set uses a hash table as its underlying structure.
>> 
>> Their key differences are as follows:
* Lists can contain any type of object, where sets can only contain objects that are hashable. This means a set cannot contain lists, dictionaries or other sets as its elements because they are all mutable (unless the set is a frozen set)
* Lists can contain duplicate elements, where sets cannot contain duplicates
* Lists are ordered, where sets are unordered
Sets allow operations from math set theory like intersection, union, difference
* Lists are accessed via indexes, where sets are accessed via hash tables
>> 
>> Lists are appropriate in cases with the following requirements:
* Need a collection of data all in one place, especially if you want to mix types of objects or accept any type of object.
* Need data to be ordered
* Need to modify or extend the data (add, remove, replace elements). For example, if you need a stack or a queue, lists can be easily manipulated to add/remove from the beginning or end of a list.
* Do not need data to be indexed by a custom value (like a key in a dictionary). Lists have a numeric index and the numeric position is required to retrieve an element.
* Do not need/want data to be unique. 
>> 
>> Sets are appropriate in cases with the following requirements:
* Need a unique set of data. Sets check the uniqueness of elements based on hashes, and will remove duplicates when creating a set object is created.
* Expect data to change. Sets are mutable.
* Need to perform mathematical operations like difference, union, intersection, etc.
* Do not need to store nested lists, sets, or dictionaries in a data structure. These are all mutable and therefore not hashable.
>> 
>> Note: Helpful reference: http://www.codersgrid.com/2013/06/19/introduction-to-list-set-tuple-and-dictionary-in-python/

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python’s lambda function is an anonymous function, meaning it is not bound to a name. It is often used with concepts like filter(), map(), and reduce().
>> 
>> A lambda function can accomplish similar tasks to a normal function, but has several key features:
* The lambda function does not include a return statement, but rather contains an expression that is returned
* A lambda definition can can be put anywhere a function is expected
* The lambda does not need to be assigned to a variable
* Lambda is not appropriate in cases where a function is too complex to write in a single line or where the function will be reused multiple times
>>
>>Examples: 
* Using filter:
 * l = [1, 2, 5, 19, 40], print filter(lambda x: x % 2 == 0, l) --> [2, 40] 
 * filters a list to return only those elements divisible by 2
* Using map:
 * l = [1, 2, 5, 19, 40], print map(lambda x: x + 1, l) --> [2, 3, 6, 20, 41]
 * converts a list to one where each element is increased by the value of one
* As a key in sorted:
 * sorted(tuples, key = lambda x: x[-1])
 * Given a list of tuples, sorts the list based on the last value in each tuple


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used to construct lists, essentially a compact for-loop for list building where at each iteration an element is appended to the list being built. They can be nested inside other list comprehensions to accomplish more complex tasks in a single statement, but this can easily become difficult to read.
>> 
>> The basic structure of a list comprehension is: [ <output value>  for <element> in <list>  <optional criteria>  ]. Given a list l = [1, 2, 3], the list comprehension [x **2 for x in l if x > 1] returns [4, 9]
>> 
>> * Example compared to map: l = [‘This’, ‘is’, ‘a’, ‘list’, ‘of’, ‘words’], build a list of lists where each list element contains the uppercase, lowercase, and length of each word in l
 * List comprehension - example = [[w.upper(), w.lower(), len(w)] for w in l]
 * Map with lambda - example = map(lambda w: [w.upper(), w.lower(), len(w)], l)
* Example compared to filter: l = [1, 2, 3, 4, 5, 6, 7, 8, 9], filter the list to contain only values less than 7
 * List comprehension - example = [x for x in l if x < 7]
 * Filter with lambda - example = filter(lambda x: x < 7, l)
>> 
>> It is generally not advisable to use list comprehensions in cases where the rules of construction are too complicated to be expressed with "for" and "if" statements. In this case, it is better to use map() or filter() with the appropriate function. Oftentimes, a list comprehension is more efficient and easier to read, in which cases it is preferable to use the list comprehension.
>> 
>> * Dictionary comprehension:
 * Follows a basic structure of: {<key>: <value> for <element> in <list> <optional criteria>}
 * For example, given a list of tuples where each tuple contains four elements the first of which is the key for the dictionary: d = {a:[b,c,d] for a,b,c,d in tuples}
* Set comprehension:
 * Allows the creation of a set without using the set() function, following a basic structure of: {<output value>  for <element> in <list>  <optional criteria>}
 * For example, create a set of numbers 0-19: s = {x for x in range(20)}


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

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





