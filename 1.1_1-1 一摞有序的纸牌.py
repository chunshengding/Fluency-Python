import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # spades; diamonds; clubs; hearts
    suits = "红心 方块 梅花 黑桃".split()

    def __init__(self):
        # print("ranks",self.ranks)
        # print("suits",self.suits)
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]
        # print(self._cards)

    # 可以使用len(deck) 获取长度
    def __len__(self):
        return len(self._cards)

    # 可以支持迭代,切片
    # 可以使用deck=FrenchDeck() deck[0]获取
    def __getitem__(self, position):
        return self._cards[position]



beer_card = Card("7", "方块")
print(beer_card)

deck = FrenchDeck()
deck[0]
print(len(deck))
print("-- 下标获取 ", "-" * 50)
print(deck[0])
print(deck[1])
print(deck[-1])
print("-- 随机获取 ", "-" * 50)
print(choice(deck))

print("-- 切片获取 ", "-" * 50)

print(deck[:3])
print(deck[12::13])

print("-- 迭代获取 ", "-" * 50)
for card in deck:
    print(card)
print("-- 倒序迭代 ", "-" * 50)
for card in reversed(deck):
    print(card)


suit_values=dict(红心=3,方块=2,梅花=3, 黑桃=4)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)