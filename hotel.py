# GUI version of Twin's Cafe using tkinter with modern colorful gradient style
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Menu Items
menu_items = {
    1: ("🍪 Pizza", 100),
    2: ("🍔 Burger", 80),
    3: ("🍝 Masala Dosa", 150),
    4: ("☕ Cold Coffee", 40),
    5: ("🍦 Ice Cream", 60)
}

orders = []
total_amount = 0

def place_order():
    try:
        item_index = int(item_var.get())
        quantity = int(quantity_var.get())

        if item_index not in menu_items:
            messagebox.showerror("Invalid", "Item number not in menu.")
            return

        item_name, price = menu_items[item_index]
        total = price * quantity
        orders.append((item_name, quantity, total))

        update_order_list()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def update_order_list():
    global total_amount
    total_amount = sum(order[2] for order in orders)
    order_list.delete(*order_list.get_children())
    for item, qty, total in orders:
        order_list.insert("", "end", values=(item, qty, f"Rs. {total}"))
    total_label.config(text=f"Total Amount: Rs. {total_amount}")

def show_bill():
    if not name_entry.get() or not mobile_entry.get():
        messagebox.showwarning("Missing Info", "Please enter your name and mobile number.")
        return
    if not orders:
        messagebox.showinfo("No Orders", "No items ordered.")
        return
    bill = f"Customer: {name_entry.get()}\nMobile: {mobile_entry.get()}\n\nItems:\n"
    for item, qty, total in orders:
        bill += f"{item} x{qty} = Rs. {total}\n"
    bill += f"\nTotal: Rs. {total_amount}\n\nThank you! Visit Again! 💖"
    messagebox.showinfo("Final Bill", bill)

# GUI Setup
root = tk.Tk()
root.title("🥧 Twin's Cafe")
root.geometry("700x600")
root.configure(bg="#f3ec78")

# Gradient Header using Canvas
header_canvas = tk.Canvas(root, height=80, width=700, bg="#f3ec78", highlightthickness=0)
header_canvas.pack()
header_canvas.create_rectangle(0, 0, 700, 80, fill="", outline="")
header_canvas.create_text(350, 40, text="Welcome to 🥧 Twin's Cafe", font=("Helvetica", 24, "bold"), fill="#FF1493")

# Customer Info Frame
info_frame = tk.Frame(root, bg="#FFDEE9")
info_frame.pack(pady=10, fill="x", padx=20)

tk.Label(info_frame, text="Name:", font=("Arial", 12), bg="#FFDEE9").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(info_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10)

tk.Label(info_frame, text="Mobile:", font=("Arial", 12), bg="#FFDEE9").grid(row=0, column=2, padx=10)
mobile_entry = tk.Entry(info_frame, font=("Arial", 12))
mobile_entry.grid(row=0, column=3, padx=10)

# Menu Display
menu_frame = tk.Frame(root, bg="#C1FFD7")
menu_frame.pack(pady=10, fill="x", padx=20)

tk.Label(menu_frame, text="MENU", font=("Arial", 16, "bold"), bg="#C1FFD7").pack()
for key, (item, price) in menu_items.items():
    tk.Label(menu_frame, text=f"{key}. {item} - Rs. {price}", font=("Arial", 12), bg="#C1FFD7").pack(anchor="w", padx=20)

# Order Form
form_frame = tk.Frame(root, bg="#FFFCF9")
form_frame.pack(pady=10, fill="x", padx=20)

tk.Label(form_frame, text="Enter Item No:", font=("Arial", 12), bg="#FFFCF9").grid(row=0, column=0, padx=10, pady=5)
item_var = tk.StringVar()
tk.Entry(form_frame, textvariable=item_var, font=("Arial", 12)).grid(row=0, column=1)

tk.Label(form_frame, text="Quantity:", font=("Arial", 12), bg="#FFFCF9").grid(row=0, column=2, padx=10)
quantity_var = tk.StringVar()
tk.Entry(form_frame, textvariable=quantity_var, font=("Arial", 12)).grid(row=0, column=3)

tk.Button(form_frame, text="Add to Order", command=place_order, font=("Arial", 12), bg="#7F00FF", fg="white").grid(row=0, column=4, padx=10)

# Orders Table
table_frame = tk.Frame(root, bg="#E0FFFF")
table_frame.pack(pady=10, padx=20, fill="both", expand=True)

order_list = ttk.Treeview(table_frame, columns=("Item", "Quantity", "Total"), show="headings")
order_list.heading("Item", text="Item")
order_list.heading("Quantity", text="Quantity")
order_list.heading("Total", text="Price")
order_list.pack(fill="both", expand=True)

# Total and Bill
bottom_frame = tk.Frame(root, bg="#E6E6FA")
bottom_frame.pack(fill="x", padx=20, pady=10)

total_label = tk.Label(bottom_frame, text="Total Amount: Rs. 0", font=("Arial", 14, "bold"), bg="#E6E6FA")
total_label.pack(side="left", padx=10)

tk.Button(bottom_frame, text="Generate Bill", command=show_bill, font=("Arial", 14, "bold"), bg="#00C9FF", fg="white").pack(side="right", padx=10)

root.mainloop()
