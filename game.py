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

# curses alternate for windows: http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time
import os
import json


class Player:

    def __init__(self, name):
        self.name = name
        self.power = 100
        self.speciality = None
        self.spells_available = []
        self.position = []
        self.this_spell = None

    def hit(self, ind):
        spell = self.spells_available.pop(ind)
        self.this_spell = spell
        self.power -=  spell.power//2
        return spell


class Spell:

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.opposite = ''

    def __repr__(self):
        return '{}! ({})'.format(self.name, self.power)

class Game:

    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        # self.starttime = ''
        # self.time = time
        # states: 'select', 'spell', 'score'
        self.state = 'select'

    def save(self):
        with open('game_file.json', 'w+') as f:
            json.dump(self.__dict__, f, indent=4)


pps = ['Harry Potter', 'Voldemort', 'Dumbledore', 'Snape', 'Hermoine', 'Ron Weasley']
sps = [
    'Avada Kedavra', 'Expelliarmus', 'Annihilate', 'Crucio', 'Imperio', 'Incarcerous', 'Oppugno', 'Expulso', 
    'Levicorpus', 'Locomotor Mortis'
    ]
players = {
    'Harry Potter': 'Expelliarmus', 'Voldemort': 'Avada Kedavra', 'Dumbledore': 'Crucio', 
    'Snape': 'Imperio', 'Hermoine': 'Expelliarmus', 'Ron Weasley': 'Incarcerous', 'Hagrid': 'Annihilate'
    }
spells =  {
    'Avada Kedavra' :10, 'Annihilate': 9, 'Crucio': 8, 'Imperio': 7, 'Levicorpus': 6, 'Expelliarmus': 5, 
    'Incarcerous': 4, 'Oppugno': 3, 'Expulso': 2, 'Locomotor Mortis': 1, 'No Spell': 0
    }

guide = [
    'The Game is for one player. On the opposite side, there is the computer',
    'You will have a list of spells available at the bottom of the screen along with their power',
    'You cast a spell by clicking its serial number. eg: 1, 2, 3 (One at a time)',
    'If the cast you spell has power that is 5 or more less than the opponent, You get killed!',
    'If all your spells are cast while that of the enemy is left, You lose.',
    'For every spell you lose some power that is proportional to the power of spell you cast',
    'You also lose power = power of your opponents spell - power of your spell.',
    'You can skip a spell by pressing 0'
]

active_spells = []

def explore():
    what = '0'
    while what != 'p':
        what = input("Explore what? \n {1: 'guide', 2: 'players', 3: 'spells', 4: ''} \n(Enter Number): \n 'p' for Play\n")
        if what == '1':
            for j, i in enumerate(guide):
                print('{}: {}'.format(j, i))
        if what == '2':
            for i in players:
                print(i + ', ',)
        if what == '3':
            for k in spells:
                print('{}: {}, '.format(k, spells[k]),)
        else:
            print("Press 'p' to Play")
    create_player()


def initiate():
    for k in sps:
        active_spells.append(Spell(k, spells[k]))

def create_player():

    o = input('Type "p" to start game, and "e" to Explore and press Enter.\n To play a saved game, press "s" : ')
    if o == 'e':
        explore()
    elif o == 'p':
        for k in sps:
            active_spells.append(Spell(k, spells[k]))
        for i, k in enumerate(pps):
            print('{}: {}'.format(i+1, k), sep = ' ')
        name = input('Create Your own Player or select from the options: ')
        try:
            player1 = Player(pps[int(name) - 1])
            player1.speciality = active_spells[sps.index(players[pps[int(name)-1]])]
            pps.remove(player1.name)
        except Exception:
            player1 = Player(name)
            for i, k in enumerate(sps):
                print('{}: {}'.format(i+1, k), sep = ' ')
            print('Select the spell you want as speciality (enter the number): ')
            player1.speciality = active_spells[int(input())-1]
        p2 = pps[randint(0, len(pps) - 1)]
        player2 = Player(p2)
        player2.speciality = active_spells[sps.index(players[p2])]
        player1.spells_available = [i for i in active_spells]
        player2.spells_available = [i for i in active_spells]
        print('Game between {} (You) and {}'.format(player1.name, player2.name))
        l = input('Press any alphabet and hit enter to continue')
        if o:
            g = Game(player1, player2)
            game_func(g)
    elif o == s:
        pass



def game_func(game):
    player1 = game.player
    player2 = game.opponent
    curses.initscr()
    win = curses.newwin(32, 80, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT
    
    p1_spell = [[10, 2], [10, 3]]
    p2_spell = [[10, 77], [10, 76]]
    
    player1.position = [10, 1]
    player2.position = [10, 78]
    h = 0

    while key != 27:
        win.border(0)
        win.addstr(0, 2, ' ' + player1.name + ' : ' + str(player1.power) + ' ')
        win.addstr(0, 30, ' Hogwarts ')
        win.addstr(0, 52, ' ' + player2.name + ' : ' + str(player2.power) + ' ')

        win.addch(player1.position[0], player1.position[1], '#')
        win.addch(player2.position[0], player2.position[1], '#')

        for i in range(1, 79):
            win.addch(20, i, '_')

        if key == ord(' '):
            key = -1
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key == ord('s'):
            game.save()
            curses.endwin()
            print('The Game is saved. You can resume later')
            break


        start1, y = 3, 23
        for i, s in enumerate(player1.spells_available):
            spel = '{0}: {1} ({2}) '.format(i+1, s.name, s.power)
            if start1 + len(spel) + 2 >= 40:
                start1 = 3
                y += 1
            win.addstr(y, start1, spel)
            start1 = start1 + len(spel) + 2
        start2, y = 43, 23
        for i, s in enumerate(player2.spells_available):
            spel = '{0}: {1} ({2}) '.format(i+1, s.name, s.power)
            if start2 + len(spel) + 2 >= 80:
                start2 = 43
                y += 1
            win.addstr(y, start2, spel)
            start2 = start2 + len(spel) + 2
        
        event = win.getch()
        if not event:
            win.addstr(5, 2, 'Press a number based on spell to cast')
        key = 500 if event == -1 else event 

        if game.state == 'select':
            win.timeout(150)

            if not event == -1:
                pass
            else:
                event = None
            if key and key in [49,50,51,52,53,54,55,56,57,58]:

                spell1 = player1.hit(key - 49)
                win.addstr(21, 2, str(spell1))

                spell2 = player2.hit(randint(0, 5))
                win.addstr(21, 52, str(spell2))

                game.state = 'spells'


        elif game.state == 'spells':
            win.timeout(1)
            p1_spell.append([10, p1_spell[-1][-1] + 1])
            p1_spell.append([10, p1_spell[-1][-1] + 1])
            p2_spell.append([10, p2_spell[-1][-1] - 1])
            p2_spell.append([10, p2_spell[-1][-1] - 1])
            if p1_spell[-1][-1] <= p2_spell[-1][-1]:
                for i in range(len(p1_spell)):
                    win.addch(p1_spell[i][0], p1_spell[i][1], '-')
                    win.addch(p2_spell[i][0], p2_spell[i][1], '-')
            else:
                win.addch(p2_spell[0][0], 39, '*')
                clash_result = clash(player1, player2)
                result = check_results(player1, player2, game)
                if result:
                    curses.endwin()
                    print(result)
                elif clash_result:
                    curses.endwin()
                    print(clash_result)
                else:
                    p1_spell = [[10, 2], [10, 3]]
                    p2_spell = [[10, 77], [10, 76]]
                    win = curses.newwin(32, 80, 0, 0)
                    game.state = 'select'

    curses.endwin()


def clash(player1, player2):
    spell1, spell2 = player1.this_spell, player2.this_spell

    if spell1 == player1.speciality:
        player2.power -= 3 * spell1.power
    elif spell2 == player2.speciality:
        player1.power -= 3 * spell2.power

    if spell1.power > spell2.power:
        if spell1.power - spell2.power >= 5:
            return 'Player 1 Kills Player 2, Player 1 wins'
        else:
            player1.power -= (spell2.power - spell1.power)
    elif spell1.power < spell2.power:
        if spell2.power - spell1.power >= 5:
            return 'Player 2 Kills Player 1, Player 2 wins'
        else:
            player2.power -= (spell1.power - spell2.power)
    return None


def check_results(player1, player2, game):
    if player1.power < 10:
        return 'Player1 Lost'
    if player2.power < 10:
        return 'Player2 Lost'
    if not player1.spells_available and not player2.spells_available:
        if player1.power > player2.power:
            return 'Player2 Lost'
        else:
            return 'Player1 Lost'
    if not player2.spells_available:
        return 'Player2 Lost'
    return None

if __name__ == '__main__':
    print('The game will start in a moment')
    time.sleep(0.5)
    create_player()
