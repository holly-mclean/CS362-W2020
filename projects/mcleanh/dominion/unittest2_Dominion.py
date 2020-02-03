"""
Created on Sunday Feb 2 2020

@author: Holly McLean
"""

from unittest import TestCase
import testUtility
import Dominion

class TestPlayer(TestCase):
    def setUp(self):
        self.players = testUtility.GetPlayers()
        self.nC = testUtility.GetCurses(self.players)
        self.nV = testUtility.GetVictoryCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        self.supply = testUtility.GetSupply(self.box, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_action_balance(self):
        # initialize test data
        self.setUp()

        # instantiate 3 action card objects
        actioncard = Dominion.Woodcutter()
        actioncard2 = Dominion.Laboratory()
        actioncard3 = Dominion.Village()

        # add action cards to player hand
        self.player.hand = [actioncard, actioncard2, actioncard3]

        # call action_balance and verify that action balance returns correct value
        balance = self.player.action_balance()

        self.assertEqual(balance, 0)

    def test_calcpoints(self):
        # initialize test data
        self.setUp()

        # clear out the player stack
        self.player.deck = []
        self.player.hand = []

        # instantiate 5 card objects
        actioncard = Dominion.Woodcutter()
        actioncard2 = Dominion.Laboratory()
        actioncard3 = Dominion.Village()
        card = Dominion.Gardens()
        card2 = Dominion.Province()

        # add cards to player hand
        self.player.hand = [actioncard, actioncard2, actioncard3, card, card2]

        # call calcpoints() and verify that the tally is 6
        tally = self.player.calcpoints()
        self.assertEqual(6, tally)

    def test_draw(self):
        # initialize test data
        self.setUp()

        # draw with an empty hand and default destination, and verify hand is filled up
        self.player.draw()
        self.assertEqual(6, len(self.player.hand))

        # draw with a filled hand and default destination, and verify a card was added
        self.player.draw()
        self.assertEqual(7, len(self.player.hand))

        # draw to a specified, empty destination (discard pile), and verify a card was added
        self.player.draw(self.player.discard)
        self.assertEqual(1, len(self.player.discard))

        # empty the deck, fill the discard pile
        self.player.deck = []
        card = Dominion.Gardens()
        self.player.discard = [card, card, card]

        # verify whether draw() replenishes the deck from the discard pile
        self.player.draw()
        self.assertEqual(2, len(self.player.deck))


    def test_cardsummary(self):
        # initialize test data
        self.setUp()

        # clear out the player stack
        self.player.deck = []
        self.player.hand = []

        # instantiate 5 card objects
        actioncard = Dominion.Woodcutter()
        actioncard2 = Dominion.Laboratory()
        actioncard3 = Dominion.Village()
        card = Dominion.Gardens()
        card2 = Dominion.Province()

        # add cards to player hand
        self.player.hand = [actioncard, actioncard, actioncard2, actioncard3, card, card2]

        summary = self.player.cardsummary()

        sumlen = len(summary)

        self.assertEqual(6, sumlen)
