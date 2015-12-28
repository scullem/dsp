#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_degree_frequency(dict):
	import string
	degrees = []
	exclude = set(string.punctuation)
	for row in dict:
		s = ''.join(ch for ch in row[" degree"] if ch not in exclude)
		l = s.split()
		for item in l:
			degrees.append(item)
	d = {x: degrees.count(x) for x in degrees}
	return d

get_degree_frequency(faculty)

#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
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

#Q3. Search for email addresses and put them in a list. Print the list of email addresses.
import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_emails(dict):
	email_address = []
	for row in dict:
		email_address.append(row[" email"])
	return email_address

get_emails(faculty)


#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_unique_domains(dict):
	import re
	email_domain = []
	for row in dict:
		email_domain.append(re.search('(?<=@).*', row[" email"]).group())
	return set(email_domain)

get_unique_domains(faculty)
