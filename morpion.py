# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
j1 = ""
j2 = ""
plateau = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]
signe1 = "x"
signe2 = "o"
coupj1 = ""
coupj2 = ""



def morpion():    
    global coupj1
    global coupj2
    global signe1
    global signe2
    global Tour
    coupj1=0
    coupj2=0
    Tour = 0
    print("jouons au morpion")
    j1 = input("j1 quel est ton nom ?")
    j2 = input("j2 quel est ton nom ?")
    print("\n", plateau[0][0], plateau[0][1], plateau[0][2], "\n",
          plateau[1][0], plateau[1][1], plateau[1][2], "\n",
          plateau[2][0], plateau[2][1], plateau[2][2])
    True
    while True:
    
        coupj1 = input("j1 où veux-tu jouer ?")
        jeu()
        verifierjetons()
        while verifierjetons() == False:
            coupj1=input("rejoue")
        Tour += 1    
            
        print("\n", plateau[0][0], plateau[0][1], plateau[0][2], "\n",
              plateau[1][0], plateau[1][1], plateau[1][2], "\n",
              plateau[2][0], plateau[2][1], plateau[2][2])
        
        if plateau[0][0] == signe1 and plateau[0][1] == signe1 and plateau[0][2] == signe1:
            print(j1+" a gagné")
            
            return False        
    
        if plateau[1][0] == signe1 and plateau[1][1] == signe1 and plateau[1][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[2][0] == signe1 and plateau[2][1] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][0] == signe1 and plateau[1][0] == signe1 and plateau[2][0] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][1] == signe1 and plateau[1][1] == signe1 and plateau[2][1] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][2] == signe1 and plateau[1][2] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][0] == signe1 and plateau[1][1] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][2] == signe1 and plateau[1][1] == signe1 and plateau[2][0] == signe1:
            print(j2+" a gagné")
            
            return False 
        if Tour >= 9:
            print("égalité")
            return False
        if plateau[1][0] == signe2 and plateau[1][1] == signe2 and plateau[1][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[2][0] == signe2 and plateau[2][1] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][0] == signe2 and plateau[1][0] == signe2 and plateau[2][0] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][1] == signe2 and plateau[1][1] == signe2 and plateau[2][1] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][2] == signe2 and plateau[1][2] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][0] == signe2 and plateau[1][1] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][2] == signe2 and plateau[1][1] == signe2 and plateau[2][0] == signe2:
            print(j2+" a gagné")
        
        coupj2 = input("j2 où veux-tu jouer ?")
        jeu()
        verifierjetons()
        while verifierjetons() == False:
            coupj2=input("rejoue")
        print("\n", plateau[0][0], plateau[0][1], plateau[0][2], "\n",
              plateau[1][0], plateau[1][1], plateau[1][2], "\n",
              plateau[2][0], plateau[2][1], plateau[2][2])
        Tour += 1
        if plateau[0][0] == signe1 and plateau[0][1] == signe1 and plateau[0][2] == signe1:
            print(j1+" a gagné")
            
            return False        
    
        if plateau[1][0] == signe1 and plateau[1][1] == signe1 and plateau[1][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[2][0] == signe1 and plateau[2][1] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][0] == signe1 and plateau[1][0] == signe1 and plateau[2][0] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][1] == signe1 and plateau[1][1] == signe1 and plateau[2][1] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][2] == signe1 and plateau[1][2] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][0] == signe1 and plateau[1][1] == signe1 and plateau[2][2] == signe1:
            print(j1+" a gagné")
            
            return False  
        if plateau[0][2] == signe1 and plateau[1][1] == signe1 and plateau[2][0] == signe1:
            print(j2+" a gagné")
            
            return False  
        if Tour >= 9:
            print("égalité")
            return False
        if plateau[1][0] == signe2 and plateau[1][1] == signe2 and plateau[1][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[2][0] == signe2 and plateau[2][1] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][0] == signe2 and plateau[1][0] == signe2 and plateau[2][0] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][1] == signe2 and plateau[1][1] == signe2 and plateau[2][1] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][2] == signe2 and plateau[1][2] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][0] == signe2 and plateau[1][1] == signe2 and plateau[2][2] == signe2:
            print(j2+" a gagné")
            
            return False  
        if plateau[0][2] == signe2 and plateau[1][1] == signe2 and plateau[2][0] == signe2:
            print(j2+" a gagné")
            
            return False  
        if Tour >= 9:
            print("égalité")
            return False 

def jeu():
    global plateau
    global signe1
    global signe2
    
    
    if coupj1 == "1" or coupj1 == "2" or coupj1 == "3":
        plateau[0][int(coupj1)-1] = signe1
    if coupj1 == "4" or coupj1 == "5" or coupj1 == "6":
        plateau[1][int(coupj1)-4] = signe1
    if coupj1 == "7" or coupj1 == "8" or coupj1 == "9":
        plateau[2][int(coupj1)-7] = signe1
    if coupj2 == "1" or coupj2 == "2" or coupj2 == "3":
        plateau[0][int(coupj2)-1] = signe2
    if coupj2 == "4" or coupj2 == "5" or coupj2 == "6":
        plateau[1][int(coupj2)-4] = signe2
    if coupj2 == "7" or coupj2 == "8" or coupj2 == "9":
        plateau[2][int(coupj2)-7] = signe2

def verifierjetons():
    global coupj1
    global coupj2
    
    if coupj1 == "1" or coupj1 == "2" or coupj1 == "3":
        if plateau[0][int(coupj2)-1] == signe1:
            return False
    if coupj1 == "4" or coupj1 == "5" or coupj1 == "6":
        if plateau[1][int(coupj2)-4] == signe1:
            return False    
    if coupj1 == "7" or coupj1 == "8" or coupj1 == "9":
        if plateau[2][int(coupj2)-7] == signe1:
            return False
    if coupj2 == "1" or coupj2 == "2" or coupj2 == "3":
        if plateau[0][int(coupj1)-1] == signe1:
            return False
    if coupj2 == "4" or coupj2 == "5" or coupj2 == "6":
        if plateau[1][int(coupj1)-4] == signe1:
            return False    
    if coupj2 == "7" or coupj2 == "8" or coupj2 == "9":
        if plateau[2][int(coupj1)-7] == signe1:
            return False
    else:
        return True
   
    
    
    



morpion()
