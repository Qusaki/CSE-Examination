# Function to normalize user input to a direction or STOP command
def normalize_direction(cmd):
    cmd = cmd.strip().lower()  # Remove whitespace and convert to lowercase
    if cmd in ['n', 'north']:
        return 'N'
    elif cmd in ['s', 'south']:
        return 'S'
    elif cmd in ['e', 'east']:
        return 'E'
    elif cmd in ['w', 'west']:
        return 'W'
    elif cmd == 'stop':
        return 'STOP'
    else:
        return None  # Invalid input

# Main function to run the GPS tracker simulation
def main():
    x, y = 0, 0  # Start at origin (0, 0)
    print("GPS Tracker Started. You are at (0, 0).")
    print("Enter direction (N/S/E/W or North/South/East/West). Type 'STOP' to end.")
    while True:
        cmd = input("Move: ")  # Get user input
        direction = normalize_direction(cmd)  # Normalize input
        if direction == 'STOP':
            break  # End session if user types STOP
        elif direction == 'N':
            y += 1  # Move north (increase y)
        elif direction == 'S':
            y -= 1  # Move south (decrease y)
        elif direction == 'E':
            x += 1  # Move east (increase x)
        elif direction == 'W':
            x -= 1  # Move west (decrease x)
        else:
            print("Invalid input. Please enter N/S/E/W or North/South/East/West.")
            continue  # Ask for input again if invalid
        print(f"Current position: ({x}, {y})")  # Show current position after move
    print(f"Session ended. Final position: ({x}, {y})")  # Show final position
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")  # Check if back at origin
    else:
        print("You did NOT return to the origin (0, 0).")

if __name__ == "__main__":
    main()  # Run the main function if script is executed directly