from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

# Create a Fernet cipher using the generated key
cipher = Fernet(key)

# Encrypt the data
encrypted_data = cipher.encrypt(b"Sensitive data")

# Write the encrypted data to a file
with open("encrypted_file.txt", "wb") as file:
    file.write(encrypted_data)
