"""
Object-Oriented Programming:
1) Encapsulation
2) Abstraction
3) Inheritance
4) Polymorphism
"""

# from item import Item
from phone import Phone
from keyboard import Keyboard

# item1 = Phone("MyItem",750, 6)

# item1.send_email()

item1 = Keyboard("BobPhone",1000,3)
item1.apply_discount() # inherits method from parent class
print(item1.price)

# item1.name = "OtherItemmmm"

# Item.instantiate_from_csv()

# print(item1.name)

# item1.price = -900
# print(item1.price)
# item1.apply_increment(0.2)
# item1.apply_discount()

# print(item1.price)

    



# phone1 = Phone("jscPhonev10",500,5, 1)

# Item.instantiate_from_csv()

# print(Item.all)
# print()
# print(Phone.all) # we don't need the all list from the child class
# print(phone1.calculate_total_price())

# print(Item.all)

# print(Item.all)
    
# print(Item.is_integer(5.0))

# for instance in Item.all:
#     print(instance.name)
# item1 = Item("Phone",100,5)
# item1.apply_discount()
# print(item1.price)


# item2 = Item("Laptop",1000,3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price,item1.quantity))


# print(item2.calculate_total_price())
# print(item2.calculate_total_price(item2.price,item2.quantity))

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# print(Item.__dict__)
# print(item1.__dict__)

