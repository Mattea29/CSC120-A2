from computer import Computer
from typing import Optional

class ResaleShop():
    # What attributes will it need? Inventory and itemID to identify object
    inventory = {}
    itemID = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID = 0
        

    # What methods will you need?

    #setting up method to buy computer and add to inventory/update the itemID counter
    def buy(self, computer):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID

    # method for updating just the price of the computer 
    def update_price(self, itemID, new_price):
        if itemID in self.inventory:
            self.inventory[itemID].price = new_price
        else:
            print(f"Item {itemID} not found")

    # method for selling the computer and removing specific computer from inventory
    def sell(self, itemID):
        if itemID in self.inventory:
            del self.inventory[itemID] 
            print(f"Item {itemID} sold!")
        else: 
            print(f"Item {itemID} not found.")

    #method for just printing the inventory for checking at each stage (with conditions for existence of inventory)
    def print_inventory(self): 
        if self.inventory:
            for itemID, computer in self.inventory.items():
                print(f"Item ID: {itemID}")
                computer_info = computer.get_info()
                for key, value in computer_info.items():
                    # trying to print the full description of the computer object
                    print(f"{key} : {value}")
                print()
        else:
            print("No items in inventory.")

    # refurbishing the computer/updating price based on computer year
    def refurbish(self, itemID, new_os : Optional[str] = None, ):
        if itemID in self.inventory:
            computer = self.inventory[itemID]
            if computer.year_made < 2000:
                computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
            else:
                computer.price = 1000
            
            if new_os is not None:
                computer.operating_system = new_os
            else:
                print(f"Item {itemID} not found.")
    
    #method for actual execution of each function
    def run(self):
        print("-" * 21)
        print("Computer Resale Store")
        print("-" * 21)

        #buying the computer and updating the itemID
        computer = Computer("Mac Pro (Late 2013)",
        "Apple M2",
        1024, 8,
        "macOS Big Sur", 2013, 1500)
        print("Buying", computer.description)
        print("Adding to inventory....")
        itemID = self.buy(computer)
        print("Done!")

        #checking inventory
        print("\nChecking inventory....")
        self.print_inventory()
        print("Done.")
       
       # refurbishing inventory and setting price based on year made
        print(f"\nRefurbishing Item {itemID}")
        self.refurbish(itemID, " Apple M20")
        print("Updating inventory...\n")
        print("Checking inventory...")
        self.print_inventory()
        print("Done.")

        # trying just updating the price arbitrarily 
        print(f"\nUpdating price of Item {itemID}...")
        print("Done.\n")
        self.update_price(self.itemID, 210)
        print("Checking inventory...")
        self.print_inventory()
        print("Done.")

        #selling computer
        print(f"\nSelling Item {itemID}")
        self.sell(itemID)
        print("\nChecking inventory...")
        self.print_inventory()
        print("Goodbye!")

        

if __name__ == "__main__":
    shop = ResaleShop()
    shop.run()



        

