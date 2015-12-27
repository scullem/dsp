import csv

faculty = csv.DictReader(open('/Users/sarah/ds/metis/prework/dsp/python/faculty.csv'))

def get_emails(dict):
	email_address = []
	for row in dict:
		email_address.append(row[" email"])
	return email_address

emails = get_emails(faculty)

f = open('emails.csv', 'w')
for item in emails:
    f.write(item + "\n")
f.close()
