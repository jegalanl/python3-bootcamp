from deck import Deck
from hand import Hand
from chips import Chips

def insert_money():
    '''
    Set the money the player starts with
    '''
    while True:
        try:
            money = int(input('How much money would you like to play with?'))
        except ValueError:
            print('Sorry, it must be an integer')
        else:
            return money

def take_bet(chips):
    '''
    Get the numbers of chips the player want to bet
    '''
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    '''
    Get the first card of the deck and adjust player's hand for aces
    '''
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    '''
    Returns True if the player wants to hit or False if the player wants to stand
    '''

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            return True

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            return False

        else:
            print("Sorry, please try again.")
            continue

def show_some(player,dealer):
    '''
    Show player's hand but only one dealer's card
    '''
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(" {}".format(dealer.cards[1]))  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    '''
    Show all cards
    '''
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand = {}".format(dealer.value))
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand = {} \n".format(player.value))

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    '''
    The player and the dealer have the same points
    '''
    print("Dealer and Player tie! It's a push.")


if __name__ == "__main__":
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Set up the Player's chips
    player_money = insert_money()
    player_chips = Chips(player_money)  
    
    while True:    
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_bet(player_chips)
        
        # Show cards but keep one dealer card hidden
        show_some(player_hand,dealer_hand)

        playing = True
        
        while playing:
            
            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(deck,player_hand) 
            
            # Show cards but keep one dealer card hidden
            show_some(player_hand,dealer_hand)  
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break        

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    
        
            # Show all cards
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)        
        
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at",player_chips.total)

        if player_chips.total == 0:
            print("Sorry, you have lost all your money!")
            print("Thanks for playing")
            break
        
        # Ask to play again
        new_game = ''
        while new_game != 'y' and new_game != 'n':
            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game.lower()=='y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break