# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015

@author: tfleck
"""

import Dominion
import testUtility2

# Get player names
players = testUtility2.GetPlayers()

# number of curses and victory cards
nV = testUtility2.GetVictoryCards(players)

nC = testUtility2.GetCurses(players)

# Define box
box = testUtility2.GetBoxes(nV)

supply_order = testUtility2.GetSupplyOrder()

# Pick 10 cards from box to be in the supply.
supply = testUtility2.GetSupply(box, players, nV, nC)

# initialize the trash
trash = []

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)