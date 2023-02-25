from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Generate public and private RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Serialize public key for later use
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt the data using the public key
encrypted_data = public_key.encrypt(
    b"Sensitive data",
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Write the encrypted data and public key to a file
with open("encrypted_file.txt", "wb") as file:
    file.write(encrypted_data)

with open("public_key.pem", "wb") as file:
    file.write(public_pem)
