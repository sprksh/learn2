# How game proceeds:
# timer moves 3.. 2... 1.. all the while scree shows the dictionary i: spell
# 0. computer waits for my input while the timer moves forward. 
# 1. The spell hits other player.. the spell is represented by a line. But in a flash we see the anme of he spell
# 2. The screen shows power reducing for both players
# 3. breaks if somebody loses else continues

# Game Length = 1 minute
# Select Player for Yourself
# Gmae Starts:

# You cast spells with powers the more power you cast to spell, the weaker you become p/5
# You have maximum 10 spells
# Winning/ Losing/ Constraints
# If your power <= 0
# if spell strength difference > 5


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time


class Player:

    def __init__(self, name):
        self.name = name
        self.power = 100
        self.speciality = []
        self.spells_available = []
        self.position = []


class Spell:

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.opposite = ''

class Game:

    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.starttime = ''
        # self.time = time
        # states: 'select', 'spell', 'score'
        self.state = 'select'


pps = ['Harry', 'Voldemort', 'Dumbledore', 'Snape', 'Hermoine', 'Ron']
sps = ['Avada Kedavra', 'Expelliarmus', 'Accio', 'Annihilate', 'Crucio', 'Imperio']
players = {'Harry': 7, 'Voldemort': 1, 'Dumbledore': 8, 
'Snape': '', 'Hermoine': 'Expelliarmus', 'Ron': 'Accio', 'Hagrid': 'Annihilate'}
spells =  {'Avada kedavra' :10, 'Expelliarmus': 5, 'Accio': 1, 'Annihilate': 9, 'Crucio': 8, 'Imperio': 7}
cool_dict = {}
active_spells = []


def create_player():
    name = input('Type the name of player: ')
    # if name in players:
    # else:

    #     speciality1 = int(input('Select the specialities by number: '))
    #     speciality2 = int(input('Select one more: '))
    #     specialities = [speciality1, speciality2]
    # player1 = Player(name)
    player1 = Player(pps[0])
    p2 = pps[randint(0, 5)]
    player2 = Player(name)
    for k in spells:
        active_spells.append(Spell(k, spells[k]))
    player1.spells_available = active_spells
    player1.speciality = [active_spells[randint(0, 5)]]
    player2.spells_available = active_spells
    player2.speciality = [active_spells[randint(0, 5)]]
    print('Game between {} and {}'.format(player1.name, player2.name))

    o = input('Press any key to start game: ')
    if o:
        game(player1, player2)


def game(player1, player2):
    game = Game(player1, player2)
    curses.initscr()
    win = curses.newwin(40, 80, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT                                                    # Initializing values

    player1.position = [10, 1]
    player2.position = [10, 78]

    # Timeout value will be based on state
    # States: 
    # 1. Selection of spell, right/left, up/d key to select spell
    # 2. Hitting of spell. timeout very low to show fast movement, Will show the spell name on screen
    # 3. Show updated score


    while key != 27:                                                   # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(player1.power) + ' ')
        win.addstr(0, 27, ' Wizardry ')
        win.addstr(0, 52, 'Score : ' + str(player1.power) + ' ')
        for i in range(80):
            win.addch(20, i, '_')
        if game.state == 'select':
            win.timeout(150)
            start1, y = 3, 30
            for i, s in enumerate(player1.spells_available):
                spel = '{0}: {1} ({2}) '.format(i+1, s.name, s.power)
                if start1 + len(spel) + 2 >= 40:
                    start1 = 3
                    y += 2
                win.addstr(y, start1, spel)
                start1 = start1 + len(spel) + 2
            start2, y = 43, 30
            for i, s in enumerate(player1.spells_available):
                spel = '{0}: {1} ({2}) '.format(i+1, s.name, s.power)
                if start2 + len(spel) + 2 >= 80:
                    start2 = 43
                    y += 2
                spel = '{0}: {1} ({2})'.format(i+1, s.name, s.power)
                win.addstr(y, start2, spel)
                start2 = start2 + len(spel) + 2

            event = win.getch()
            key = event
            if key not in [1,2,3,4,5,6,7,8,9,10, 27]:     # If an invalid key is pressed
                pass
            else:
                try:
                    this_spell1 = player1.spells_available[key-1]
                except Exception:
                    # print('You lose this spell')
                    this_spell1 = player1.spells_available[-1]
                this_spell2 = player1.spells_available[randint(0, len(player2.spells_available) - 1)]
                game.state = 'spell'

        if game.state == 'spell':
            win.timeout(20)
            win.addstr(2, 2, this_spell1.name)
            win.addstr(2, 52, this_spell2.name)
            p1_spell = [[10, 1]]
            p2_spell = [[10, 79]]
            while p1_spell[-1][-1] < 80:
                p1_spell.append([10, p1_spell[-1][-1] + 1])
                p1_spell.append([10, p1_spell[-1][-1] - 1])
                win.addch(p1_spell[0][0], p1_spell[0][1], '.')
                win.addch(p1_spell[0][0], p2_spell[0][1], '.')
        if game.state == 'score':
            win.timeout(150)
            
        
        

        win.addch(player1.position[0], player1.position[1], '#')
        win.addch(player2.position[0], player2.position[1], '#')

        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        

    curses.endwin()


if __name__ == '__main__':
    print('The game will start in 2 seconds')
    time.sleep(0.5)
    # print('The game will start in 1 seconds')
    # time.sleep(0.5)
    # print('The game will start in 1 seconds')
    # o = input('Press a key to select player')
    # if o:
    create_player()
