import random
import os
import sys
from card import Card
from deck import Deck
from hand import Hand
from score import score_hand
from analyze import analyze_hand

deck = Deck()
hand = Hand()
hand.add_card(Card("H", 7))
hand.add_card(Card("D", 8))
hand.add_card(Card("C", 9))
hand.add_card(Card("H", 10))
hand.add_card(Card("H", 11))
print(hand)
print(score_hand(hand))
print("Hold cards: {}".format(analyze_hand(hand)))
new_hand = Hand()
