import score
from hand import Hand

def analyze_hand(hand):
    if score.score_royal_flush(hand):
        return hand

    elif score.score_straight_flush(hand):
        return hand

    elif score.score_four_of_a_kind(hand):
        ranks = [card.rank for card in hand.cards]
        rank_count = dict()
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        for key, count in rank_count.items():
            if count == 4:
                rank_to_keep = key

        return Hand([card for card in hand.cards if card.rank == rank_to_keep])

    elif four_to_royal(hand):
        pass

    elif score.score_full_house(hand):
        return hand

    elif score.score_flush(hand):
        return hand

    elif score.score_three_of_a_kind(hand):
        ranks = [card.rank for card in hand.cards]
        rank_count = dict()
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        for key, count in rank_count.items():
            if count == 3:
                rank_to_keep = key

        return Hand([card for card in hand.cards if card.rank == rank_to_keep])

    elif score.score_straight(hand):
        return hand

    else:
        return Hand()

def four_to_royal(hand):
    return False
