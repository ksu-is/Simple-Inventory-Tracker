import tkinter as tk
from tkinter import messagebox


class InventorySystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.inventory = {}



        # Setting Window Size
        self.root.geometry("600x400")  # Initial size: 600x400 pixels



        # Create Frames
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=20)
        self.frame_display = tk.Frame(root)
        self.frame_display.pack()



        # Add Buttons
        tk.Button(self.frame_buttons, text="List Inventory", command=self.list_inventory).grid(row=0, column=0, padx=10)
        tk.Button(self.frame_buttons, text="Add Category", command=self.add_category_popup).grid(row=0, column=1, padx=10)
        tk.Button(self.frame_buttons, text="Add Item", command=self.add_item_popup).grid(row=0, column=2, padx=10)
        tk.Button(self.frame_buttons, text="Remove Item", command=self.remove_item_popup).grid(row=0, column=3, padx=10)



        # Inventory Display Area
        self.inventory_display = tk.Text(self.frame_display, width=60, height=15, state='disabled', wrap=tk.WORD)
        self.inventory_display.pack(pady=10)





    
    # List Inventory
    def list_inventory(self):
        """Displays the current inventory in the text widget."""
        self.inventory_display.config(state='normal')
        self.inventory_display.delete(1.0, tk.END)

        if not self.inventory:
            self.inventory_display.insert(tk.END, "The inventory is empty.\n")
        else:
            for category, items in self.inventory.items():
                self.inventory_display.insert(tk.END, f"Category: {category}\n")
                for item, quantity in items.items():
                    self.inventory_display.insert(tk.END, f"  {item}: {quantity}\n")
                self.inventory_display.insert(tk.END, "\n")

        self.inventory_display.config(state='disabled')






    # Add Category
    def add_category_popup(self):
        """Popup for adding a new category."""
        popup = tk.Toplevel(self.root)
        popup.title("Add Category")


        tk.Label(popup, text="Category Name:").pack(pady=5)
        entry_category = tk.Entry(popup)
        entry_category.pack(pady=5)

        #Add Category (Sub Section)
        def add_category():
            category = entry_category.get().strip()
            if category:
                if category not in self.inventory:
                    self.inventory[category] = {}
                    messagebox.showinfo("Success", f"Category '{category}' added.")
                else:
                    messagebox.showwarning("Warning", f"Category '{category}' already exists.")
                popup.destroy()
            else:
                messagebox.showerror("Error", "Category name cannot be empty.")

        tk.Button(popup, text="Add", command=add_category).pack(pady=10)








    # Add Item Popup
    def add_item_popup(self):
        """Popup for adding an item."""
        popup = tk.Toplevel(self.root)
        popup.title("Add Item")

        tk.Label(popup, text="Category:").pack(pady=5)
        entry_category = tk.Entry(popup)
        entry_category.pack(pady=5)

        tk.Label(popup, text="Item Name:").pack(pady=5)
        entry_item = tk.Entry(popup)
        entry_item.pack(pady=5)

        tk.Label(popup, text="Quantity:").pack(pady=5)
        entry_quantity = tk.Entry(popup)
        entry_quantity.pack(pady=5)





        # Add Item (Sub Section)
        def add_item():
            category = entry_category.get().strip()
            item_name = entry_item.get().strip()
            try:
                quantity = int(entry_quantity.get().strip())
                if category in self.inventory:
                    self.inventory[category][item_name] = self.inventory[category].get(item_name, 0) + quantity
                    messagebox.showinfo("Success", f"Added {quantity} of '{item_name}' to '{category}'.")
                    popup.destroy()
                else:
                    messagebox.showerror("Error", f"Category '{category}' does not exist.")
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a valid integer.")

        tk.Button(popup, text="Add", command=add_item).pack(pady=10)







    # Remove Item Popup
    def remove_item_popup(self):
        """Popup for removing an item."""
        popup = tk.Toplevel(self.root)
        popup.title("Remove Item")

        tk.Label(popup, text="Category:").pack(pady=5)
        entry_category = tk.Entry(popup)
        entry_category.pack(pady=5)

        tk.Label(popup, text="Item Name:").pack(pady=5)
        entry_item = tk.Entry(popup)
        entry_item.pack(pady=5)

        tk.Label(popup, text="Quantity:").pack(pady=5)
        entry_quantity = tk.Entry(popup)
        entry_quantity.pack(pady=5)









        # Remove Item (Sub Section)
        def remove_item():
            category = entry_category.get().strip()
            item_name = entry_item.get().strip()
            try:
                quantity = int(entry_quantity.get().strip())
                if category in self.inventory and item_name in self.inventory[category]:
                    if self.inventory[category][item_name] >= quantity:
                        self.inventory[category][item_name] -= quantity
                        if self.inventory[category][item_name] == 0:
                            del self.inventory[category][item_name]
                            messagebox.showinfo("Info", f"'{item_name}' removed from '{category}'.")
                        else:
                            messagebox.showinfo("Success", f"Removed {quantity} of '{item_name}' from '{category}'.")
                        popup.destroy()
                    else:
                        messagebox.showerror("Error", f"Not enough '{item_name}' to remove.")
                else:
                    messagebox.showerror("Error", f"Item '{item_name}' not found in '{category}'.")
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a valid integer.")

        tk.Button(popup, text="Remove", command=remove_item).pack(pady=10)







# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  # Window Size
    app = InventorySystemGUI(root)
    root.mainloop()
