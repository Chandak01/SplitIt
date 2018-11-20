import csv

#default
N = 3

def getMin(arr):
     
    minInd = 0
    for i in range(0, N):
        if (arr[i] < arr[minInd]):
            minInd = i
    return minInd

def getMax(arr):
 
    maxInd = 0
    for i in range(0, N):
        if (arr[i] > arr[maxInd]):
            maxInd = i
    return maxInd

def minOf2(x, y):
 
    return x if x < y else y

def minCashFlowRec(amount):
    mxCredit = getMax(amount)
    mxDebit = getMin(amount)

    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0

    min = minOf2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -=min
    amount[mxDebit] += min


    
    with open('debt.csv', 'w') as writeFile:
    	writer = csv.writer(writeFile)#,quotechar='"', quoting=csv.QUOTE_MINIMAL)
    	lines[mxDebit][mxCredit] = str(int(lines[mxDebit][mxCredit]) + min)
    	writer.writerows(lines)
    
    print("Person " , mxDebit , " pays " , min
        , " to " , "Person " , mxCredit)
    minCashFlowRec(amount)

def minCashFlow(graph):

    amount = [0 for i in range(N)]

    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])
 
    minCashFlowRec(amount)
     
# Driver code

print('Enter the number of users: ')
N = int(input())

graph = [[0 for x in range(int(N))] for y in range(int(N))] 

print('Enter number of transactions: ')
e = int(input())
while(e):
	print("enter 'debtor' 'creditor' 'amount' in space separated format")
	ints = input()
	x = [int(i) for i in ints.split(" ")]
	if(len(x)!=3):
		print("enter 'debtor' 'creditor' 'amount' in space separated format")
		continue
	u,v,w = x[0],x[1],x[2]
	graph[u][v] = w
	e = e-1

print("Press 1 to update previous values")
print("Press 0 to start from fresh")
flag = int(input())

if flag==0:
	lines = [["0" for i in range(N)] for _ in range(N)]
	with open('debt.csv', 'w') as writeFile:
	    	writer = csv.writer(writeFile)#,quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    	writer.writerows(lines)

if flag == 1:
	with open('debt.csv', 'rU') as f:
		reader = csv.reader(f)
		lines = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

minCashFlow(graph)
