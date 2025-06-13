#!/usr/bin/env python3
"""
Mnemosyne Database Utility
Created: June 13, 2025
Purpose: Command-line utility to interact with the interview prep flashcard database
"""

import sqlite3
import json
import sys
from datetime import datetime
from pathlib import Path

DB_PATH = "data/interview_prep_test.db"

def print_header(title):
    """Print formatted header."""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def list_cards(stage=None, difficulty=None):
    """List flashcards with optional filtering."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = "SELECT id, question, stage, difficulty, tags FROM flashcards"
    params = []
    
    if stage:
        query += " WHERE stage = ?"
        params.append(stage)
    
    if difficulty:
        if stage:
            query += " AND difficulty = ?"
        else:
            query += " WHERE difficulty = ?"
        params.append(difficulty)
    
    query += " ORDER BY stage, difficulty"
    
    cursor.execute(query, params)
    cards = cursor.fetchall()
    
    print(f"Found {len(cards)} flashcards:")
    for card_id, question, stage, diff, tags in cards:
        print(f"\n🆔 ID: {card_id}")
        print(f"📚 Stage: {stage}")
        print(f"🎯 Difficulty: {diff}/5")
        print(f"❓ Question: {question[:80]}{'...' if len(question) > 80 else ''}")
        print(f"🏷️  Tags: {tags}")
    
    conn.close()

def show_card(card_id):
    """Show complete card details."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM flashcards WHERE id = ?", (card_id,))
    card = cursor.fetchone()
    
    if not card:
        print(f"❌ Card with ID {card_id} not found")
        return
    
    print_header(f"FLASHCARD #{card_id}")
    print(f"📚 Stage: {card[5]}")
    print(f"🎯 Difficulty: {card[4]}/5")
    print(f"🏷️  Tags: {card[3]}")
    print(f"📅 Created: {card[6]}")
    print(f"🔄 Reviews: {card[9]}")
    print(f"📊 Success Rate: {card[10]:.1%}" if card[10] else "📊 Success Rate: No data")
    print(f"\n❓ QUESTION:")
    print(card[1])
    print(f"\n✅ ANSWER:")
    print(card[2])
    
    # Show review history
    cursor.execute("""
        SELECT reviewed_at, difficulty_rating, response_time, correct 
        FROM review_sessions 
        WHERE card_id = ? 
        ORDER BY reviewed_at DESC
    """, (card_id,))
    reviews = cursor.fetchall()
    
    if reviews:
        print(f"\n📈 REVIEW HISTORY:")
        for review_date, rating, time_ms, correct in reviews:
            status = "✅ Correct" if correct else "❌ Incorrect"
            time_sec = time_ms / 1000 if time_ms else "N/A"
            print(f"   {review_date}: {status}, Rating: {rating}/5, Time: {time_sec}s")
    
    conn.close()

def add_review(card_id, rating, correct, response_time=None):
    """Add a review session for a card."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Add review session
    cursor.execute("""
        INSERT INTO review_sessions (card_id, difficulty_rating, response_time, correct)
        VALUES (?, ?, ?, ?)
    """, (card_id, rating, response_time, correct))
    
    # Update card statistics
    cursor.execute("""
        UPDATE flashcards 
        SET last_reviewed = CURRENT_TIMESTAMP, 
            review_count = review_count + 1
        WHERE id = ?
    """, (card_id,))
    
    # Recalculate success rate
    cursor.execute("""
        SELECT COUNT(*) as total, SUM(CASE WHEN correct THEN 1 ELSE 0 END) as correct
        FROM review_sessions 
        WHERE card_id = ?
    """, (card_id,))
    
    total, correct_count = cursor.fetchone()
    success_rate = correct_count / total if total > 0 else 0
    
    cursor.execute("""
        UPDATE flashcards 
        SET success_rate = ?
        WHERE id = ?
    """, (success_rate, card_id))
    
    conn.commit()
    conn.close()
    
    print(f"✅ Review added for card {card_id}")
    print(f"   Rating: {rating}/5, Correct: {correct}")
    print(f"   Updated success rate: {success_rate:.1%}")

def stats():
    """Show database statistics."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print_header("DATABASE STATISTICS")
    
    # Total cards
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    total = cursor.fetchone()[0]
    print(f"📊 Total flashcards: {total}")
    
    # Cards by stage
    cursor.execute("SELECT stage, COUNT(*) FROM flashcards GROUP BY stage ORDER BY stage")
    stage_counts = cursor.fetchall()
    print(f"\n📚 Cards by interview stage:")
    for stage, count in stage_counts:
        print(f"   {stage}: {count} cards")
    
    # Cards by difficulty
    cursor.execute("SELECT difficulty, COUNT(*) FROM flashcards GROUP BY difficulty ORDER BY difficulty")
    diff_counts = cursor.fetchall()
    print(f"\n🎯 Cards by difficulty level:")
    for diff, count in diff_counts:
        print(f"   Level {diff}: {count} cards")
    
    # Review statistics
    cursor.execute("SELECT COUNT(*) FROM review_sessions")
    total_reviews = cursor.fetchone()[0]
    print(f"\n📈 Total review sessions: {total_reviews}")
    
    if total_reviews > 0:
        cursor.execute("SELECT AVG(difficulty_rating), AVG(response_time), COUNT(*) as correct FROM review_sessions WHERE correct = 1")
        avg_rating, avg_time, correct_reviews = cursor.fetchone()
        accuracy = (correct_reviews / total_reviews) * 100
        
        print(f"   Average difficulty rating: {avg_rating:.1f}/5")
        print(f"   Average response time: {avg_time/1000:.1f}s" if avg_time else "   Average response time: N/A")
        print(f"   Overall accuracy: {accuracy:.1f}%")
    
    conn.close()

def help_text():
    """Show help information."""
    print_header("MNEMOSYNE DATABASE UTILITY - HELP")
    print("""
🔧 COMMANDS:
   list [stage] [difficulty]     - List flashcards (optional filters)
   show <id>                     - Show complete card details
   review <id> <rating> <correct> [time_ms] - Add review session
   stats                         - Show database statistics
   help                          - Show this help
   
📚 STAGES:
   data_manipulation, culture_fit, mlops, work_history
   
🎯 DIFFICULTY LEVELS:
   1 (very easy) - 5 (very hard)
   
📊 REVIEW RATINGS:
   1 (again) - 5 (perfect)
   
💡 EXAMPLES:
   python3 db_utility.py list data_manipulation
   python3 db_utility.py show 1
   python3 db_utility.py review 1 4 1 12000
   python3 db_utility.py stats
""")

def main():
    """Main CLI interface."""
    if not Path(DB_PATH).exists():
        print(f"❌ Database not found: {DB_PATH}")
        print("💡 Run test_mnemosyne_complete.py first to create the test database")
        return
    
    if len(sys.argv) < 2:
        help_text()
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        stage = sys.argv[2] if len(sys.argv) > 2 else None
        difficulty = int(sys.argv[3]) if len(sys.argv) > 3 else None
        list_cards(stage, difficulty)
    
    elif command == "show":
        if len(sys.argv) < 3:
            print("❌ Usage: show <card_id>")
            return
        card_id = int(sys.argv[2])
        show_card(card_id)
    
    elif command == "review":
        if len(sys.argv) < 5:
            print("❌ Usage: review <card_id> <rating> <correct> [response_time_ms]")
            return
        card_id = int(sys.argv[2])
        rating = int(sys.argv[3])
        correct = bool(int(sys.argv[4]))
        response_time = int(sys.argv[5]) if len(sys.argv) > 5 else None
        add_review(card_id, rating, correct, response_time)
    
    elif command == "stats":
        stats()
    
    elif command == "help":
        help_text()
    
    else:
        print(f"❌ Unknown command: {command}")
        help_text()

if __name__ == "__main__":
    main()
