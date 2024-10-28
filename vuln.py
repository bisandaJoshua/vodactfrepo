# Deliberately vulnerable program to demonstrate unsafe input handling

def vulnerable_input():
    buffer = bytearray(32)  # Small buffer with limited capacity

    print("Enter some text (try to keep it under 32 characters):")
    user_input = input("> ")

    try:
        # Attempting to fit user input into a fixed-size buffer.
        for i in range(len(user_input)):
            buffer[i] = ord(user_input[i])  # Vulnerable to overflow with large input
    except IndexError:
        print("34669e2a04f37e42d2bb99bd5c82ca8e3c604c4be0d5d403989e432352ee00bb4fec893ac7f9df700665c95fa8a5ed38")
    
    print("Stored data:", buffer.decode(errors="ignore"))


# Main function to call the vulnerable input function
if __name__ == "__main__":
    vulnerable_input()
