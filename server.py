#!/usr/bin/python

import socket	#Chargment du module pour la communication TCP/IP
import time	#Chargement du module de gestion du temp

TCP_IP = '192.168.0.182' #Adresse IP du serveur
TCP_PORT = 4242 #Port de connection au serveur
BUFFER_SIZE = 2 #Taille max d'un packet

vectX = 1 #vecteur de deplacement en X
vectY = -1 #vecteur de deplacement en Y
posX = 4 #Position en X
posY = 4 #Position en Y

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Création du socket de communications
s.bind((TCP_IP, TCP_PORT)) #Bind du socket
s.listen(1) #On met le serveur en écoute

print 'Lancement du serveur \nAttente des connections ... ' #Affichage de lancement du serveur
rasp1, addr = s.accept() #on attend la connection du joueur 1
rasp1.send('Bienvenue sur le serveur joueur 1') #Une fois le joueur 1 connecté on lui envoie un message d'acceuil
rasp1.send(str('1')) #On lui indique son numéro de joueur
print 'Connection address:',addr #On affiche la reception d'une connection
rasp2, addr2 = s.accept() #Meme protocole pour le joueur 2
rasp2.send('Bienvenue sur le serveur joueur 2') #Cf joueur 1
rasp2.send(str('2')) #Cf joueur 1
print 'connection address:',addr2 #Cf joueur 1

while 1: #Boucle du serveur (Une amélioration simple serait de mettre un try: Except: pour le KEYBOARDINTERRUPT)
	print 'Pos x:{} y:{}',int(posX),int(posY) #A chaque MAJ du serveur on affiche les coordonnées de la balle
	if posX==15: # Si la balle a atteint la limite du joueur 2
		rasp1.send(str(posX)) #On Envoie les coordonnées
       		rasp1.send(str(posY))
        	rasp2.send(str(posX))
        	rasp2.send(str(posY))
		data = int(rasp2.recv(BUFFER_SIZE)) #On attends la résolution de collisions du joueur 2
		if data==1: #Dans le cas 1 (Balle au centre de la raquette)
			print 'bat 2 1' #On affiche l'evenement
			vectX=(-1) #On inverse le vecteur en X
			vectY=0 #Le vecteur Y n'est actuellement pas implémenté
		elif data==2: #Dans le cas 2 (Balle sur le cote gauche de la raquette)
			print 'bat2 2'
			vectX=(-1)
			vectY=0
		elif data==3: #Balle sur le cote droit
			print 'bat 2 3'
			vectX=(-1)
			vectY=0
		elif data==4: #Le joueur n'a pas renvoye la balle
			print 'bat 2 4'
			posX=4 #On reset les coordonnées
			posY=4
	if posX==0: #Meme protocole pour le joueur 1
		rasp1.send(str(posX))
        	rasp1.send(str(posY))
        	rasp2.send(str(posX))
        	rasp2.send(str(posY))
		data = int(rasp1.recv(BUFFER_SIZE))
		if data==1:
			print 'bat 1 1'
                        vectX=(1)
                        vectY=0
                elif data==2:
			print 'bat 1 2'
                        vectX=(1)
                        vectY=0
                elif data==3:
			print 'bat 1 3'
                        vectX=(1)
                        vectY=0
                elif data==4:
			print 'bat 1 4'
                        posX=4
                        posY=4
	if posY==7: #On verifie que la balle ne sorte pas en Y
		vectY=(-1)
	if posY==0:#Pareil
		vectY=1
	rasp1.send(str(posX)) #on envoie les coordonnées
	rasp1.send(str(posY))
	rasp2.send(str(posX))
	rasp2.send(str(posY))
	posY+=vectY
        posX+=vectX
	time.sleep(0.3) #On fait une pause jusqu'a la prochaine maj de positions
rasp1.close() #On deconnecte les rasp du serveur en sortie de programme	
rasp2.close()
