"""
Created on Sunday Feb 2 2020

@author: Holly McLean
"""

from unittest import TestCase
import testUtility
import Dominion

class TestAction_card(TestCase):
    def setUp(self):
        self.players = testUtility.GetPlayers()
        self.nC = testUtility.GetCurses(self.players)
        self.nV = testUtility.GetVictoryCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        self.supply = testUtility.GetSupply(self.box, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_init(self):
        # initialize test data
        self.setUp()

        # instantiate card object
        actioncard = Dominion.Woodcutter()

        # verify that Woodcutter has correct values
        self.assertEqual("Woodcutter", actioncard.name)
        self.assertEqual(3, actioncard.cost)
        self.assertEqual(0, actioncard.actions)
        self.assertEqual(0, actioncard.cards)
        self.assertEqual(1, actioncard.buys)
        self.assertEqual(2, actioncard.coins)

    def test_use(self):
        # initialize test data
        self.setUp()

        # instantiate card objects
        actioncard = Dominion.Woodcutter()
        actioncard2 = Dominion.Laboratory()

        # add action cards to player hand
        self.player.hand = [actioncard, actioncard2]

        self.assertEqual(len(self.player.hand), 2)

        # call the use() function
        actioncard.use(self.player, self.trash)
        actioncard2.use(self.player, self.trash)

        # verify that use() functions correctly
        self.assertEqual(self.player.played[0], actioncard)
        self.assertEqual(self.player.played[1], actioncard2)
        self.assertEqual(len(self.player.hand), 0)

    def test_augment(self):
        pass
