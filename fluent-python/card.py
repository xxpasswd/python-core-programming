'''
一个模拟纸牌的类
'''

import collections
import time

Card = collections.namedtuple('Card',['suit','rank'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(suit,rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self,pos):
        return self._card[pos]

# 纸牌排序函数
_suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def card_size(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    suit_value = _suit_values[card.suit]*100
    return suit_value+rank_value
