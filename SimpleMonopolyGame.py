from Go import Go
from Space import Space
from Player import Player

class SimpleMonopolyGame:
    """Allows two or more people to play a simplified version of the game Monopoly. """

    def __init__(self) -> None:
        """Initializer for the SimpleMonopolyGame class.  Takes no parameters and initializes the private data members,
        which include a dictionary with the players, and a list with the board spaces."""
        self._player_dictionary = {}
        self._spaces_list = []

    def get_player_dictionary(self) -> dict:
        """Get method for player list."""
        return self._player_dictionary

    def get_spaces_list(self) -> list:
        """Get method for spaces list."""
        return self._spaces_list

    def get_player_account_balance(self, name: str) -> int:
        """Takes as a parameter a player's name and returns the player's account balance."""
        return self.get_player_dictionary()[name].get_balance()

    def get_player_current_position(self, name: str) -> int:
        """Takes as a parameter a player's name and return's the player's current position."""
        return self.get_player_dictionary()[name].get_position()

    def get_player_object(self, name: str) -> Player:
        """Takes as a parameter a player's name and returns the Player object."""
        return self.get_player_dictionary()[name]

    def get_current_space_owner(self, position: int) -> str:
        """Takes as a parameter a position, and returns the owner of that position."""
        return self.get_spaces_list()[position].get_owner()

    def get_go_amount(self) -> int:
        """Returns the amount that players receive after passing the Go space."""
        return self.get_spaces_list()[0].get_go_amount()

    def set_space_positions(self) -> None:
        """Called when create_spaces is called to initialize the position order on the board."""

        position = 0

        # Assigns each space in spaces list a position starting from 0.
        for board_space in self._spaces_list:
            board_space.set_position(position)
            position += 1

    def create_spaces(self, go_amount: int, rent_amounts: int) -> None:
        """Takes two parameters: the amount of money given to players when they land on or pass the "GO"
        space, and an array of integers (rent amounts).  Creates respective Go/Space objects, and appends
        them to the spaces_list before calling the set_space_positions method to initialize the positions on
        the board."""
        # First space on the board is the Go space.  A Go object is created, taking the go_amount passed in as
        # a parameter, and appended to the board.
        go_space = Go(go_amount)
        self._spaces_list.append(go_space)

        # For each of the rent amounts in the list passed in, a Space object is created and appended to the board.
        for amount in rent_amounts:
            board_space = Space(amount)
            self._spaces_list.append(board_space)

        # Finally, the set_space_positions method is called to assign a position to each of the board spaces.
        self.set_space_positions()

    def create_player(self, name: str, balance: int) -> None:
        """Takes two parameters: a unique name and an initial account balance.  Creates a Player object and
        adds it to the player_list dictionary, with the name as a key."""

        new_player = Player(name, balance)
        self._player_dictionary[name] = new_player

    def buy_space(self, name: str) -> None:
        """Takes as a parameter a player's name.  If the player has an account balance greater than the purchase
        price, and the space doesn't have an owner, the space is bought by the player."""

        # Owner of the space that the name passed in is on.
        space_owner = self.get_spaces_list()[self.get_player_current_position(name)].get_owner()
        # Price of the space that the name passed in is on.
        space_price = int(self.get_spaces_list()[self.get_player_current_position(name)].get_purchase_price())

        # Player cannot purchase Go space.
        if self.get_player_current_position(name) == 0:
            print("Can't purchase the 'GO' space.")

        # If the player has a balance > space price and the space that they are currently on does not have an owner,
        # space is purchased.
        if self.get_player_account_balance(name) > space_price and space_owner is None:
            self.get_player_object(name).set_balance(0 - space_price)
            self.get_spaces_list()[self.get_player_current_position(name)].set_owner(name)
            print("Space purchased.")

        else:
            print("Not enough balance.")

    def move_player(self, name: str, num_spaces: int) -> None:
        """Takes as parameters the name of the player and the number of spaces to move.  If the player has a balance
        of 0, then it will return immediately without doing anything.  If the player has a balance > 0, they can move
        between 1-6 spaces.  If the player passes the "GO" space, they receive the set amount of money.
        The player will pay rent for the new space occupied, if necessary."""

        # Check to see if the player is still in the game.
        if self.get_player_dictionary()[name].get_balance() == 0:
            return
            
        else:
            # New position is the player's current position + the number of spaces passed in.
            new_position = self.get_player_object(name).get_position() + num_spaces

            # If the end of the board is reached, continue on in a circular manner (from the Go space).  Each time the
            # Go space is passed or landed on, the Go amount is added to their balance.
            if new_position > len(self.get_spaces_list()) - 1:
                self.get_player_object(name).set_balance(self.get_go_amount())
                new_position = new_position % (len(self._spaces_list)-1)
                self.get_player_object(name).set_position(new_position)

                # If the space landed on has an owner, then the player has to pay rent - either the rent amount,
                # or if they don't have enough of a balance, then their entire balance.
                if self.get_current_space_owner(new_position) is not None:
                    space_rent = self.get_spaces_list()[new_position].get_rent_amount()
                    new_position_owner = self.get_current_space_owner(new_position)

                    if self.get_player_object(name).get_balance() >= space_rent:
                        self.get_player_object(new_position_owner).set_balance(space_rent)
                        self.get_player_object(name).set_balance(0-space_rent)

                    else:
                        self.get_player_object(new_position_owner).set_balance(self.get_player_account_balance(name))
                        self.get_player_object(name).set_balance(0-self.get_player_account_balance(name))
                
            else:
                # If the end of the board is not reached, then the player's position is set as the new_position, and
                # the same conditions are checked to see what rent amount is due/adjust appropriate balances.
                self.get_player_object(name).set_position(new_position)

                if self.get_current_space_owner(new_position) is not None:
                    space_rent = self.get_spaces_list()[new_position].get_rent_amount()
                    new_position_owner = self.get_current_space_owner(new_position)

                    if self.get_player_object(name).get_balance() >= space_rent:
                        self.get_player_object(new_position_owner).set_balance(space_rent)
                        self.get_player_object(name).set_balance(0 - space_rent)

                    else:
                        self.get_player_object(new_position_owner).set_balance(self.get_player_account_balance(name))
                        self.get_player_object(name).set_balance(0 - self.get_player_account_balance(name))
               
        # If the player loses (account balance of 0), then they are removed as the owner of any of the spaces that
        # they owned.
        if self.get_player_account_balance(name) == 0:
            for spaces in self.get_spaces_list():
                if spaces.get_owner() == name:
                    spaces.set_owner(None)

    def check_game_over(self) -> bool:
        """Takes no parameters.  The game is over if all but one player have run out of money.  If that is the case,
        the method returns the winning player's name.  Otherwise, the method returns an empty string."""

        zero_balance = 0
        total_players = len(self.get_player_dictionary())

        # Counter for number of players with 0 balance.
        for player in self.get_player_dictionary():
            if self.get_player_object(player).get_balance() == 0:
                zero_balance += 1

        # If there is only one player with a balance > 0, the game is over and that player's name is returned.
        if zero_balance == total_players - 1:
            for player in self.get_player_dictionary():
                if self.get_player_object(player).get_balance() != 0:
                    print(str(player) + " wins.")
                    return True

        else:
            return False