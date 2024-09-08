import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from ParkingLot import ParkingLot
from ParkingFloor import ParkingFloor
from ParkingSpot import ParkingSpot
from Vehicle import Vehicle

# Initialize the Parking Lot
LOT_NAME = "Xsport Gym Garage"
parking_lot = ParkingLot(LOT_NAME)

def add_floor():
    # Get the floor name from the user
    new_floor_name = floor_name_entry.get()
    if new_floor_name:
        result = parking_lot.add_new_floor(new_floor_name)
        messagebox.showinfo("Floor Added", f"New Floor Added: {result}")
    else:
        messagebox.showwarning("Input Error", "Floor name cannot be empty.")

def display_status():
    status_message = parking_lot.display_status()
    messagebox.showinfo("Parking Lot Status", status_message)

def print_ticket_and_assign_vehicle():
    license_number = vehicle_license_var.get()
    vehicle_type = vehicle_type_var.get()
    if license_number and vehicle_type:
        vehicle = Vehicle(license_number, vehicle_type)
        ticket_info = parking_lot.get_new_parking_ticket(vehicle)
        if ticket_info:
            ticket = ticket_info['ticket']
            messagebox.showinfo("Ticket Issued", f"Ticket Issued:\n{ticket}")
        else:
            messagebox.showwarning("No Available Spots or Duplicate Vehicle", 
                                   "No available parking spots or vehicle already assigned a ticket.")
    else:
        messagebox.showwarning("Input Error", "Please provide both license number and vehicle type.")

def show_admin_menu():
    main_frame.pack_forget()
    admin_frame.pack(fill="both", expand=True)

def show_main_menu():
    admin_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

# Initialize Tkinter window
window = tk.Tk()
window.title(LOT_NAME)

# Main Frame
main_frame = tk.Frame(window)
main_frame.pack(fill="both", expand=True)

# Main Menu
tk.Label(main_frame, text="Assign Vehicle and Print Ticket", font=("Helvetica", 16)).pack(pady=10)
vehicle_license_var = tk.StringVar()
vehicle_type_var = tk.StringVar()
tk.Label(main_frame, text="Vehicle License Number:").pack(pady=5)
tk.Entry(main_frame, textvariable=vehicle_license_var).pack(pady=5)
tk.Label(main_frame, text="Vehicle Type:").pack(pady=5)
tk.Entry(main_frame, textvariable=vehicle_type_var).pack(pady=5)
tk.Button(main_frame, text="Print Ticket and Assign Vehicle", command=print_ticket_and_assign_vehicle).pack(pady=5)
tk.Button(main_frame, text="Go to Admin Menu", command=show_admin_menu).pack(pady=10)

# Admin Frame
admin_frame = tk.Frame(window)
tk.Label(admin_frame, text="Admin Menu", font=("Helvetica", 16)).pack(pady=10)
tk.Button(admin_frame, text="Display Parking Lot Status", command=display_status).pack(pady=5)

tk.Label(admin_frame, text="Add New Floor", font=("Helvetica", 16)).pack(pady=10)
tk.Label(admin_frame, text="Floor Name:").pack(pady=5)
floor_name_entry = tk.Entry(admin_frame)
floor_name_entry.pack(pady=5)
tk.Button(admin_frame, text="Add Floor", command=add_floor).pack(pady=5)

tk.Button(admin_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Start with Main Menu
show_main_menu()

window.mainloop()
