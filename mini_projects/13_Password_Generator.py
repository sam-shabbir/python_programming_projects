# Password Generator

import secrets  # For cryptographic random password generation
import string   # For character sets (uppercase, lowercase, digits, symbols)
import math     # For entropy calculation

def generate_password(length=12): # Default length is set to 12 characters
    """Generates a secure password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation # Combine all character sets
    password = ''.join(secrets.choice(characters) for _ in range(length)) # Generate a random password using the combined character set
    return password

def calculate_entropy(password): # Calculate the entropy of the generated password
    # what is entropy? It is a measure of how unpredictable a password is, based on the number of possible combinations.
    # The more characters and character types used, the higher the entropy, making the password more secure against brute-force attacks.
    """Calculates entropy (bits of security) for a given password."""
    char_pool = 0 # Initialize character pool size - this will be used to calculate the total number of possible combinations based on the types of characters in the password.
    # We check for the presence of different character types in the password and add their respective counts to the character pool:
    
    if any(c.islower() for c in password):
        char_pool += 26  # Lowercase letters
    # - If the password contains lowercase letters, we add 26 to the character pool. why add 26? Because there are 26 lowercase letters in the English alphabet.
    if any(c.isupper() for c in password):
        char_pool += 26  # Uppercase letters
    # - If the password contains uppercase letters, we add another 26 to the character pool. This is because there are also 26 uppercase letters in the English alphabet.
    if any(c.isdigit() for c in password):
        char_pool += 10  # Digits
    # - If the password contains digits, we add 10 to the character pool, since there are 10 digits (0-9).
    if any(c in string.punctuation for c in password):
        char_pool += len(string.punctuation)  # Special characters
    # - If the password contains special characters (punctuation), we add the number of punctuation characters available in the string.punctuation set to the character pool.
    # This accounts for all the special characters that can be used in the password.
    entropy = math.log2(char_pool ** len(password)) # calculate the entropy by taking the logarithm base 2 of the total number of possible combinations, which is the character pool raised to the power of the password length. 
    # This gives us the entropy in bits, which indicates how secure the password is.
    # Calculate the total number of possible combinations (char_pool raised to the power of password length) and then take the logarithm base 2 to get the entropy in bits.
    return entropy # The resulting entropy value indicates how secure the password is, with higher values representing stronger passwords.

if __name__ == "__main__": # This block ensures that the code inside it runs only when the script is executed directly, and not when imported as a module in another script.
    # why __ name__ == "__main__"? Because it allows us to control the execution of code and ensures that certain parts of the code are only run when the script is executed directly, rather than when it's imported as a module in another script.
    print("===== Secure Password Generator =====")
    
    while True:
        length = int(input("Enter desired password length: "))
        
        password = generate_password(length)
        entropy = calculate_entropy(password)

        print(f"\nGenerated Password: {password}")
        print(f"Password Entropy: {entropy:.2f} bits")

        if entropy < 50:
            print("⚠️ Weak password! Consider using more characters.")
        elif entropy < 80:
            print("✅ Moderate password. Could be stronger.")
        else:
            print("🔒 Strong password! Very secure.")
        
        user_choice = input("Are you happy with this password? (yes/no): ").strip().lower()
        if user_choice == 'yes':
            print("✅ Password finalized.")
            break
        else:
            print("🔄 Generating a new password...\n")

print("Thank you for using the Secure Password Generator!")
