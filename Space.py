class Space:
    """Represents a space on the board.  Takes the rent amount as a parameter and initializes it
    along with the purchase price (5*rent amount), owner (None), and board position (None) as private data
    members with associated get/set methods.  The Space objects are stored in the space_list in the
    SimpleMonopolyGame class."""

    def __init__(self, rent_amount: int) -> None:
        """Initializer for the Space class."""
        self._rent_amount = rent_amount
        self._purchase_price = rent_amount * 5
        self._owner = None
        self._position = None

    def get_owner(self) -> str:
        """Get method for Space owner."""
        return self._owner

    def get_rent_amount(self) -> int:
        """Get method for Space rent amount."""
        return self._rent_amount

    def get_purchase_price(self) -> int:
        """Get method for Space purchase price."""
        return self._purchase_price

    def get_position(self) -> int:
        """Get method for Space position."""
        return self._position

    def set_position(self, position: int) -> None:
        """Set method for Space position.  This method will be called when the spaces are created in the
         SimpleMonopolyGame class."""
        self._position = position

    def set_owner(self, name: str) -> None:
        """Set method for Space owner.  This method will be called whenever a Player purchases a Space."""
        self._owner = name