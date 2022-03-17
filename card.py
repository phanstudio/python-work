import random
from dialog import DialogReader as dr
from collections import Counter

class Deck():
    def __init__(self, typ) -> None:
        self.deck = []
        self.shape = []
        self.checker = []
        self.typ = (typ + " cards")
        self.card_type()
        self.build()
        
    def card_type(self):
        if self.typ == "nija cards":
            self.shape = ["Box", "Circle", "Star", "Angle"]

    def build(self):
        for i in range(1, 15):
            for y in self.shape:
                if not(i > 7 and y == "Star") and i != 1:
                    self.add_card(Card(i, y))
                elif i == 1:
                    self.add_card(Card("A", y))     
        self.checker = self.deck.copy()

    def add_card(self, card):
        if not (card in self.deck):
            self.deck.append(card)

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
        #print(self.deck)

    def draw(self):
        return self.deck.pop()

class Card():
    def __init__(self, num, shape: str) -> None:
        self.shape = shape
        self.num = num
    
    def __repr__(self) -> str:
        if self.num != "A":
            if int(self.num) > 10:
                return str(self.num) + " of " + str(self.shape)
            else:
                return "" + str(self.num) + " of " + str(self.shape)
        else:
            return "" + str(self.num) + " of " + str(self.shape)

    def show(self):
        return str(self.num) + " of " + str(self.shape)

class player():
    def __init__(self, part) -> None:
        self.participants = part
        self.hand = []
        self.name = ("Player" + str(self.participants))
    
    def draw(self, deck):
        self.hand.append(deck.draw())
        print(self.hand[-1])
        return True

    def play(self, which, where):
        cont = []
        h = which.split()
        for x in h:
            if x != "of":
                cont.append(x)
        b = Card(cont[0], cont[1])
        for o in range(len(self.hand)):
            if b.num == str(self.hand[o].num) and b.shape == self.hand[o].shape:
                if b.num == "A":
                    if where.place_card(b) == True:
                        self.hand.pop(o)
                        break
                else:
                    b.num = int(b.num)
                    if where.place_card(b) == True:
                        self.hand.pop(o)
                        break
                    else:
                        print("Wrong Card!")
                        return False
                break
                
    def show(self):
        print(self.hand)

class dealer():
    def deal(self, npp, deck, stac,*player):
        for _ in range(npp):
            for p in player:
                p.hand.append(deck.draw())
        stac.cards.append(deck.draw())
        stac.last_card = stac.cards[0].show()

class stack():
    def __init__(self) -> None:
        self.cards = []
        self.last_card = "0 of nothing"

    def stack_rules(self, *p):
        for i in p:
            if i.hand == []:
                return "finished"

    def place_card(self, card):
        return self.check_card(card)

    def check_card(self, card):
        if not (len(self.cards) > 0):
            self.last_card = "0 of nothing"
        if self.last_card != "0 of nothing":
            c = len(self.cards) - 1
            if card.num == "A" and self.cards[c].shape == card.shape:
                self.cards.append(card)
                self.last_card = card.show()
                print(self.last_card)
                return True
            elif self.cards[c].num == "A" and self.cards[c].shape == card.shape:
                self.cards.append(card)
                self.last_card = card.show()
                print(self.last_card)
                return True
            else:
                if card.num == "A" and self.cards[c].num == "A":
                    self.cards.append(card)
                    self.last_card = card.show()
                    print(self.last_card)
                    return True
                elif self.cards[c].num == card.num or self.cards[c].shape == card.shape:
                    self.cards.append(card)
                    self.last_card = card.show()
                    print(self.last_card)
                    return True
                else:
                    return False
        else:
            self.cards.append(card)
            self.last_card = card.show()
            print(self.last_card)
            return True

class computer(player):
    def __init__(self, part) -> None:
        self.numb = Counter()
        self.shape = Counter()
        self.score = {}
        super().__init__(part)
    
    def rules(self, stac):
        self.cont = False
        self.best = 0
        self.p = 0
        for i in range(len(self.hand)):
            self.numb.update([self.hand[i].num])
            self.shape.update([self.hand[i].shape])
            self.score[self.hand[i]] = 0
            if stac.last_card != "0 of nothing":
                c = len(stac.cards) - 1
                if stac.cards[c].num == self.hand[i].num:
                    self.score[self.hand[i]] += 2
                    self.cont = True
                if  stac.cards[c].shape == self.hand[i].shape:
                    self.score[self.hand[i]] += 2
                    self.cont = True
        if self.cont == True:
            for i in self.score.keys():
                # Shape score
                for j in self.shape.keys():
                    if i.shape == j:
                        self.score[i] += self.shape[j]    
                # Number score
                for j in self.numb.keys():
                    if i.num == j:
                        self.score[i] += self.numb[j]
            for i in range(len(self.score) - 1):
                if self.best < self.score[self.hand[i]]:
                    self.best = self.score[self.hand[i]]
                    self.p = i
            self.score.clear()
            if self.play(self.hand[self.p].show(), stac) != False:
                self.cont = False
                return False
        else:
            return True

    def draw(self, deck):
        self.hand.append(deck.draw())
        return True

nija_what = Deck("nija")
nija_what.shuffle()
p1 = player(1)
com1 = computer(2)
d = dealer()
print("Welcome to the WhatCard game")
s = stack()
d.deal(3, nija_what, s, p1, com1)
p1.show()
r = random.randint(0,1)
print(s.last_card)

turn = r
while True:
    if s.stack_rules(p1, com1) != "finished":
        if turn ==  0:
            print("Your turn!")
            cho = dr.dialog("What do you want to do", "space", quiter= False)
            if cho[:5].lower() == "check":
                p1.show()
            elif cho.lower() == "go_fish" or cho.lower() == "go_to_market":
                print("Player Picked a card from the deck")
                if p1.draw(nija_what): turn += 1
            elif cho[:7].lower() == "shuffle":
                nija_what.shuffle()
            else:
                for i in nija_what.checker:
                    if i.show() == cho:
                        if p1.play(cho, s) != False:
                            turn += 1
        if turn == 1:
            if not com1.rules(s):
                turn = 0
            else:
                print("Computer Picked a card from the deck")
                if com1.draw(nija_what):
                    turn = 0
    else:
        print("Thanks for playing")
        break
