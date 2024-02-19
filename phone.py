from item import Item

class Phone(Item): #Child class
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
        # print(f"Instance created: {name}")
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not >= 0"

        # Assign to self object
        self.broken_phones = broken_phones

        # Append to all list every time instance is created
        # Actions to execute