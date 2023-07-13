import time
import random
import string
import threading
import tkinter as tk
import requests
from colorama import Fore, init

# Initialize colorama
init()

# Global variables
owner_keys = {
    "twistyohnah": 10000,
}
admin_keys = {
    "ksvthegoat": 300,
}
paid_keys = {
    "twistyonyoutube": 100,
    "15567": 100,
}
free_keys = []
used_keys = []

# Function to generate Nitro codes and send them to Discord webhook
def generate_nitro_codes(webhook_url, num_codes):
    # Simulating the process of generating Nitro codes
    for _ in range(num_codes):
        time.sleep(1)  # Simulate a delay of 1 second
        nitro_code = generate_random_code()
        send_to_webhook(webhook_url, nitro_code)

# Function to generate a random Nitro code
def generate_random_code():
    code_length = 16
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for _ in range(code_length))
    return f"https://discord.gift/{code}"

# Function to send data to Discord webhook
def send_to_webhook(webhook_url, content):
    data = {"content": content}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send data to webhook. Error code: {response.status_code}")

# Function to create the GUI
def generate_nitro_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Nitro Generator")
    window.geometry("500x400")
    window.configure(bg="black")

    # Create and position the elements in the GUI
    header_label = tk.Label(window, text="""
▀███▀▀▀██▄   ▄▄█▀▀██▄ ▀███▀   ▀███▀ ▄▄█▀▀▀█▄█▀████▀  ▀████▀▀
  ██    ▀██▄██▀    ▀██▄██       █ ▄██▀     ▀█  ██      ██   
  ██     ▀███▀      ▀████       █ ██▀       ▀  ██      ██   
  ██      ███        ████       █ ██           ██████████   
  ██     ▄███▄      ▄████       █ ██▄    ▀████ ██      ██   
  ██    ▄██▀██▄    ▄██▀██▄     ▄█ ▀██▄     ██  ██      ██   
▄████████▀   ▀▀████▀▀   ▀██████▀▀   ▀▀███████▄████▄  ▄████▄▄
""", font=("Courier New", 12, "bold"), fg="yellow", bg="black")
    header_label.pack(pady=20)

    key_label = tk.Label(window, text="Enter your key:", font=("Courier New", 16), fg="white", bg="black")
    key_label.pack(pady=10)

    key_entry = tk.Entry(window, font=("Courier New", 16), show="*")
    key_entry.pack()

    def verify_key():
        key = key_entry.get().strip()
        if key in owner_keys:
            show_generation_section(owner_keys[key], "Owner Key")
        elif key in admin_keys:
            show_generation_section(admin_keys[key], "Admin Key")
        elif key in paid_keys:
            show_generation_section(paid_keys[key], "Paid Key")
        elif key in free_keys:
            show_generation_section(50, "Free Key")
        else:
            key_label.config(text="Invalid Key", fg="red")

    def show_generation_section(max_codes, key_type):
        key_label.config(text=f"{key_type} - Key Verified", fg="green")
        key_entry.config(state="disabled")
        webhook_label.pack()
        webhook_entry.pack()
        num_codes_label.config(text=f"Enter the number of codes to generate (max {max_codes}):")
        num_codes_label.pack()
        num_codes_entry.pack()
        generate_button.config(state="normal")
        max_codes_label.config(text=f"Max Codes: {max_codes}")

    verify_button = tk.Button(window, text="Verify Key", font=("Courier New", 16), command=verify_key)
    verify_button.pack(pady=10)

    webhook_label = tk.Label(window, text="Enter Discord Webhook:", font=("Courier New", 16), fg="white", bg="black")
    webhook_entry = tk.Entry(window, font=("Courier New", 16))
    num_codes_label = tk.Label(window, text="Enter the number of codes to generate:", font=("Courier New", 16), fg="white", bg="black")
    num_codes_entry = tk.Entry(window, font=("Courier New", 16))

    def start_generation():
        num_codes = int(num_codes_entry.get())
        if num_codes > max_codes:
            num_codes = max_codes
        generate_nitro_codes(webhook_entry.get(), num_codes)
        generate_button.config(text="Generating...", state="disabled")
        threading.Thread(target=loading_animation).start()

    generate_button = tk.Button(window, text="Generate", font=("Courier New", 16), command=start_generation, state="disabled")

    max_codes_label = tk.Label(window, text="", font=("Courier New", 12), fg="white", bg="black")

    loading_label = tk.Label(window, text="", font=("Courier New", 16), fg="yellow", bg="black")

    # Loading animation
    def loading_animation():
        start_time = time.time()
        while time.time() - start_time < 6:
            for _ in range(3):
                loading_label.config(text="Loading.")
                time.sleep(0.2)
                loading_label.config(text="Loading..")
                time.sleep(0.2)
                loading_label.config(text="Loading...")
                time.sleep(0.2)

        loading_label.config(text="Done!", fg="green")

    # Run the GUI
    window.mainloop()

# Run the Nitro code generator GUI directly
generate_nitro_gui()
