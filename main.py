import random

# Define the rooms
rooms = {
    'living_room': {
        'description': 'You are in the living room. There is a door to the north.',
        'north': 'kitchen'
    },
    'kitchen': {
        'description': 'You are in the kitchen. There is a door to the south and a door to the east.',
        'south': 'living_room',
        'east': 'dining_room'
    },
    'dining_room': {
        'description': 'You are in the dining room. There is a door to the west.',
        'west': 'kitchen'
    }
}

# Initialize player state
player_state = {
    'current_room': 'living_room',
    'inventory': []
}

def describe_room(room):
    """Print the description of the current room."""
    description = rooms[room]['description']
    print(description)

def move_player(direction):
    """Move the player in the specified direction."""
    current_room = player_state['current_room']
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        player_state['current_room'] = new_room
        print(f"You moved {direction}.")
        describe_room(new_room)
    else:
        print("You can't go that way!")

def game_loop():
    """Main game loop."""
    print("Welcome to the text-based adventure game!")
    describe_room(player_state['current_room'])
    
    while True:
        command = input("Enter a command (move [direction], quit): ").strip().lower()
        
        if command == 'quit':
            print("Thanks for playing!")
            break
        elif command.startswith('move '):
            direction = command.split(' ', 1)[1]
            move_player(direction)
        else:
            print("Unknown command. Try 'move [direction]' or 'quit'.")

if __name__ == "__main__":
    game_loop()
