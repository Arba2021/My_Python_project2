# --- Get our tools ready ---
# We're adding 'math' for logarithm calculations (for entropy)
# and 'hashlib' for secure password hashing. We also import 'csv' and 'json'
# at the top, which is standard practice.
import random
import string
import math
import hashlib
import csv
import json
from colorama import Fore, Style, init

# Initialize colorama to ensure colors work on all systems
init(autoreset=True)

# --- Define our character sets ---
def password_characters():
    """
    Puts all the possible characters into a neat dictionary.
    This makes it easy to reference them later.
    """
    return {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "digits": string.digits,
        "special": "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    }

# --- Let the user build their character pool ---
def char_pool():
    """
    Asks the user what kinds of characters they want in their passwords
    and builds a single string (the 'pool') to draw characters from.
    """
    char_map = password_characters()
    pool = ""
    print("\n--- Character Set Selection ---")
    option = input("Enter choice: (a = all, c = custom): ").lower()

    if option == "a":
        # The user wants everything, so just mash all the character sets together.
        pool = "".join(char_map.values())
    elif option == "c":
        # The user wants to pick and choose. We'll go through each category.
        for key, value in char_map.items():
            if input(f"Include {key}? (y/n): ").lower() == 'y':
                pool += value
    else:
        # If they enter something weird, we'll play it safe and use all characters.
        print("Invalid choice, using all characters.")
        pool = "".join(char_map.values())
    return pool

# --- NEW: Calculate the password's entropy ---
def calculate_entropy(password, pool_size):
    """
    Calculates the entropy of a password in bits.
    Entropy is a measure of how unpredictable a password is. Higher is better!
    A score over 80 bits is generally considered very strong.
    """
    # The formula is: log2(pool_size ^ password_length), which simplifies to:
    entropy = len(password) * math.log2(pool_size)
    return entropy

# --- Strength checker (now returns raw text) ---
def check_strength(password):
    """
    Analyzes a password and returns its strength as plain text ("Weak", "Medium", "Strong").
    We return raw text so we can save it cleanly to a file without color codes.
    """
    categories = {
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digits": any(c.isdigit() for c in password),
        "special": any(c in password_characters()["special"] for c in password),
    }
    score = sum(categories.values())
    if len(password) < 8 or score < 3:
        return "Weak"
    elif len(password) >= 12 and score >= 3:
        return "Strong"
    else:
        return "Medium"

# --- The main password creation engine ---
def generate_passwords(num_passwords, length, chars, prefix="", show_passwords=True):
    """
    Generates passwords, checks their strength, calculates entropy,
    and stores them in a list of dictionaries for later use.
    """
    passwords_data = []
    pool_size = len(chars) # Get the size of the character pool for entropy calculation.

    print("\n--- Generated Passwords ---")
    for i in range(num_passwords):
        random_part_length = length - len(prefix)
        random_part = ''.join(random.choice(chars) for _ in range(random_part_length))
        password = prefix + random_part

        strength = check_strength(password)
        entropy = calculate_entropy(password, pool_size)
        
        # Store all the important info in a dictionary.
        passwords_data.append({
            "password": password,
            "strength": strength,
            "entropy": entropy
        })

        # --- NEW: Hide password in output if requested ---
        display_pass = password if show_passwords else "[hidden]"
        
        # Colorize the strength for display purposes.
        strength_colors = {"Weak": Fore.RED, "Medium": Fore.YELLOW, "Strong": Fore.GREEN}
        colored_strength = f"{strength_colors.get(strength, Fore.WHITE)}{strength}"
        
        # Display the result to the user, including the new entropy value.
        print(f"Password {i+1}: {display_pass} -> {colored_strength} (Entropy: {entropy:.2f} bits)")
        
    return passwords_data

# --- NEW: Updated save function with hashing ---
def save_passwords(passwords_data):
    """
    Asks the user if they want to save passwords to a file. If yes, it offers
    to hash them with SHA-256 for secure storage before saving.
    """
    choice = input("\nSave passwords to a file? (txt/csv/json/none): ").lower()
    if choice in ["txt", "csv", "json"]:
        # --- NEW: Ask to hash before saving ---
        do_hash = input("Hash passwords before saving for security? (y/n): ").lower() == 'y'
        filename_base = "passwords"
        
        output_data = []
        for p_data in passwords_data:
            password_to_save = p_data["password"]
            if do_hash:
                # Use SHA-256 to create a secure, one-way hash of the password.
                # .encode() converts the string to bytes, which hashing algorithms require.
                password_to_save = hashlib.sha256(password_to_save.encode()).hexdigest()
            
            # We prepare the data for saving, including the password (or its hash).
            output_data.append({
                "password_or_hash": password_to_save,
                "strength": p_data["strength"],
                "entropy_bits": f"{p_data['entropy']:.2f}"
            })

        # Save to the chosen format.
        if choice == "txt":
            with open(f"{filename_base}.txt", "w") as f:
                for item in output_data:
                    f.write(f"Password/Hash: {item['password_or_hash']}, Strength: {item['strength']}\n")
        elif choice == "csv":
            with open(f"{filename_base}.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["password_or_hash", "strength", "entropy_bits"])
                writer.writeheader()
                writer.writerows(output_data)
        elif choice == "json":
             with open(f"{filename_base}.json", "w") as f:
                json.dump(output_data, f, indent=4)
        
        status = "Hashed passwords" if do_hash else "Plain text passwords"
        print(Fore.GREEN + f"✅ {status} saved to {filename_base}.{choice}")
        if not do_hash:
            print(Fore.YELLOW + "⚠️ Warning: Saving passwords in plain text is not recommended.")
    else:
        print("Passwords not saved.")

# --- This is where the program actually starts running ---
if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Advanced Password Generator")
    
    try:
        num_passwords = int(input("How many passwords? "))
        length = int(input("Length of each password? "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter numbers only.")
        exit()
    
    # --- NEW: Option to hide passwords from the console ---
    show_passwords = input("Show passwords in console? (y/n): ").lower() == 'y'

    chars = char_pool()
    if not chars:
        print(Fore.RED + "No character sets selected. Exiting...")
    else:
        prefix = ""
        if input("Include custom prefix? (y/n): ").lower() == 'y':
            prefix = input("Enter your custom prefix: ")

        if len(prefix) >= length:
            print(Fore.RED + "Prefix length must be smaller than total password length.")
            exit()

        # Generate the passwords.
        generated_data = generate_passwords(num_passwords, length, chars, prefix, show_passwords)
        
        # Ask to save the results.
        save_passwords(generated_data)
