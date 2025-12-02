# this is notes 
import json
import os

DATE_FILE = "notes.json"

def load_notes():
    if not os.path.exists(DATE_FILE):
        return []
    with open(DATE_FILE, "r") as f:
        return json.load(f)
    
def save_notes(notes):
    with open(DATE_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def list_notes(notes):
    if not notes:
        print("/n[ No notes yet]\n")
        return
    print("\nYour Notes:")
    for i,note in enumerate(notes):
        print(f"{i + 1}. {note}")
    print()

def add_note(notes):
    text = input("Write your note: ").strip()
    if text:
        notes.append(text)
        save_notes(notes)
        print("Saved!\n")
    else:
        print("Empty note ignored.\n")

def delete_note(notes):
    list_notes(notes)
    if not notes:
        return
    try:
        idx = int(input("Which note to delete? (number): ")) -1 
        if 0 <= idx < len(notes):
            removed = notes.pop(idx)
            save_notes(notes)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid number. \n")
    except ValueError:
        print("Please enter a valid number. \n")

def main():
    notes = load_notes()
    
    while True:
        print("=== NOTES APP ===")
        print("1. List notes")
        print("2. Add note")
        print("3. Delete note")
        print("4. Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            list_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()

    