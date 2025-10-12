# Clipboard History Manager

## Description
A Python script that tracks and manages clipboard history using pyperclip. This utility monitors your clipboard for changes, saves the history persistently, and allows you to view or clear past clipboard entries.

## Features
- **Real-time Monitoring**: Continuously tracks clipboard changes
- **Persistent Storage**: Saves clipboard history to JSON file
- **History Display**: View all past clipboard entries with timestamps
- **Configurable Limits**: Set maximum number of entries to store
- **Clear History**: Option to clear all saved clipboard data

## Requirements
```bash
pip install pyperclip
```

## Usage
```bash
python clipboard_history_manager.py
```

### Options:
1. **Monitor clipboard (60 seconds)**: Actively monitors clipboard for 60 seconds and saves any changes
2. **View history**: Display all saved clipboard entries with timestamps
3. **Clear history**: Remove all saved clipboard history

## Implementation Details
- Maximum 50 clipboard entries stored by default
- Entries are saved with timestamp in `clipboard_history.json`
- Only first 200 characters of each entry are stored
- Checks clipboard every second during monitoring

## Example
```python
from clipboard_history_manager import ClipboardHistoryManager

# Create manager instance
manager = ClipboardHistoryManager(max_history=100)

# Monitor for 120 seconds
manager.monitor_clipboard(duration=120)

# Display history
manager.display_history()

# Clear history
manager.clear_history()
```

## Notes
- Requires pyperclip library
- Works on Windows, macOS, and Linux
- History is saved locally in JSON format
- Empty clipboard entries are ignored
