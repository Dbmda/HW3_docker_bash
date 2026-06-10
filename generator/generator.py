import csv
import random
import os
import sys

NUM_ROWS = 25

COLUMNS = ["group","company","leader", "members_count"]

GROUPS = [
    "BTS",
    "Stray Kids",
    "ATEEZ",
    "TXT",
    "BOYNEXTDOOR",
    "ENHYPEN",
    "SEVENTEEN",
    "TREASURE",
    "NCT DREAM",
    "ZEROBASEONE",
    "EXO"
]

LEADERS = [
    "RM",
    "Bang Chan",
    "Hongjoong",
    "Soobin",
    "Jaehyun",
    "Jungwon",
    "S.Coups",
    "Choi Hyunsuk",
    "Mark",
    "Sung Hanbin",
    "Min Yoongi"
]

COMPANIES = [
    "HYBE",
    "BIGHIT MUSIC",
    "BELIFT LAB",
    "JYP Entertainment",
    "SM Entertainment",
    "YG Entertainment",
    "PLEDIS Entertainment",
    "KQ Entertainment",
    "KOZ Entertainment",
    "WAKEONE"
]

def generate_row():

    return {
        "group": random.choice(GROUPS),
        "company": random.choice(COMPANIES),
        "leader": random.choice(LEADERS),
        "members_count": random.randint(5,12),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

print(f"Data file created: {OUTPUT_FILE}")