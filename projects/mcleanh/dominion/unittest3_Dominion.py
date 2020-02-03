"""
Created on Sunday Feb 2 2020

@author: Holly McLean
"""

from unittest import TestCase
import testUtility
import Dominion

class Test(TestCase):
    def setUp(self):
        self.players = testUtility.GetPlayers()
        self.nC = testUtility.GetCurses(self.players)
        self.nV = testUtility.GetVictoryCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        self.supply = testUtility.GetSupply(self.box, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_gameover(self):
        # initialize test data
        self.setUp()

        # verify that an unaltered supply doesn't end the game
        gameOver1 = Dominion.gameover(self.supply)
        self.assertEqual(False, gameOver1)

        # set Province supply to 0, and confirm gameover() returns true
        self.supply["Province"] = [Dominion.Province()]*0
        gameOver2 = Dominion.gameover(self.supply)
        self.assertEqual(True, gameOver2)

        # add province cards back to the supply
        self.supply["Province"] = [Dominion.Province()]

        # set 3 card piles to 0, and confirm gameover() returns true
        self.supply["Silver"] = [Dominion.Silver()]*0
        self.supply["Gold"] = [Dominion.Gold()]*0
        self.supply["Duchy"] = [Dominion.Duchy()]*0
        gameOver3 = Dominion.gameover(self.supply)
        self.assertEqual(True, gameOver3)