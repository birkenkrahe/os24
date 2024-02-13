def handle_command(command):
    # This function handles the commands input by the user
    if command == "exit":
        # If the command is 'exit', stop the kernel loop
        return False
    elif command == "hello":
        # If the command is 'hello', print a greeting message
        print("Hello from the pseudo-kernel!")
    else:
        # Handle any unknown commands
        print(f"Unknown command: {command}")
    return True

def minimal_kernel():
    # This function represents the main loop of the pseudo-kernel
    running = True
    while running:
        # Get command input from the user
        command = input("kernel> ")
        # Process the command and decide whether to continue running
        running = handle_command(command.strip())

if __name__ == "__main__":
    # Entry point of the program
    minimal_kernel()
