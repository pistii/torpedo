import random 
from itertools import chain

enemyships = []
playerships = []

gameOver = False
startGame = True

hajo_egysegek = [1, 2, 3, 4]
total_ships = len(hajo_egysegek)
Xsize, Ysize = 10, 10
full_block= Xsize*Ysize
coords = list(range(1, full_block+1))
playerPoints, enemyPoints = 0,0

horizontal = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

enemyshipsBoard = [["O" for y in range(Ysize)] for x in range(Xsize)]
playershipsBoard = [["O" for y in range(Ysize)] for x in range(Xsize)]
tip = None
nextRound = "player"


def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
     

def generate_ship(numShip):
	
	x=0
	enemy = []

	while x != total_ships:
		randomEnemy = randomDirection(random_place(), hajo_egysegek[x] )
		#ellenőrzi hogy a randomEnemy lista felbontása után bármelyik item szerepel-e az enemy listában
		check = any(item in chain.from_iterable(enemy) for item in randomEnemy)
		#ha igaz akkor új kordinátát hoz létre
		if check is True:
			
			randomEnemy = randomDirection(random_place(), hajo_egysegek[x] )
		#ha hamis hozzáadja az ellenség hajóihoz
		else:
			
			enemyships.append(randomEnemy)
			enemy.append(randomEnemy)
			x+=1
	print(enemyships)



def randomDirection(cord, hajo_egyseg):
	#irány, hogy a hajó melyik irányba nem nézhet
	#0: balra
	left = random.choice([1, 2, 3])
	#1: feln
	up = random.choice([0, 2, 3])
	#2: jobbra
	right = random.choice([0, 1, 3])
	#3: le
	down = random.choice([0, 1, 2])
	
	irany = None
	x=False

	while x != True:
		if cord + (hajo_egyseg*10) > 100:
			cord = random_place()
		else:
			x = True
	#0-9ig felső sor
	if cord < 10:
		if cord == 0:
			cord += 1
			irany = random.choice([0, 1])
		if cord == 9:
			irany = random.choice([2, 1])
		else:
			irany = down

	#89-től 99ig alsó sor
	if cord > 89:
		if cord == 90:
			irany = random.choice([3, 0])
		if cord == 100:
			irany = random.choice([3, 2])
		else:
			irany = up
	#jobb oldal
	if cord %10==0:
		irany = right
	#bal oldal
	if cord %9==0:
		irany = left
	else:
		irany = random.randrange(0, 3)


	#növeli a hajó egységét az iránytól függően
	egyseg = cord
	egysegek= []

	for x in range(hajo_egyseg):
		if irany == 0:
			egyseg += 1 
		if irany == 1:
			egyseg += 10
		if irany == 2:
			egyseg +=  1
		if irany == 3:
			egyseg += 10
		
		egysegek.append(egyseg)
	
	return egysegek
	egysegek.clear()



def random_place():
	#egy koordinátát ad vissza ahol még nincs hajó
	cord = random.choice(coords)
	enemyfoglalt = []

	while True:
		if cord not in enemyfoglalt:
			enemyfoglalt.append(cord)
			return cord
			break		
		else:
			cord = random.choice(coords)



def playerCoords():
	one_ship=[]
	foglalt_cords = []
	direction = 0

	for x in range(total_ships):
		try: #abban az esetben ha a bekért adat nem szám
			while len(playerships) != hajo_egysegek[x]:
				playership = int(input(f'Add meg hogy hová szeretnéd lerakni a(z) {x+1}. {hajo_egysegek[x]} egységes hajót: '))
				pCoord = list(str(playership))
				
				if playership>0 and playership<Xsize*Ysize: #megfelelő-e a coord
					if len(playerships) == 0: # ha még nincs hajó
						playerships.append([playership])
						foglalt_cords.append(playership)
												
						#hajó kiírása
						for elem in pCoord:
							if playership < 10:
								playershipsBoard[0][int(pCoord[0])-1] = "H" #y kordináta 0 x kordináta játékos által megadott első elem
							elif playership == 10:
								playershipsBoard[0][9] = "H"
							else:
								if elem[-1] == "0":
									playershipsBoard[int(pCoord[0])-1][9] = "H"	
								else:
									playershipsBoard[int(pCoord[0])][int(pCoord[1])-1] = "H"

					else:
						direction = int(input('Milyen irányba szeretnéd lerakni a hajót?\n0: balra, 1: felfelé, 2: jobbra, 3: lefelé  |'))

						#Balra
						#10-től 100-ig és 1-től 10-ig
						if (direction == 0 and playership-hajo_egysegek[x] in range(int(pCoord[0])*10, int(pCoord[0])*10 + 10)) or (direction == 0 and playership-hajo_egysegek[x] in range(1, 10)):
							for i in range(playership, playership-hajo_egysegek[x], -1):
								one_ship.append(i)
						#fel
						if direction == 1 and playership-(10*hajo_egysegek[x]-10) in range(0, 100):
							for i in range(playership, playership-(10*hajo_egysegek[x]), -10  ):
								one_ship.append( i )
						#jobbra
						#10-től 100-ig és 1-től 10-ig
						if (direction == 2 and playership+hajo_egysegek[x]-1 in range(int(pCoord[0])*10, int(pCoord[0])*10 + 11)) or (direction == 2 and playership+hajo_egysegek[x] in range(1, 10)):
							for i in range(playership, playership+hajo_egysegek[x] ):
								one_ship.append(i)
						#lefelé
						if direction == 3 and playership+(hajo_egysegek[x]*10-10) in range(0, 100):
							for i in range(playership, playership+(10*hajo_egysegek[x]), 10 ):
								one_ship.append ( i )

						#print('össz:', playerships)	
						#print('egyes hajók: ', one_ship)
						#print('hajoegyseg: ', hajo_egysegek[x])
						

						#kész hajók hozzáadása
						if len(one_ship) == hajo_egysegek[x]:
							foglalt_cords.append(playership)
							playerships.append(one_ship)
						else:
							one_ship.clear()
				else:
					print('Ide nem tehetsz hajót! ')

				#játékos koordinátája alapján az X (hajó egységek) kiíratása
				for elem in one_ship:
					szam = list(str(elem))
					if elem < 10:
						playershipsBoard[0][int(szam[0])-1] = "H" #y kordináta 0 x kordináta játékos által megadott első elem
					else:
						if szam[-1] == "0":
							playershipsBoard[int(szam[0])-1][9] = "H"	
						else:
							playershipsBoard[int(szam[0])][int(szam[1])-1] = "H"
						


			one_ship = []
			prev = None
			print("Játékos hajói lerakva: ", playerships)

			for x in range(len(playershipsBoard)):

				print(" ".join(playershipsBoard[x]))


			

		except ValueError: 
			print("Hiba. Adj meg másik értéket")




def possible_places():
	#A playerCoords ennek a továbbfejlesztett változata, erre a metódusra már nincs szükség
	prev = None
	hminimum, hmaximum = 0,0
	vminumum, vmaximum = 0,0
	one_ship=[]
	vertical = bool() #feltételezzük hogy vízszintesen rak a játékos
	#ha ez a feltétel igaz akkor a horiz listát használjuk
	foglalt_cords = []
	playershipTip = 0

	for x in range(total_ships):
		try: #abban az esetben ha a bekért adat nem szám
			
			while len(one_ship) != hajo_egysegek[x]:
				playership = int(input(f'Add meg hová szeretnéd lerakni a(z) {x+1}. {hajo_egysegek[x]}-es hajót: '))
				possible = [playership-1, playership+1, playership+10, playership-10]


				if playership>0 and playership<100: #megfelelő-e a coord
					if prev == None:
						prev = playership
					
					if prev != None:
						hminimum, hmaximum = prev - hajo_egysegek[x]+1, prev + hajo_egysegek[x]-1
						vminimum, vmaximum = prev - (hajo_egysegek[x]-1)*10, prev + (hajo_egysegek[x]-1)*10
						

						#a minimum vagy maximum koordináta ne essen a táblán kívülre
						if hminimum<0:
							hminimum = 0
						if hmaximum>100: 
							hmaximum = 100

						if vminimum<0:
							vminimum = 0
						if vmaximum>100:
							vmaximum = 100

						
						if playership == hminimum or playership == hmaximum or len(one_ship) == 0:
							if len(one_ship) == 0:
								vertical = False
						if playership == vminimum or playership == vmaximum:
							if len(one_ship) == 0:
								vertical = True

					
					#####################Vízszintes ###########
					if vertical == False:
						print(f'min: {hminimum} max: {hmaximum}')

						if hminimum<=playership<=hmaximum and playership not in foglalt_cords:
							one_ship.append(playership)
							playershipTip = list(str(playership))
							foglalt_cords.append(playership)
					
							#####  koordináták ellenőrzése 
							if int(playership) <10:
								playershipsBoard[0][int(playershipTip[0])-1] = "X" #y kordináta 0 x kordináta tip
							else:
								if playershipTip[1] == '0':
									playershipsBoard[int(playershipTip[0])-1][9] = "X"	
								else:
									playershipsBoard[int(playershipTip[0])][int(playershipTip[1])-1] = "X"
							

					####################### Függőleges ############
					if vertical == True:
						print(f'min: {vminimum} max: {vmaximum}')

						if playership == vmaximum or playership == vminimum and playership not in foglalt_cords:
							one_ship.append(playership)
							playershipTip = list(str(playership))
							foglalt_cords.append(playership)
					
							##### koordináták ellenőrzése 
							if int(playership) <10:
								playershipsBoard[0][int(playershipTip[0])-1] = "X" #y kordináta 0 x kordináta tip
							else:
								if playershipTip[1] == '0':
									playershipsBoard[int(playershipTip[0])-1][9] = "X"	
								else:
									playershipsBoard[int(playershipTip[0])][int(playershipTip[1])-1] = "X"
						
					#kész hajók hozzáadása	
					if len(one_ship) == hajo_egysegek[x]:
						playerships.append(one_ship)

				else:
					print('Ide nem tehetsz hajót!')
	
			for x in range(len(playershipsBoard)):
				print(" ".join(playershipsBoard[x]))
			one_ship = []
			prev = None
			print("Játékos: ", playerships)

		except ValueError: 
			print("Hiba. Adj meg másik értéket")




def enemyNextTip(enemytip):
	possible = [enemytip-1, enemytip+1, enemytip+10, enemytip-10]
	for i in range(len(playerships)):
		if enemytip in playerships[i]:
			nextTip = random.choice(possible)
			return nextTip



if startGame:

	
	print('\tJátékos\t\t\t\t\tEllenség')
	print(' '.join(horizontal[0:Xsize]), "\t", ' '.join(horizontal[0:Xsize]))
	for dd in range(1, Xsize):
		print(" ".join(playershipsBoard[dd][0:Xsize]), '\t',  " ".join(enemyshipsBoard[dd][0:Xsize]))


	generate_ship(total_ships)
	playerCoords()
	#possible_places()

	phajo = []
	ehajo = []
	
	#a hajók kordinátáinak felbontása és eltárolása, így többször már nem kell újra bejárni
	for i in range(len(enemyships)):
		for h in range(len(enemyships[i])):
			ehajo.append(enemyships[i][h]) #ellenséges hajók hozzáadása
			phajo.append(playerships[i][h]) #játékos hajóinak hozzáadása


	while not gameOver:
		if nextRound == "player" and not gameOver:
			
			tip = input('Hol lehet a hajó? ')
			ltip = list(str(tip)) 

			if int(tip) not in ehajo:
				print("Itt nincs hajó. :(")
				if int(tip) <10:
					enemyshipsBoard[1][int(ltip[0])] = "T" #y kordináta 0 x kordináta tip
				else:
					if ltip[1] == '0':
						enemyshipsBoard[int(ltip[0])][9] = "T"	
					else:
						if ltip[0] == '9':
							enemyshipsBoard[9][int(ltip[1])-1] = "T"
						else:
							enemyshipsBoard[int(ltip[0])+1][int(ltip[1])-1] = "T"

			if int(tip) in ehajo:
				playerPoints+=1
				ehajo.remove(int(tip))
				print("Találat! ")
				
				if int(tip) <10:
					enemyshipsBoard[1][int(ltip[0])] = "X" #y kordináta 0 x kordináta tip
				else:
					if ltip[1] == '0':
						enemyshipsBoard[int(ltip[0])][9] = "X"	
					else:
						if ltip[0] == '9':
							enemyshipsBoard[9][int(ltip[1])-1] = "X"
						else:
							enemyshipsBoard[int(ltip[0])+1][int(ltip[1])-1] = "X"
				
					
				if sumOfList(hajo_egysegek, len(hajo_egysegek)) == playerPoints:
					print("Kilőttél minden hajót. Nyertél.")
					gameOver = True
					break
			nextRound = "enemy"


		if nextRound == "enemy" and not gameOver:
			
			enemytip = random.choice(coords)
			coords.remove(enemytip)
			eCoord = list(str(enemytip))
			print(f"Az ellenség következik... Tippje: {enemytip} ", end = "")
			if enemytip not in phajo:
				print("Nem talált, te jössz!")

			if enemytip in phajo:
				#enemyNextTip(enemytip)
				phajo.remove(enemytip)
				if int(enemytip) <10:
					playershipsBoard[0][int(eCoord[0])-1] = "X" #y kordináta 0 x kordináta tip
				else:
					if eCoord[1] == '0':
						playershipsBoard[int(eCoord[0])-1][9] = "X"	
					else:
						playershipsBoard[int(eCoord[0])][int(eCoord[1])-1] = "X"
				print("Eltalálta a hajód!")
				enemyPoints+=1
			
			
			if sumOfList(hajo_egysegek, len(hajo_egysegek)) == enemyPoints:
				print('Az ellenség kilőtte a hajóid, vesztettél.')
				gameOver = True
				break
				
			nextRound = "player"

		#táblák kiiratása
		print('\tJátékos\t\t\t\t\tEllenség')
		print(' '.join(horizontal[0:Xsize]), "\t", ' '.join(horizontal[0:Xsize]))
		for dd in range(1, Xsize):
			print(" ".join(playershipsBoard[dd][0:Xsize]), '\t',  " ".join(enemyshipsBoard[dd][0:Xsize]))
			
						
					