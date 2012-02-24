#encoding=utf8
import random

l1 = []

while len(l1) < 100000:
    l1.append(random.randrange(-10000000, 1000000)

def find():
'''
    add your code
'''
    count = 0;   
    for i in range(len(l1)):
	    for j in range(1,len(l1)):
		    if l1[i] + l1[j] == 0:
			    count++
			    print l1[i] + '+' l1[j] + '=0'
    count = count / 2
if __name__ == '__main__':
    find()


