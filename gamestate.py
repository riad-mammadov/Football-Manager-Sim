import pickle
import os
def save_game(user, filename="savegame.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(user, f)
    print("\nGame saved successfully.")

def load_game(filename="savegame.pkl"):
    try:
        with open(filename, "rb") as f:
            user = pickle.load(f)
        print(f"\nLoaded save for {user.name}, managing {user.team.name}")
        return user
    except FileNotFoundError:
        print("\nNo save file found.")
        return None
    
def delete_game(filename="savegame.pkl"):
    try:
        os.remove(filename)
        print(f"Save deleted successfully.")

    except FileNotFoundError:
        print(f"No save file named {filename} was found.")