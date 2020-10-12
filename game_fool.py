import random

class Deck:
# Создаем колоду
    def __init__(self):
        self._suits = ["\u2660", "\u2665", "\u2663", "\u2666"]
        self._cards = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck={self._cards[i]: i for i in range(len(self._cards))}
        _mixed_deck=[]
        self.all_deck = {}
        for i in range(len(self._suits)):
            for key, values in self.deck.items():
                key = self._suits[i] + key
                self.all_deck[key] = values

# Перемешиваем колоду
    def mix_deck(self):
        self._mixed_deck=list(self.all_deck)
        random.shuffle(self._mixed_deck)

# Раздаем карты
    def hand_cards(self):
        self.player_hand = self._mixed_deck[-6:]
        self._comp_hand = self._mixed_deck[-12:-6]
        del self._mixed_deck[-12:]

# Кто ходит первым
    def first_turn(self):
        if random.randint(1, 2) == 1:
            print('Ваш ход')
            return 'Ваш ход'
        else:
            print('Ход компьютера')
            return 'Ход компьютера'

# Ход игрока
    def pl_turn(self):
        print('У вас на руках такие карты:\n{}'.format(self.player_hand))
        self.player_card = []
        self.player_hand_len = []
        for i in range(len(self.player_hand)):
            self.player_hand_len.append(i)
        self.player_choice = int(input('Какой картой пойдете? Введите номер: {}'.format(self.player_hand_len)))
        self.player_card.append(self.player_hand[self.player_choice])
        self.player_hand.remove(self.player_hand[self.player_choice])

# Ответ компьютера
    def computer_answer(self):
        self.answer_cards = []
        for card in self._comp_hand:
            if (card[0:1] == self.player_card[0][0:1]):
                if self.all_deck[card] > self.all_deck[self.player_card[0]]:
                    self.answer_cards.append(card)

        if len(self.answer_cards)>0:
            self.comp_move = self.answer_cards[0]
            self._comp_hand.remove(self.comp_move)
            print('Ваша карта бита {}.'.format(self.comp_move))
        else:
            print('Компьютер взял.')
            self._comp_hand.append(self.player_card)

# Добор карт
    def new_cards(self):
        if (len(self._comp_hand) < 6) and (len(self._mixed_deck) > 0):
            self._comp_hand.append(self._mixed_deck[-1])
            del self._mixed_deck[-1]

            print('Карту компьютеру. Осталось карт в колоде: {}'.format(len(self._mixed_deck)))
            print('Всего карт у компьютера: {}'.format(len(self._comp_hand)))

        if (len(self.player_hand) < 6) and (len(self._mixed_deck) > 0):
            self.player_hand.append(self._mixed_deck[-1])
            del self._mixed_deck[-1]
            print('Карту вам. Осталось карт в колоде: {}'.format(len(self._mixed_deck)))
            print('Ваши карты: {}'.format(self.player_hand))

# Следующий ход
    def computer_move(self):

        if len(self._comp_hand) > 0:
           self.min_comp_card = 20
           self.comp_move = ''
           for card in range(len(self._comp_hand)):
               self.comp_move = str(self._comp_hand[card])
           self._comp_hand.remove(self.comp_move)
           print('Ход компьютера: {}'.format(self.comp_move))

# Ответ
    def player_answer(self):
        while True:
            print('Ваши карты:\n{}'.format(self.player_hand))
            player__answer_hand_len = []
            for i in range(len(self.player_hand)):
                player__answer_hand_len.append(i + 1)
            player_answer_cards = int(input('Какой картой будем бить компьютер?.\nВведите 0, чтобы забрать карту.'.format(player__answer_hand_len)))
            if player_answer_cards == 0:
                self.player_hand.append(self.comp_move)
                print('Взяли. \nВаши карты: {}'.format(len(self.player_hand), self.player_choice))
                return 'Ход Компьютера'

    def is_winner(self):
        if len(self.player_hand) == 0:
            return 'Игрок победил'
        if len(self._comp_hand) == 0:
            return 'Компьютер победил'

deck = Deck()

if __name__ == '__main__':
    deck = Deck()
    deck.mix_deck()
    deck.hand_cards()
    deck.first_turn()
    deck.pl_turn()
    deck.computer_answer()
    deck.new_cards()
    deck.computer_move()
    deck.player_answer()
    deck.is_winner()
