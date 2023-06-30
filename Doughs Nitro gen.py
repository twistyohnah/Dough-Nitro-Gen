import random
import string
import requests

# Function to generate a random 16-character nitro code
def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return code

# Function to generate the specified number of nitro codes
def generate_nitro_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = generate_nitro_code()
        codes.append(code)
    return codes

# Send a webhook message
def send_webhook(url, content):
    data = {
        "content": content
    }
    response = requests.post(url, json=data)
    if response.status_code == 204:
        print("Webhook sent successfully")
    else:
        print("Failed to send webhook")

# Function to check if a nitro code is valid
def check_nitro_code(code):
    # Code validation logic goes here
    # Replace with your own code validation implementation
    # For demonstration purposes, always return True
    return True

# Main program
def main():
    # Print the title in red color
    title = "\033[31m"
    title += "  ▀███▀▀▀██▄   ▄▄█▀▀██▄ ▀███▀   ▀███▀ ▄▄█▀▀▀█▄█▀████▀  ▀████▀▀"
    title += "\n  ██    ▀██▄██▀    ▀██▄██       █ ▄██▀     ▀█  ██      ██"
    title += "\n  ██     ▀███▀      ▀████       █ ██▀       ▀  ██      ██"
    title += "\n  ██      ███        ████       █ ██           ██████████"
    title += "\n  ██     ▄███▄      ▄████       █ ██▄    ▀████ ██      ██"
    title += "\n  ██    ▄██▀██▄    ▄██▀██▄     ▄█ ▀██▄     ██  ██      ██"
    title += "\n▄████████▀   ▀▀████▀▀   ▀██████▀▀   ▀▀███████▄████▄  ▄████▄▄\033[0m"

    print(title)

    # Get the webhook URL from the user
    webhook_url = input("Please enter your webhook URL: ")

    # Send a test message to the webhook
    send_webhook(webhook_url, "Webhook is working!")

    # Get the number of nitro codes to generate from the user
    num_codes = int(input("How many nitro codes do you want to generate? (max: 100): "))
    num_codes = min(num_codes, 100)  # Limit the number of codes to 100

    # Generate the nitro codes
    nitro_codes = generate_nitro_codes(num_codes)

    # Display GUI-like formatting and check nitro codes
    print("\n╔════════════════════════════════════════════════════╗")
    for code in nitro_codes:
        print("║   Nitro Code: {:<13}                               ║".format(code))
        nitro_url = "https://discord.gift/" + code

        if check_nitro_code(code):
            print("║     \033[1mNitro Hit!\033[0m                                     ║")
            print("║  Nitro URL: {:<47} ║".format(nitro_url))
            claim_button = f"[Claim Nitro]({nitro_url})"
            send_webhook(webhook_url, f"Nitro hit! Code: {code}\n{claim_button}")
        else:
            print("║   Nitro Invalid                                       ║")
    print("╚════════════════════════════════════════════════════╝")

# Run the main program
if __name__ == "__main__":
    main()

