import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	for p in scdb:
		intDB(p,scdb) # Age,Score Integer 변환
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]
		elif parse[0] == 'find':
			for p in scdb:
				if p['Name'] == parse[1]:
					print(p)				
						
					
	#	scdb에서 remove(p)를 하면 딕셔너리가 왼쪽으로 들어오게 됨(마지막 값 제거가 안됨)	
	#	elif parse[0] == 'del':
	#		for p in range(-1,len(scdb[p]),1):#그래서 역순 출력 시도
	#			if scdb[p]['Name'] == parse[1]:
	#				scdb.remove(p) #역순출력 시도 실패
		# 원래 코드
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
					scdb.remove(p) 
		
		elif parse[0] == 'inc':
			for p in scdb:
				if p['Name'] == parse[1]:
					intDB(p,scdb) #integer 변환
					p['Score'] += int(parse[2])
						
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" , p[attr], end=' ')
		print()
def findScoreDB(p):
	
		print(p)	

def intDB(p,scdb):
	for p in scdb:
		p['Age'] = int(p['Age'])
		p['Score'] = int(p['Score'])


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

