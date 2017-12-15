#Gozde DOGAN
#131044019
#CSE 321 Introduction To Algorithm Design
#HW3
#findOptimalAssistantShip


import sys

DEPARTMENT_TASK = 6

def main():
	inputTable = [[4, 8, 7, 6], [8, 5, 7, 15], [11, 4, 8, 5]]

	asst, time = findOptimalAssistantship(inputTable)
	print "\n----------------------------------"
	if(asst is None or time is None):
		print "n>r, So:"

	print "asst: ", asst
	print "time: ", time
	print "----------------------------------\n"
	

def findOptimalAssistantship(L):
	if len(L[0])>=len(L):
		asst = []
		tempL = []
	
		for i in range(0, len(L[0])):
			tempL.append(i)

		minTime = 1000

		for l in permutation(tempL):
			time = calculateTime(l, len(L), len(L[0]), L)
			if minTime >= time:
				minTime = time
				asst = l

		return asst, minTime
	else:
		return None, None



def calculateTime(l, n, r, L):
	time = 0
	for i in range(0, r):
		if l[i] >= n:
			time += DEPARTMENT_TASK
		else:
			time += L[l[i]][i]

	return time
	

def permutation(L):
	if len(L) <= 1:
		return [L]

	perm = []
	for i in range(0, len(L)):
		elm = L[i]
		subList = L[:i] + L[i+1:]

		for p in permutation(subList):
			perm.append([elm] + p)

	return perm
	
	
if __name__ == '__main__':
    main()
