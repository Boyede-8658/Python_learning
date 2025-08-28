from pathlib import Path
from participant.py import save_participant, load_participants

def get_valid_input():
    while True:
        print("\n Please enter participant details:")

        name = input("\tName: ").strip()
        if not name:
            print("\t Name cannot be empty.")
            continue

        try:
            age = int(input("\tAge: ").strip())
        except ValueError:
            print("\t Age must be a number.")
            continue

        phone = input("\tPhone Number: ").strip()
        if not phone.isdigit() or len(phone) != 10:
            print("\t Phone must be 10 digits.")
            continue

        track = input("\tTrack (e.g., Web, Data, Mobile): ").strip()
        if not track:
            print("\t Track cannot be empty.")
            continue

        return {
            "Name": name,
            "Age": age,
            "Phone": phone,
            "Track": track
        }

def main():
    file_path = Path("workspace/contacts.csv")
    file_path.parent.mkdir(exist_ok=True)

    print(" Welcome to the Participant Collector!")

    while True:
        participant = get_valid_input()

        try:
            save_participant(file_path, participant)
            print("\n Participant saved!\n")
        except Exception as e:
            print(f" Failed to save: {e}")

        again = input("Would you like to add another? (y/n): ").strip().lower()
        if again != 'y':
            break

    # Load and summarize
    all_participants = load_participants(file_path)
    print(f"\n Total participants saved: {len(all_participants)}")
    for p in all_participants:
        print(f"\t- {p['Name']} ({p['Track']})")

if __name__ == "__main__":
    main()
