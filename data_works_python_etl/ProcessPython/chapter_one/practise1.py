#　一摞有序的纸牌
import collections
from random import choice
Cards = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(x) for x in range(2,11)]+list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Cards(rank,suit) for rank in self.ranks for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    getCard = FrenchDeck()
    print(len(getCard))
    print(getCard[0])
    print(getCard[:3])
    print(getCard[12::13])
    print(choice(getCard))