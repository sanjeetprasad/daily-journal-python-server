import sqlite3
import json
from models import journalEntries


def get_all_journal_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            j.id,
            j.concept,
            j.entry,
            j.date,
            j.mood_Id
            
        FROM journal_Entries j
        """)

        journalentries=[]

        dataset= db_cursor.fetchall()

        for row in dataset:
            journalentry= journalEntries(row['id'], row['concept'], row['entry'], row['date'], row['mood_Id'])
            
            journalentries.append(journalentry.__dict__)

    return json.dumps(journalentries)


    #                `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	# `concept`	TEXT NOT NULL,
	# `entry`	TEXT NOT NULL,
    # `date`	DATE,
    # `mood_Id` INTEGER NOT NULL,
    # FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)