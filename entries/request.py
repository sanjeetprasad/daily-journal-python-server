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


def get_single_journal_entries(id):
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
        JOIN Mood m
            ON m.id = j.mood_id
        WHERE j.id = ?    
        """, (id, ))

        data = db_cursor.fetchone()
        
        journalentry= journalEntries(data['id'], data['concept'], data['entry'], data['date'], data['mood_Id'])
            
        journalentry.__dict__

        return json.dumps(journalentry.__dict__)

def delete_journal_entrie(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM journal_Entries
        WHERE id = ?
        """, (id, ))     