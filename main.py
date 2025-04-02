from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import webbrowser
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()
icon_path = "icon.png"
image = Image.open(icon_path)

def connect():
    # Prompt user for IP and Port
    ip = simpledialog.askstring("Connect", "Enter IP address:")
    if not ip:
        print("Invalid IP address")
        return

    port = simpledialog.askinteger("Connect", "Enter Port:")
    if not port:
        print("Invalid port number")
        return

    messagebox.showinfo("Connecting", f"Connecting to {ip}:{port}...")
    # TODO
    print(f"Attempting connection to {ip}:{port}")

def open_settings(): # TODO
    print("Opening settings...")

def open_website():
    webbrowser.open("https://www.linkedin.com/in/petreradu/")

def about(): # TODO
    messagebox.showinfo("About", "Secure File Transfer App\nVersion 1.0")

def exit_app(icon, item):
    icon.stop()

menu = menu(
    item("Connect IP:Port", connect),
    item(
        "Settings",
        menu(
            item("General Settings", open_settings),
            item("Advanced Settings", open_settings),
            item("Network Settings", open_settings),
        )
    ),
    item("Website", open_website),
    item("About", about),
    item("Exit", exit_app)
)

icon = icon("SecureFileTransfer", image, menu=menu)
icon.run()