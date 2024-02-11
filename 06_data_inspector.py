import json
import keyboard
import os

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to load data from a JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to display a record
def display_record(data, index):
    clear_console()
    print(f"[record {index}]")
    print(data[index]['text'])  # Assuming each record has a 'text' key
    print(f"[record {index}]")

# Main function to handle navigation and display
def main(file_path):
    data = load_data(file_path)
    current_index = 0
    display_record(data, current_index)

    while True:
        if keyboard.is_pressed('right'):  # Right arrow key for next record
            current_index = (current_index + 1) % len(data)
            display_record(data, current_index)
            while keyboard.is_pressed('right'):  # Wait until key release
                pass

        elif keyboard.is_pressed('left'):  # Left arrow key for previous record
            current_index = (current_index - 1) % len(data)
            display_record(data, current_index)
            while keyboard.is_pressed('left'):  # Wait until key release
                pass

if __name__ == "__main__":
    file_path = '05_data.json'
    main(file_path)
