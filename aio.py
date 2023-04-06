#!/usr/bin/env python3
# (c)J~Net 2023
# jnet.sytes.net
#
# ./aio.py
#
import os
import subprocess

def generate_key():
    if os.path.exists("private_key.txt") and os.path.exists("public_key.txt"):
        os.remove("private_key.txt")
        os.remove("public_key.txt")
        print("Old keys deleted.")
    private_key=subprocess.check_output(["openssl", "genpkey", "-algorithm", "RSA", "-out", "private_key.txt"])
    public_key=subprocess.check_output(["openssl", "pkey", "-in", "private_key.txt", "-pubout", "-out", "public_key.txt"])
    print("Keys generated successfully.")

        

def encrypt_message():
    if not os.path.exists("public_key.txt"):
        print("Public key not found. Please generate a key first.")
        return
    if not os.path.exists("message.txt"):
        message=input("Enter the message to encrypt: ")
        with open("message.txt", "w") as f:
            f.write(message)
    try:
        encrypted=subprocess.check_output(["openssl", "rsautl", "-encrypt", "-pubin", "-inkey", "public_key.txt", "-in", "message.txt"])
        with open("encrypted.txt", "wb") as f:
            f.write(encrypted)
        print("Message encrypted successfully.")
    except subprocess.CalledProcessError:
        print("Unable to encrypt message")

def decrypt_message():
    if not os.path.exists("private_key.txt"):
        print("Private key not found. Please generate a key first.")
        return
    if not os.path.exists("encrypted.txt"):
        print("Encrypted message not found.")
        return
    decrypted = subprocess.check_output(["openssl", "rsautl", "-decrypt", "-inkey", "private_key.txt", "-in", "encrypted.txt"])
    decrypted_message = decrypted.decode()
    print("Decrypted message:", decrypted_message)
    with open("decrypted.txt", "w") as f:
        f.write(decrypted_message)
    print("Decrypted message written to decrypted.txt.")

def menu():
    print("\nPython3 Open-SSL 115 Char Secure Crypto (c) J~Net 2023\n")
    print("1. Generate a new key")
    print("2. Encrypt message")
    print("3. Decrypt message")

    choice=input("\nEnter choice (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        encrypt_message()
    elif choice == "3":
        decrypt_message()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()

