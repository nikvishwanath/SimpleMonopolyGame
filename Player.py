class Player:
    """Represents a player of the game.  Takes a player's name and account balance as parameters and
    initializes them, along with the player's location and board position, as private data members.  The location
    is initialized to the Go space (position 0). Contains respective get/set methods.  The objects of this
    class are stored as the values within the player_dictionary in the SimpleMonopolyGame class, with the player names
    as the keys."""

    def __init__(self, name: str, balance: int) -> None:
        """Initializer for the Player class."""
        self._name = name
        self._balance = balance
        self._location = "GO"
        self._position = 0

    def get_name(self) -> str:
        """Get method for Player name."""
        return self._name

    def get_balance(self) -> int:
        """Get method for Player balance."""
        return self._balance

    def get_location(self) -> int:
        """Get method for Player location."""
        return self._location

    def get_position(self) -> int:
        """Get method for Player position."""
        return self._position

    def set_position(self, position: int) -> None:
        """Set method for Player position."""
        self._position = position

    def set_balance(self, amount: int) -> None:
        """Set method for Player balance."""
        self._balance += amount