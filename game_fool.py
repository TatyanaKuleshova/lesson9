import random

#класс карта
class Card:
    '''c - трефы, d - бубны, h - червы, s - пики
    J - валет, D - дама, K - король, A - туз'''

    rank = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suit = ['d', 'h', 's', 'c']

    def __init__(self):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

#класс колода
    class Deck:
        def cards_shuffled(self):
            self._rep = list(self._rep)
            random.shuffle(self._rep)
            print('Карты перемешаны')

    @staticmethod
    def r_card(x):
        value = 6
        for i in card:
            if x == i:
                return value
            value += 1




        ranks = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
        value = 6
