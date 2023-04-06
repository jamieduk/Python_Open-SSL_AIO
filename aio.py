#!/usr/bin/env python3
# (c)J~Net 2023
# jnet.sytes.net
#
# ./aio.py
#
import os
import subprocess

print("Python3 Open-SSL Crpto (c) J~Net 2023")

def generate_key_pair():
    # Generate key pair
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "private_key.pem"])
    subprocess.run(["openssl", "pkey", "-in", "private_key.pem", "-out", "key.txt", "-pubout"])
    with open("key.txt", "rb") as f:
        public_key=f.read()
    with open("private_key.pem", "rb") as f:
        private_key=f.read()
    print("Key pair generated.")

def encrypt_message():
    # Read message or prompt user for input
    if os.path.exists("message.txt"):
        with open("message.txt", "rb") as f:
            message=f.read()
    else:
        message=input("Enter message to encrypt: ").encode()

    # Encrypt message
    if message:
        subprocess.run(["openssl", "rsautl", "-encrypt", "-pubin", "-inkey", "key.txt", "-in", "-", "-out", "encrypted.txt"], input=message)
        print("Message encrypted.")
    else:
        print("No message to encrypt.")

def decrypt_message():
    # Decrypt message
    if os.path.exists("encrypted.txt"):
        subprocess.run(["openssl", "rsautl", "-decrypt", "-inkey", "private_key.pem", "-in", "encrypted.txt", "-out", "decrypted.txt"])
        print("Message decrypted.")
    else:
        print("Can't open encrypted.txt for reading, No such file or directory.")

# Check if key pair exists
if os.path.exists("key.txt"):
    with open("key.txt", "rb") as f:
        private_key=f.read()
        public_key=subprocess.check_output(["openssl", "pkey", "-in", "key.txt", "-pubout"])
else:
    generate_key_pair()

# Display menu
while True:
    print("Menu:")
    print("1. Generate Key Pair")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice == "1":
        generate_key_pair()
    elif choice == "2":
        encrypt_message()
    elif choice == "3":
        decrypt_message()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Print decrypted message
if os.path.exists("decrypted.txt"):
    with open("decrypted.txt", "r") as f:
        decrypted_message=f.read()
        print("Decrypted message:")
        print(decrypted_message)
else:
    with open("decrypted.txt", "w") as f:
        f.write("Decrypted message not available")

