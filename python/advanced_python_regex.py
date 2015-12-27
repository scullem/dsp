#Q1 -- in progress



#Q2
import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_titles_frequency(dict):
	import re
	title = []
	for row in dict:
		title.append(re.search(r'.*(?=\s(is|of)\s)', row[" title"]).group())
	d = {x: title.count(x) for x in title}
	return d

get_titles_frequency(faculty)

#Q3
import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_emails(dict):
	email_address = []
	for row in dict:
		email_address.append(row[" email"])
	return email_address

get_emails(faculty)


#Q4
import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_unique_domains(dict):
	import re
	email_domain = []
	for row in dict:
		email_domain.append(re.search('(?<=@).*', row[" email"]).group())
	return set(email_domain)

get_unique_domains(faculty)
