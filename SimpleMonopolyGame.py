
class NumberMovesError(Exception):
    pass


class Player:
    """Represents a player of the game.  Takes a player's name and account balance as parameters and
    initializes them, along with the player's location and board position as private data members.  The location
    is initialized to the Go space, with the position as 0.Contains respective get/set methods.  The objects of this
    class are stored as the values within the player_dictionary in the RealEstateGame class, with the player names
    as the keys."""

    def __init__(self, name, balance):
        """Initializer for the Player class."""
        self._name = name
        self._balance = balance
        self._location = "GO"
        self._position = 0

    def get_name(self):
        """Get method for Player name."""
        return self._name

    def get_balance(self):
        """Get method for Player balance."""
        return self._balance

    def get_location(self):
        """Get method for Player location."""
        return self._location

    def get_position(self):
        """Get method for Player position."""
        return self._position

    def set_position(self, position):
        """Set method for Player position."""
        self._position = position

    def set_balance(self, amount):
        """Set method for Player balance."""
        self._balance += amount


class Space:
    """Represents a space on the board.  Takes the rent amount as a parameter and initializes it
    along with the purchase price (5 * rent amount), owner (None), and board position (None) as private data
    members with associated get/set methods.  The Space objects are stored in the space_list in the
    SimpleMonopolyGame class."""

    def __init__(self, rent_amount):
        """Initializer for the Space class."""
        self._rent_amount = rent_amount
        self._purchase_price = rent_amount * 5
        self._owner = None
        self._position = None

    def get_owner(self):
        """Get method for Space owner."""
        return self._owner

    def get_rent_amount(self):
        """Get method for Space rent amount."""
        return self._rent_amount

    def get_purchase_price(self):
        """Get method for Space purchase price."""
        return self._purchase_price

    def get_position(self):
        """Get method for Space position."""
        return self._position

    def set_position(self, position):
        """Set method for Space position.  This method will be called when the spaces are created in the
         RealEstateGame class."""
        self._position = position

    def set_owner(self, name):
        """Set method for Space owner.  This method will be called whenever a Player purchases a Space."""
        self._owner = name


class Go:
    """Represents the "GO" space the board.  Takes the go_amount as a parameter, and initializes
    it along with the location ("GO"), board position (0) and rent amount (None) as private data members with
    associated get/set methods.  The GO space will be added as the first element in the spaces_list in the
    RealEstateGame object.  The get_go_amount method will be called upon each time a player lands on or passes the
    "GO" space."""

    def __init__(self, go_amount):
        """Initializer for the Go class."""
        self._go_amount = go_amount
        self._location = "GO"
        self._position = 0
        self._rent_amount = None
        self._purchase_price = None
        self._owner = None

    def get_go_amount(self):
        """Get method for Go amount."""
        return self._go_amount

    def get_location(self):
        """Get method for Go location. Returns "GO"."""
        return self._location

    def get_position(self):
        """Get method for Go position.  Returns 0."""
        return self._position

    def get_purchase_price(self):
        """Get method for Go purchase price.  Returns None."""
        return self._purchase_price

    def get_owner(self):
        """Get method for Go owner.  Returns None."""
        return self._owner

    def set_position(self, position):
        """Set method for Go position.  This method will be called when the spaces are created in the
        RealEstateGame class.  The Go space will be set to position 0 of the board."""
        self._position = position


class SimpleMonopolyGame:
    """Allows two or more people to play a very simplified version of the game Monopoly.  Players take turns rolling
    a single die, and move around the board spaces ("GO" space + 24 other spaces).  The spaces are arranged in a
    circle, and players will pass each space repeatedly.  Each player receives a certain amount of money at the
    start, and also every time they land on or pass the "GO" space.  Each space on the board may be purchased
    except for "GO'.  Once purchased, the owner charges rent to other players who land on the space.  When a player
    runs out of money, that player becomes inactive, and cannot move or own spaces.  The game continues until
    all but one player have run out of money."""

    def __init__(self):
        """Initializer for the RealEstateGame class.  Takes no parameters and initializes the private data members,
        which include a dictionary with the players, and a list with the board spaces."""
        self._player_dictionary = {}
        self._spaces_list = []

    def get_player_dictionary(self):
        """Get method for player list."""
        return self._player_dictionary

    def get_spaces_list(self):
        """Get method for spaces list."""
        return self._spaces_list

    def get_player_account_balance(self, name):
        """Takes as a parameter a player's name and returns the player's account balance."""
        return self.get_player_dictionary()[name].get_balance()

    def get_player_current_position(self, name):
        """Takes as a parameter a player's name and return's the player's current position."""
        return self.get_player_dictionary()[name].get_position()

    def get_player_object(self, name):
        """Takes as a parameter a player's name and returns the Player object."""
        return self.get_player_dictionary()[name]

    def get_current_space_owner(self, position):
        """Takes as a parameter a position, and returns the owner of that position."""
        return self.get_spaces_list()[position].get_owner()

    def get_go_amount(self):
        """Returns the amount that players receive after passing the Go space."""
        return self.get_spaces_list()[0].get_go_amount()

    def set_space_positions(self):
        """Called when create_spaces is called to initialize the position order on the board."""

        position = 0

        # Assigns each space in spaces list a position starting from 0.
        for board_space in self._spaces_list:
            board_space.set_position(position)
            position += 1

    def create_spaces(self, go_amount, rent_amounts):
        """Takes two parameters: the amount of money given to players when they land on or pass the "GO"
        space, and an array of 24 integers (rent amounts).  Creates respective Go/Space objects, and appends
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

    def create_player(self, name, balance):
        """Takes two parameters: a unique name and an initial account balance.  Creates a Player object and
        adds it to the player_list dictionary, with the name as a key."""

        new_player = Player(name, balance)
        self._player_dictionary[name] = new_player

    def buy_space(self, name):
        """Takes as a parameter a player's name.  If the player has an account balance greater than the purchase
        price, and the space doesn't have an owner, the space is bought by the player."""

        # Owner of the space that the name passed in is on.
        space_owner = self.get_spaces_list()[self.get_player_current_position(name)].get_owner()
        # Price of the space that the name passed in is on.
        space_price = int(self.get_spaces_list()[self.get_player_current_position(name)].get_purchase_price())

        # Player cannot purchase Go space.
        if self.get_player_current_position(name) == 0:
            return False

        # If the player has a balance > space price and the space that they are currently on does not have an owner,
        # space is purchased.
        if self.get_player_account_balance(name) > space_price and space_owner is None:
            self.get_player_object(name).set_balance(0 - space_price)
            self.get_spaces_list()[self.get_player_current_position(name)].set_owner(name)
            print("Space purchased.")

        else:
            print("Not enough balance.")

    def move_player(self, name, num_spaces):
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
                        print(new_position_owner + " balance: " + str(self.get_player_account_balance(new_position_owner)))
                        self.get_player_object(name).set_balance(0-space_rent)
                        print(name + " balance: " + str(self.get_player_account_balance(name)))

                    else:
                        self.get_player_object(new_position_owner).set_balance(self.get_player_account_balance(name))
                        print(new_position_owner + " balance: " + str(self.get_player_account_balance(new_position_owner)))
                        self.get_player_object(name).set_balance(0-self.get_player_account_balance(name))
                        print(name + "eliminated.")
                
            else:
                # If the end of the board is not reached, then the player's position is set as the new_position, and
                # the same conditions are checked to see what rent amount is due/adjust appropriate balances.
                self.get_player_object(name).set_position(new_position)

                if self.get_current_space_owner(new_position) is not None:
                    space_rent = self.get_spaces_list()[new_position].get_rent_amount()
                    new_position_owner = self.get_current_space_owner(new_position)

                    if self.get_player_object(name).get_balance() >= space_rent:
                        self.get_player_object(new_position_owner).set_balance(space_rent)
                        print(new_position_owner + " balance: " + str(self.get_player_account_balance(new_position_owner)))
                        self.get_player_object(name).set_balance(0 - space_rent)
                        print(name + " balance: " + str(self.get_player_account_balance(name)))

                    else:
                        self.get_player_object(new_position_owner).set_balance(self.get_player_account_balance(name))
                        print(new_position_owner + " balance: " + str(self.get_player_account_balance(new_position_owner)))
                        self.get_player_object(name).set_balance(0 - self.get_player_account_balance(name))
                        print(name + " eliminated.")
               
        # If the player loses (account balance of 0), then they are removed as the owner of any of the spaces that
        # they owned.
        if self.get_player_account_balance(name) == 0:
            for spaces in self.get_spaces_list():
                if spaces.get_owner() == name:
                    spaces.set_owner(None)

    def check_game_over(self):
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
                    print("The winner is " + player)
                    return True

        else:
            return False
