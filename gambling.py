import random
import time 
from dataclasses import dataclass 
import os
# used AI for blackjack because it was too complex for me
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Player:
   money : int
   irlcash : int
   def win_money(self, amount : int):
      self.money += amount
      print(f"You've succesfully received {amount} tokens!")
      
   def lose_money(self, amount : int):
      self.money -= amount
      print(f"Uh Oh! you've lost {amount} tokens!")
      
   def deposit(self, amount: int):
    amount = int(amount)

    if amount <= 0:
        print("You must deposit at least 1 cash.")
        return

    if amount > self.irlcash:
        print("Uh oh! You don't have enough real cash to deposit that amount.")
        return

    # Cada unidad de irlcash se convierte en 5 tokens
    tokens_gained = amount * 5
    self.money += tokens_gained
    self.irlcash -= amount

    print(f"Successfully deposited {amount} cash! Now you have {self.money} tokens!")

         
    
   def withdraw(self, amount : int):
      amount = int(amount)
      tokens_withdrawn = amount * 5
      if amount <= 0:

         print("Hey... you must add something higher than that")
         return
      if amount > self.money:
         print("Hey... you dont have enough tokens")
         return
      self.money -= tokens_withdrawn
      self.irlcash += amount
      print(f"Succesfully withdrawn {amount} tokens! now you have {self.irlcash} cash")
   
         
          
         
   def coinflip(self, amount : int):
      coin = random.randrange(1,3)
      coin = int(coin)
      print("Heads or tails? [Heads : 1 ,Tails : 2]")
      choice = int(input("choice : "))
      if choice == 2:
         if coin == choice:
            print("you won!")
            self.money += amount
         if coin != choice:
             print("You lost!")
             self.money -= amount
      if choice == 1:
         if coin == choice:
            print("you won!")
            self.money += amount
         if coin != choice:
             print("You lost!")
             self.money -= amount
      return
   def roulette(self, amount: int):
      spin = random.randint(1, 2)  # 1 = Red, 2 = Black
      print("Red or Black? [Red: 1, Black: 2]")
      choice = int(input("choice: "))
      
      if choice == 2:
         if spin == choice:
            print("You won!")
            self.money += amount
         if spin != choice:
            print("You lost!")
            self.money -= amount
      if choice == 1:
         if spin == choice:
            print("You won!")
            self.money += amount
         if spin != choice:
            print("You lost!")
            self.money -= amount
      
      return
   def blackjack(self, amount: int):
    if amount > self.money:
        print("Hey... you don't have enough tokens for that bet!")
        return

    print(f"Starting Blackjack! You bet {amount} tokens.")

    # Crear baraja simplificada (solo valores)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck)

    # Repartir cartas
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    def hand_value(hand):
        total = sum(hand)
        # Ajustar ases
        aces = hand.count(11)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    # Mostrar mano del jugador y la primera carta del dealer
    print(f"Your hand: {player_hand} (total {hand_value(player_hand)})")
    print(f"Dealer shows: {dealer_hand[0]}")

    # Turno del jugador
    while True:
        choice = input("Do you want to Hit or Stand? [H/S]: ").lower()
        if choice == 'h':
            card = deck.pop()
            player_hand.append(card)
            print(f"You drew a {card}. Your hand: {player_hand} (total {hand_value(player_hand)})")
            if hand_value(player_hand) > 21:
                print("Bust! You lost 😢")
                self.lose_money(amount)
                return
        elif choice == 's':
            break
        else:
            print("Please choose H or S")

    # Turno del dealer
    print(f"Dealer's hand: {dealer_hand} (total {hand_value(dealer_hand)})")
    while hand_value(dealer_hand) < 17:
        card = deck.pop()
        dealer_hand.append(card)
        print(f"Dealer draws {card}. Hand: {dealer_hand} (total {hand_value(dealer_hand)})")

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    # Determinar resultado
    if dealer_total > 21 or player_total > dealer_total:
        print("You win! 🎉")
        self.win_money(amount)
    elif player_total < dealer_total:
        print("Dealer wins! 😢")
        self.lose_money(amount)
    else:
        print("It's a tie! 🤝")


      
            
      
      
   
      
p = Player(money=0, irlcash=100)

while True:
  print("""
Hello, welcome to RNG store!
what do you want to do?
 > 1 : Deposit 
 > 2 : Withdraw
 > 3 : Gamble
 > 4 : Close
 > 5 : Balance""")
  choice = int(input("Choice : "))
  if choice == 1:
    print("How much do you want to deposit?")
    amount = input("amount : ")
    p.deposit(amount)
    input("Enter to continue : ")
    clear()
  if choice == 2:
    print("How much you want to withdraw?")
    amount = input("amount : ")
    p.withdraw(amount)
    input("Enter to continue : ")
    clear()
  if choice == 3:
     clear()
     print("""What game do you want to play?
     > Blackjack : 1
     > Coinflip : 2
     > Roulette : 3
     > exit : 4
     """)
     choice = int(input("Choice : "))
     if choice == 1:
        print("How much?")
        amount = int(input("Amount : "))
        p.blackjack(amount)
        pass
     
     if choice == 2:
        print("How much?")
        amount = int(input("Amount : "))
        p.coinflip(amount)
        
     if choice == 3:
        print("How much?")
        amount = int(input("Amount : "))
        p.roulette(amount)

  if choice == 4:
     exit()
     
  if choice == 5:
     print(f"""Balance :
     > Cash : {p.irlcash}
     > Tokens : {p.money}
     """)
     input("Enter to continue : ")
     clear()
     
  else :
   pass