#!/usr/bin/env python3
"""
Clipboard History Manager
Tracks and manages clipboard history using pyperclip
"""

import pyperclip
import time
import json
import os
from datetime import datetime
from collections import deque

class ClipboardHistoryManager:
    def __init__(self, max_history=50, save_file='clipboard_history.json'):
        self.max_history = max_history
        self.save_file = save_file
        self.history = deque(maxlen=max_history)
        self.last_clipboard = ""
        self.load_history()
    
    def load_history(self):
        """Load clipboard history from file"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    self.history = deque(data, maxlen=self.max_history)
            except Exception as e:
                print(f"Error loading history: {e}")
    
    def save_history(self):
        """Save clipboard history to file"""
        try:
            with open(self.save_file, 'w') as f:
                json.dump(list(self.history), f, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def monitor_clipboard(self, duration=60):
        """Monitor clipboard for changes"""
        print(f"Monitoring clipboard for {duration} seconds...")
        start_time = time.time()
        
        while time.time() - start_time < duration:
            try:
                current = pyperclip.paste()
                if current != self.last_clipboard and current.strip():
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    entry = {"timestamp": timestamp, "content": current[:200]}
                    self.history.append(entry)
                    self.last_clipboard = current
                    print(f"New clipboard entry: {current[:50]}...")
                    self.save_history()
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)
    
    def display_history(self):
        """Display clipboard history"""
        if not self.history:
            print("No clipboard history available.")
            return
        
        print("\n=== Clipboard History ===")
        for idx, entry in enumerate(reversed(list(self.history)), 1):
            print(f"{idx}. [{entry['timestamp']}] {entry['content']}")
    
    def clear_history(self):
        """Clear clipboard history"""
        self.history.clear()
        self.save_history()
        print("Clipboard history cleared.")

def main():
    manager = ClipboardHistoryManager(max_history=50)
    
    print("Clipboard History Manager")
    print("1. Monitor clipboard (60 seconds)")
    print("2. View history")
    print("3. Clear history")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == '1':
        manager.monitor_clipboard(duration=60)
    elif choice == '2':
        manager.display_history()
    elif choice == '3':
        manager.clear_history()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
