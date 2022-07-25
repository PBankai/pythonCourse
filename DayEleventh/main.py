logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""" 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import os
from turtle import clear
def calculate_player_points(player):
    points=0
    for card in player:
        points+=card
    return points
def dealer_cards (dealer,player_points):
    if calculate_player_points(dealer)<21:
        draw_card2="y"
        while(draw_card2=='y' ):
            dealer.append(random.choice(cards))
            if(calculate_player_points(dealer)>player_points or calculate_player_points(dealer)>21):
                draw_card2="n"
    return dealer
continue_game="y"
while continue_game=="y":
    if continue_game=="y":
        os.system("CLS")
        print(logo)
        dealer = [random.choice(cards),random.choice(cards)]
        player = [random.choice(cards),random.choice(cards)]
        print(f"computer first card is {dealer[0]}")
        print (f"Your cards are {player}")
        draw_card=input("Do you want to draw another card (y/n)\n")
        while(draw_card=='y' ):
            player.append(random.choice(cards))
            if(calculate_player_points(player)>21):
                print (f"Your cards are {player}")
                print("You have lost")
                print(f"Dealer cards were {dealer}")
                draw_card='n'
            else: 
                print (f"Your cards are {player}")
                draw_card=input("Do you want to draw another card (y/n)\n")
                if (calculate_player_points(player)<=21):
                    player_points=calculate_player_points(player)
                    dealer_result=dealer_cards(dealer,player_points)
                    dealerPoints= calculate_player_points(dealer_result)
                    player_points=calculate_player_points(player)
                    if( dealerPoints>player_points and dealerPoints==21):
                        print(f"You have Lost again {dealer_result} cards")
                    if( dealerPoints>player_points and dealerPoints>21):
                        print(f"You have won your cards were {player}")
                    if(dealerPoints==player_points):
                        print(f"it was a draw your cards {player}\n the dealer cards were {dealer_result}")
    input("Do you want to continue playing (y/n)\n")
