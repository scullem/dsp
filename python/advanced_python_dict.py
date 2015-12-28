#Q6. Create a dictionary in the below format:
#Create a dictionary using last name as the key

import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_faculty_tuple_ln(dict):
	import re
	l=[]
	for row in dict:
		l.append((row["name"].split()[-1], [row[" degree"].lstrip(), re.search(r'.*(?=\s(is|of)\s)', row[" title"]).group(), row[" email"]]))
	return l

fac_tuples_ln = get_faculty_tuple_ln(faculty)

dict_ln = {}
for key, val in fac_tuples_ln:
    dict_ln.setdefault(key, []).append(val)

print dict_ln
print dict_ln.items()[:3]


#Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
#Create a dictionary using first name, last name as the key

import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_faculty_tuple_fn_ln(dict):
	import re
	l=[]
	for row in dict:
		l.append(((row["name"].split()[0],row["name"].split()[-1]), row[" degree"].lstrip(), re.search(r'.*(?=\s(is|of)\s)', row[" title"]).group(), row[" email"]))
	return l

fac_tuples_fn_ln = get_faculty_tuple_fn_ln(faculty)
dict_fn_ln = {a:[b,c,d] for a,b,c,d in fac_tuples_fn_ln}

print dict_fn_ln
print dict_fn_ln.items()[:3]

#Q8. It looks like the current dictionary is printing by first name. Sort by last name and print the first 3 key and value pairs.
#Create a dictionary ordered by last name, using first name, last name as the key

import csv
from collections import OrderedDict

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_faculty_tuple_fn_ln_sort(dict):
	import re
	l=[]
	for row in dict:
		l.append(((row["name"].split()[0],row["name"].split()[-1]), [row[" degree"].lstrip(), re.search(r'.*(?=\s(is|of)\s)', row[" title"]).group(), row[" email"]]))
	return sorted(l, key=lambda tup: tup[0][1])

fac_tuples_fn_ln_sort = get_faculty_tuple_fn_ln_sort(faculty)
dict_fn_ln_sort = OrderedDict(fac_tuples_fn_ln_sort)

print dict_fn_ln_sort
print dict_fn_ln_sort.items()[:3]
