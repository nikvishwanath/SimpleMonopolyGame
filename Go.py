class Go:
    """Represents the "GO" space the board.  Takes the go_amount as a parameter, and initializes
    it along with the location ("GO"), board position (0) and rent amount (None) as private data members with
    associated get/set methods.  The GO space will be added as the first element in the spaces_list in the
    SimpleMonopolyGame object.  The get_go_amount method will be called upon each time a player lands on or passes the
    "GO" space."""

    def __init__(self, go_amount: int) -> None:
        """Initializer for the Go class."""
        self._go_amount = go_amount
        self._location = "GO"
        self._position = 0
        self._rent_amount = None
        self._purchase_price = None
        self._owner = None

    def get_go_amount(self) -> int:
        """Get method for Go amount."""
        return self._go_amount

    def get_location(self) -> int:
        """Get method for Go location. Returns "GO"."""
        return self._location

    def get_position(self) -> int:
        """Get method for Go position.  Returns 0."""
        return self._position

    def get_purchase_price(self) -> int:
        """Get method for Go purchase price.  Returns None."""
        return self._purchase_price

    def get_owner(self) -> str:
        """Get method for Go owner.  Returns None."""
        return self._owner
    
    def get_rent_amount(self) -> int:
        """Get method for Go rent amount,  Returns None"""
        return self._rent_amount

    def set_position(self, position: int) -> None:
        """Set method for Go position.  This method will be called when the spaces are created in the
        SimpleMonopolyGame class.  The Go space will be set to position 0 of the board."""
        self._position = position