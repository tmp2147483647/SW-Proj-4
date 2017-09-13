import pickle
import sys

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
	return scdb

def change_int(scdb): #age와 score를 int형으로 바꿔줌
	for i in scdb:
		i['Age'] = int(i['Age'])
		i['Score'] = int(i['Score'])
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
			for n in scdb:
				if n['Name'] == parse[1]:
					print(n)# 원래는 showScoreDB함수로 넘겨야 하지만 못하겠어서 바로 프린트로 출력함
					#called_name = parse[1]
					#showScoreDB(scdb[n],called_name)
		elif parse[0] == 'inc':
			for n in scdb:
				if n['Name'] == parse[1]:
					n['Score'] +=1
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
					scdb.remove(p)
					#break 제거
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			sys.exit()
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr , "=" , p[attr], end=' ') #int형으로 바꾸어 +는 사용 불가능해짐 >> ,사용
		print()
	


scoreDB = readScoreDB()
scoredb = change_int(scoreDB)
doScoreDB(scoredb)
writeScoreDB(scoredb)

