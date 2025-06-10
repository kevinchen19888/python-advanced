"""
面向对象编程示例
"""
from enum import Enum

class Suite(Enum):
    """花色枚举"""
    SPADE,HEART,DIAMOND,CLUB = range(4)


class Card:
    """牌"""
    def __init__(self, suite: Suite, face: int):
        """
        :param suite: 花色
        :param face: 点数
        """
        self.suite = suite
        self.face = face
    def __repr__(self):
        """
        :return: 牌名
        """
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数


import random
class Poker:
    """牌堆"""
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        # 发牌位置
        self.current = 0
    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)
    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card
    @property
    def has_more(self):
        """是否还有牌"""
        return self.current < len(self.cards)


class Player:
    """玩家"""
    def __init__(self, name):
        self.name = name
        self.cards = []
    def get_one(self, card: Card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self):
        """排序"""
        self.cards.sort(key=lambda card: (card.suite.value, card.face))


def play():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    # 玩家整理手中的牌,输出名字和牌
    for player in players:
        player.sort()
        print(f'{player.name}: {[str(card) for card in player.cards]}')

# play()


