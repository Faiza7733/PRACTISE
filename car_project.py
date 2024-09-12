import tkinter as tk
from tkinter import messagebox

class MyCar:
    def __init__(self, model, stock):
        self.model = model
        self.stock = stock
    
    def display_stock(self):
        return f"Total cars in stock for {self.model}: {self.stock}"
    
    def rent_for_car(self, quantity):
        if quantity <= 0:
            return "Enter a positive number of cars."
        elif quantity > self.stock:
            return "Not enough cars available."
        else:
            self.stock -= quantity
            total_rent = quantity * 10000  # Example rental rate
            return f"Total rent for {quantity} car(s): ${total_rent}\n" + self.display_stock()
    
    def sell_car(self, quantity):
        if quantity <= 0:
            return "Enter a positive number of cars."
        else:
            self.stock -= quantity
            total_sale = quantity * 15000  # Example sale price
            return f"Total sale for {quantity} car(s): ${total_sale}\n" + self.display_stock()

# Initialize the car objects
car_list = [
    MyCar(model="Toyota Camry", stock=10),
    MyCar(model="Honda Civic", stock=15),
    MyCar(model="Ford Focus", stock=5)
]

def rent_car():
    model = model_var.get()
    quantity = int(quantity_entry.get())
    for car in car_list:
        if car.model == model:
            result = car.rent_for_car(quantity)
            messagebox.showinfo("Rental Information", result)
            return
    messagebox.showerror("Error", "Car model not found.")

def sell_car():
    model = model_var.get()
    quantity = int(quantity_entry.get())
    for car in car_list:
        if car.model == model:
            result = car.sell_car(quantity)
            messagebox.showinfo("Sale Information", result)
            return
    messagebox.showerror("Error", "Car model not found.")

def show_stock():
    model = model_var.get()
    for car in car_list:
        if car.model == model:
            messagebox.showinfo("Car Stock", car.display_stock())
            return
    messagebox.showerror("Error", "Car model not found.")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Car Rental and Sales System")

# Create and place the widgets
tk.Label(root, text="Select Car Model:").pack(pady=10)

model_var = tk.StringVar(value="Toyota Camry")
model_menu = tk.OptionMenu(root, model_var, *[car.model for car in car_list])
model_menu.pack(pady=5)

tk.Label(root, text="Enter number of cars:").pack(pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

rent_button = tk.Button(root, text="Rent Car", command=rent_car)
rent_button.pack(pady=5)

sell_button = tk.Button(root, text="Sell Car", command=sell_car)
sell_button.pack(pady=5)

stock_button = tk.Button(root, text="Show Stock", command=show_stock)
stock_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()


        