# -*- coding: utf-8 -*-
"""
Created on Saturday Jan 18 15:55:38 2020

@author: Holly McLean
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

# REFACTOR #1
# Define box
box = testUtility.GetBoxes(nV)

# REFACTOR #2
# Set up supply order
supply_order = testUtility.SetupSupplyOrder()

# REFACTOR #3
# Pick 10 cards from box to be in the supply, and initialize the supply
supply = testUtility.SetupSupply(box, player_names, nV, nC)

# TEST SCENARIO #2: Redefine the number of all Coin cards in the supply to be 0
supply["Copper"]=[Dominion.Copper()]*0
supply["Silver"]=[Dominion.Silver()]*0
supply["Gold"]=[Dominion.Gold()]*0

#initialize the trash
trash = []

# REFACTOR #4
#Costruct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)