



class InventorySystem:
    def __init__(self):
        # Dictionary to store items in the format: {category: {item_name: quantity}} Just like this.
        self.inventory = {}



    # List Inventory
    def list_inventory(self):
        # Lists all items in the inventory with their categories and quantities. Very Important.
        print("\nCurrent Inventory:")
        if not self.inventory:
            print("The inventory is empty.")
        for category, items in self.inventory.items():
            print(f"\nCategory: {category}")
            for item, quantity in items.items():
                print(f"  {item}: {quantity}")
        print()



    # Categorys
    def add_category(self, category):
        # Adds a new category to the inventory
        if category not in self.inventory:
            self.inventory[category] = {}
            print(f"Category '{category}' added.")
        else:
            print(f"Category '{category}' already exists.")



    # Add Items
    def add_item(self, category, item_name, quantity):
        # Adds an item to the specified category
        if category not in self.inventory:
            print(f"Category '{category}' does not exist. Add the category first.")
            return

        self.inventory[category][item_name] = self.inventory[category].get(item_name, 0) + quantity
        print(f"Added {quantity} of '{item_name}' to '{category}'.")



    # Remove Items
    def remove_item(self, category, item_name, quantity):
        # Removes a specified quantity of an item
        if category in self.inventory and item_name in self.inventory[category]:
            if self.inventory[category][item_name] >= quantity:
                self.inventory[category][item_name] -= quantity
                print(f"Removed {quantity} of '{item_name}' from '{category}'.")

                # Remove the item if quantity becomes zero
                if self.inventory[category][item_name] == 0:
                    del self.inventory[category][item_name]
                    print(f"'{item_name}' is out of stock in '{category}'.")
            else:
                print(f"Cannot remove {quantity} of '{item_name}' - only {self.inventory[category][item_name]} available.")
        else:
            print(f"Item '{item_name}' not found in '{category}'.")



    # Track Changes
    def track_changes(self, action, category, item_name, quantity):
        # Tracks changes made to inventory
        print(f"Action: {action} | Category: {category} | Item: {item_name} | Quantity: {quantity}")



    #Updates Inventory
    def update_inventory(self, action, category, item_name, quantity):
        # Updates inventory based on action and logs the changes
        if action == "add":
            self.add_item(category, item_name, quantity)
        elif action == "remove":
            self.remove_item(category, item_name, quantity)
        self.track_changes(action, category, item_name, quantity)



    # Menu 
    def menu(self):
        while True:
            print("\nInventory Management System")
            print("1. List Inventory")
            print("2. Add Category")
            print("3. Add Item")
            print("4. Remove Item")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.list_inventory()
            elif choice == "2":
                category = input("Enter the name of the new category: ")
                self.add_category(category)
            elif choice == "3":
                category = input("Enter the category: ")
                item_name = input("Enter the item name: ")
                quantity = int(input("Enter the quantity: "))
                self.update_inventory("add", category, item_name, quantity)
            elif choice == "4":
                category = input("Enter the category: ")
                item_name = input("Enter the item name: ")
                quantity = int(input("Enter the quantity to remove: "))
                self.update_inventory("remove", category, item_name, quantity)
            elif choice == "5":
                print("Exiting the Inventory Management System.")
                break
            else:
                print("Invalid choice. Please try again.")




# Initialize and run the inventory system
inventory = InventorySystem()
inventory.menu()

