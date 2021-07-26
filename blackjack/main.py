import random

# helper function
def get_value(rank):
  if rank == "A":
    return 11
  elif rank == "J" or rank == "Q" or rank == "K":
    return 10
  else:
    return int(rank)

# classes
class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = get_value(rank)

  def __str__(self):
    return f"{self.rank} of {self.suit}"

class Deck:
  cards = []
  suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
  ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  def __init__(self):
    for suit in self.suits:
      for rank in self.ranks:
        self.cards.append(Card(suit, rank))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self, number):
    cards_dealt = []
    for x in range(number):
      card = self.cards.pop()
      cards_dealt.append(card)
    return cards_dealt

class Hand:
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    ace_count = 0
    value = 0
    for card in self.cards:
      value += card.value

      if card.rank == "A":
        ace_count += 1

    if ace_count > 0 and value > 21:
      value -= ace_count * 10

    return value

  def get_value(self):
    return self.calculate_value()

  def is_blackjack(self):
    return self.get_value() == 21 and len(self.cards) == 2

  def display(self, showAllCards=False):
    print(f'''{"Dealer's Hand:" if self.dealer else "Your Hand:" }''')

    for item in enumerate(self.cards):
      if showAllCards or not self.dealer or item[0] > 0:
        print(item[1])
      else:
        print('hidden')

    if not self.dealer:
      print("Value:", self.get_value())
    print()

class Game:
  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games would you like to play? "))
      except:
        print("Please enter a number.")
      
    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle()

      player = Hand()
      dealer = Hand(True)

      for i in range(2):
        player.add_card(deck.deal(1))
        dealer.add_card(deck.deal(1))

      print()
      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      print("*" * 30)

      player.display()
      dealer.display()

      if (self.check_winner(player, dealer)):
        continue

      choice = ""
      
      while player.get_value() < 21 and choice not in ["s", "stand"]:
        while choice not in ["s", "stand", "h", "hit"]:
          choice = input("Please choose 'Hit' or 'Stand': ").lower()
        print()

        if choice == "hit" or choice == "h":
          player.add_card(deck.deal(1))
          player.display()
          choice = ""

      if self.check_winner(player, dealer):
        continue

      while dealer.get_value() < 17:
        dealer.add_card(deck.deal(1))
      dealer.display(True)

      self.check_winner(player, dealer, True)
      

  def check_winner(self, player, dealer, game_over=False):
    if not game_over:
      if player.get_value() > 21:
        print("You Busted. Dealer Wins.")
        return True
      elif dealer.get_value() > 21:
        print("Dealer Busted. Dealer Wins.")
        return True
      elif player.is_blackjack() and dealer.is_blackjack():
        print("Both Players got Blackjack. Tie.")
        return True
      elif player.is_blackjack():
        print("You win with a blackjack")
        return True
      elif dealer.is_blackjack():
        print("You lose. Dealer has a blackjack")
        return True
    else:
      if (player.get_value() > dealer.get_value()):
        print("You Win!")
      elif (player.get_value() == dealer.get_value()):
        print("Tied")
      else:
        print("You Lose!")

    # keep going
    return False

# run loop
game = Game()
game.play()