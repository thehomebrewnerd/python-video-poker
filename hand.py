class Hand():
    def __init__(self, deck, num_cards):
        self.cards = []
        for _ in range(num_cards):
            self.cards.append(deck.draw_card())

    def __str__(self):
        output = ""
        for card in self.cards:
            output = output + str(card) + " "

        return output

    def discard(self, pos):
        self.cards.pop(pos)

    def draw(self, deck):
        self.cards.append(deck.draw_card())

    def get_max_rank(self):
        rank_list = [card.rank for card in self.cards]
        return max(rank_list)

    def get_min_rank(self):
        rank_list = [card.rank for card in self.cards]
        return min(rank_list)

    def add_card(self, card):
        self.cards.append(card)

    def empty_hand(self):
        self.cards = []

    def contains_ace(self):
        rank_list = [card.rank for card in self.cards]
        if 14 in rank_list:
            return True
        else:
            return False
