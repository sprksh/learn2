import sys
import random


class Card:
    '''Stores card objects'''
    def __init__(self, name, suite, value):
        self.name = name
        self.suite = suite
        self.value = value
        self.ace = False
        if self.name == 'A':
            self.ace = True

    def __repr__(self):
        name, suite = self.name, self.suite
        return '{0} of {1}'.format(name, suite)


class Player:
    '''Stores Player object with id and cards stacks and states (Play, Hold, 'Busted', Won)'''
    def __init__(self, id):
        self.id = id
        self.dealer = False
        if id == 1:
            self.dealer = True
        self.cards = []
        self.point = 0
        self.max_point = 0
        self.aces_count = 0
        self.state = 'Play'     # Play, Hold, 'Busted', Won

    def __repr__(self):
        name = 'Player {}'.format(self.id)
        return '[{0} ({1}): {2}]'.format(name, self.state, self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.point += card.value
        self.max_point += card.value
        if card.ace:
            self.max_point += 10
            self.aces_count += 1
        if self.max_point > 21 and self.max_point > self.point:
            self.max_point -= 10

        if self.point > 21:
            self.state = 'Busted'
            print('\nBusted: {}'.format(self))
        elif 16 < self.point < 21:
            self.state = 'Hold'
            print('\nOn Hold: {}'.format(self))
        elif self.point == 21 or self.max_point == 21:
            self.state = 'Won'
        points[self.id - 1] = self.max_point


cards, players, points = [], [], []      # list storage of cards objects, players and points

val_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'A': 1, 'K': 10, 'Q': 10, 'J': 10}
suites = {'Diamond': 'Red', 'Club': 'Black', 'Heart': 'Red', 'Spade': 'Black'}


def shuffle():          # Creates a random list of 52 cards
    for key in val_dict:
        for j in suites:
            cards.append(Card(name=key, suite=j, value=val_dict[key]))
    random.shuffle(cards)


def start():            # Starts the game, takes input and starts the deal giving 2 cards to each player
    while True:
        try:
            global player_count
            player_count = int(input("Enter number of players between 2 and 26: ").strip())
            if player_count > 26 or player_count < 2:       # The game needs atleast 2 players including dealer
                raise ValueError
        except ValueError:
            print('Input Not a number or does not lie between 2 and 26')
            continue
        else:
            break
    # Create Players
    for i in range(1, player_count + 1):
        players.append(Player(id=i))
        points.append(0)
    # First Deal
    for p in players:
        for i in range(2):
            card = cards.pop()
            p.add_card(card)
    print([(w, w.max_point) for w in players])


def find_winner():                          # Finds winners and prints the List of winners
    winners = []
    maximum = players[0].max_point          # What happens when all players have points = dealer.point? Nobody wins??
    for p in players:
        if p.state in ['Hold', 'Play', 'Won']:
            if p.max_point > maximum:
                winners.append(p)
    if not winners and not players[0].max_point > 21: winners = [players[0]]    # points are atmost equal to dealer's
    print("\n::Winners:: ")
    for w in winners:
        print(w, w.max_point)


def game_on():                              # Checks if the game needs to continue
    if players[0].state == 'Busted':        # Else finds winner and exits
        print([w for w in players if w.state in ['Hold', 'Play', 'Won']])
        sys.exit("\nDealer Busted! Everybody else in game wins. Game Over!!")
    if 21 in points:
        print("Winners: {}".format([w for w in players if w.point == 21 or w.max_point == 21]))
        sys.exit("\nBlackjack.. Game Over!!")
    pc = len([i for i in players if i.state == 'Play'])
    if pc > len(cards):
        find_winner()
        sys.exit("\nNot enough Cards! Game Over!!")
    return True


def hit():                                  # The Dealer Distributes the cards
    if game_on():
        count = 0
        for p in players:
            if p.state == 'Play':
                card = cards.pop()
                p.add_card(card)
                count += 1
        print([(w, w.max_point) for w in players])
        if count == 0:
            find_winner()
            sys.exit("\nNo one left to serve.. Game Over!!")      # Not given in problem but still


if __name__ == '__main__':
    shuffle()
    start()
    print("Game Stated, Deal Done")
    while True:
        input("Nobody won yet! Press Enter to continue...")
        hit()
