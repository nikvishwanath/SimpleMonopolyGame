# SimpleMonopolyGame
# Creator: Nikhil Vishwanath


from random import randint
from SimpleMonopolyGame import SimpleMonopolyGame


# Ask players for names, store results in a list which will be used to initialize the game.  
player_list = []
number_of_players = int(input("Welcome to the Simple Monopoloy Game.  How many players? "))
for number in range(1, number_of_players+1):
    player_name = input("Player " + str(number) + " Name: ")
    player_list.append(player_name)

start_amount = int(input("Enter the amount that each player starts with: "))
go_amount = int(input("Enter the pass 'GO' amount: "))

# Ask players for # of spaces and the rental cost for each (which will be used to determine the 
# purchase price).  
space_list = []
number_of_spaces = int(input("How many spaces? "))
for number in range(1,number_of_spaces+1):
    rental_price = int(input("Enter the rental price for space number " + str(number) + ": "))
    space_list.append(rental_price)

# Visual key for the board.  
print("Board: ")
go = ["GO"]
print(go + space_list)

# Initialize the game.  
game = SimpleMonopolyGame()
game.create_spaces(go_amount, space_list)
for player in player_list:
    game.create_player(player, start_amount)

game_over = 0 # 0: game on, 1: game over. 
turn_counter = 0

# Game loop.  
while game_over != 1:
    player_turn = player_list[turn_counter]
    # Player rolls a random number between 1-6, inclusive.
    dice_roll = randint(1,6) 
    enter_response = input(player_turn + "'s turn, press 'Enter' when ready to roll: ")
    game.move_player(player_turn, dice_roll)
    current_position = game.get_player_current_position(player_turn)
    rent_amount = game.get_spaces_list()[current_position].get_rent_amount()
    current_space_owner = game.get_current_space_owner(current_position)
    
    print(player_turn + " moved " + str(dice_roll) + " spaces.")
    print(player_turn + "'s Position: Space " + str(current_position))

    # If player lands on the "GO" space, there will be no option to purchase the space.
    if game.get_player_current_position(player_turn) == 0:
        print(player_turn + " landed on the 'GO' space.")
        
    # For any other space landed on, if it doesn't have an owner, give the player the option to purchase it.  
    elif game.get_current_space_owner(game.get_player_current_position(player_turn)) is None:
        purchase_price = game.get_spaces_list()[game.get_player_current_position(player_turn)].get_purchase_price()
        print("Purchase Price: " + str(purchase_price))
        print("Rent Amount: " + str(rent_amount))
        purchase_response = input(("Purchase Space? (Y/N): "))
        if purchase_response == "Y":
            game.buy_space(player_turn)
    else:
        print("Pay " + str(current_space_owner) + " " + str(rent_amount))
        
    # Notify player of balance. 
    print("Turn over. " + player_turn + "'s Balance: " + str(game.get_player_account_balance(player_turn)))
    
    # Check to see if game is over. 
    if game.check_game_over() is not False:
        game_over = 1

    # If not, move on to the next player.  
    if turn_counter == number_of_players - 1:
        turn_counter = 0
    else:
        turn_counter += 1

print("Thank you for playing.")

