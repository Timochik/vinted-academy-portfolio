import random
import csv
import numpy as np
from faker import Faker

fake = Faker()

# -------------------------------
# CONFIG
# -------------------------------
NUM_ROWS = 2000  # change this after you pick size

GENRES = {
    "Pop": {"danceability": (0.65, 0.15), "energy": (0.7, 0.15), "tempo": (100, 30)},
    "Hip-Hop": {"danceability": (0.75, 0.10), "energy": (0.6, 0.20), "tempo": (140, 20)},
    "R&B": {"danceability": (0.70, 0.20), "energy": (0.5, 0.15), "tempo": (120, 25)},
    "Rock": {"danceability": (0.55, 0.10), "energy": (0.8, 0.10), "tempo": (130, 20)},
    "Electronic": {"danceability": (0.80, 0.10), "energy": (0.85, 0.10), "tempo": (128, 10)},
    "Alternative": {"danceability": (0.60, 0.15), "energy": (0.45, 0.15), "tempo": (115, 20)},
    "Soul": {"danceability": (0.45, 0.15), "energy": (0.35, 0.10), "tempo": (100, 20)},
}

YEARS = list(range(2000, 2024))

# -------------------------------
# STREAMS distribution
# log-normal ~ realistic for Spotify
# -------------------------------
def generate_streams():
    mean = 15
    sigma = 0.5
    return int(np.random.lognormal(mean, sigma))

# -------------------------------
# Track name generator
# -------------------------------
WORDS = ["Love", "Dream", "Night", "Sky", "Heart", "Fire", "Lonely", "Paradise", "Shadow", "Light", "Forever", "Broken"]

def track_name():
    return f"{random.choice(WORDS)} {random.choice(WORDS)}"

# -------------------------------
# MAIN GENERATION LOOP
# -------------------------------
rows = []

for i in range(1, NUM_ROWS + 1):
    genre = random.choice(list(GENRES.keys()))
    g = GENRES[genre]

    danceability = max(0, min(1, random.gauss(g["danceability"][0], g["danceability"][1])))
    energy = max(0, min(1, random.gauss(g["energy"][0], g["energy"][1])))
    tempo = int(random.gauss(g["tempo"][0], g["tempo"][1]))

    row = {
        "track_id": i,
        "track_name": track_name(),
        "artist": fake.name(),
        "genre": genre,
        "release_year": random.choice(YEARS),
        "danceability": round(danceability, 3),
        "energy": round(energy, 3),
        "tempo": tempo,
        "streams": generate_streams(),
    }
    rows.append(row)

# -------------------------------
# SAVE TO CSV
# -------------------------------
filename = "spotify_generated.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {NUM_ROWS} rows → {filename}")
