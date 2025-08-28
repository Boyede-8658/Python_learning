#HELPER MODULE
from pathlib import Path
import csv

def save_participant(path: Path, participant_dict: dict):
    file_exists = path.exists()

    with path.open(mode="a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Phone", "Track"])
        if not file_exists:
            writer.writeheader()  # Write header only once
        writer.writerow(participant_dict)

def load_participants(path: Path):
    participants = []
    if not path.exists():
        return participants

    with path.open(mode="r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            participants.append(row)
    return participants