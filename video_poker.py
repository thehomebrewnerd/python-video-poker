import random
from card import Card
from deck import Deck
from hand import Hand
from score import score_hand

deck = Deck()
print("Num Cards in Deck", deck.get_num_cards())
hand = Hand(deck, 5)
print(hand)
print("Num Cards in Deck", deck.get_num_cards())
hand.discard(3)
print(hand)
hand.draw(deck)
print(hand)
print("Num Cards in Deck", deck.get_num_cards())
score = score_hand(hand)
print(score)

'''
test_hand = Hand(deck, 5)
test_hand.empty_hand()
print(len(test_hand.cards))
test_hand.add_card(Card("H", 10))
test_hand.add_card(Card("D", 11))
test_hand.add_card(Card("C", 13))
test_hand.add_card(Card("S", 13))
test_hand.add_card(Card("D", 2))
print(score_hand(test_hand))
'''

counts = dict()
for iter in range(1000000):
    deck = Deck()
    hand = Hand(deck, 5)
    #print(hand)
    score = score_hand(hand)
    #print(iter, score)
    counts[score] = counts.get(score, 0) + 1

print(counts)
