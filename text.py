from textmagic.rest import TextmagicRestClient
import csv

username = "xxx"
token = "yyy"

print('Enter no of users')
N = int(input())

with open('debt.csv', 'rU') as f:
	reader = csv.reader(f)
	data = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists
msg = ""
for e in range(N):
	print('Enter mobiles number')
	num = input()
	for n in range(N):
		if n!=e:
			msg = msg+"pay "+str(n)+" Rs"+str(data[e][n])
			msg = msg+"\n"
	
	client = TextmagicRestClient(username, token)
	message = client.messages.create(phones=num, text=msg) 

	msg = ""