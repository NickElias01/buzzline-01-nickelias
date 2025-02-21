"""
basic_consumer_nickelias.py

This script reads a log file in real-time as it is being written. It analyzes 
the messages for trends and specific patterns, such as the usage of positive words. 
Alerts are triggered when certain thresholds are met, and trends are logged periodically.

Author: Elias Analytics
"""

#####################################
# Import Modules
#####################################

# Python Standard Library
import os
import time
import re
from datetime import datetime, timedelta
from collections import Counter

# Internal Modules
from utils.utils_logger import logger, get_log_file_path

#####################################
# Global Variables
#####################################

# List of positive words to track
POSITIVE_WORDS = ["amazing", "funny", "exciting", "loved", "happy", "thrilled", "amazed"]

# Counters and thresholds
POSITIVE_WORD_COUNT = 0  # Tracks the total number of positive words
ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 5))  # Number of positive words required to trigger an alert

# Time-based metrics
time_window = datetime.now() + timedelta(seconds=60)  # Current time window for tracking trends
window_count = 0  # Tracks the number of messages processed in the current time window

#####################################
# Functions
#####################################

def track_positive_words(message: str) -> None:
    """
    Analyze a message for positive words and update the global count. 
    Trigger an alert if the total count exceeds the defined threshold.

    Args:
        message (str): The log message to analyze.
    """
    global POSITIVE_WORD_COUNT

    # Extract individual words from the message, ignoring punctuation
    words = re.findall(r'\b\w+\b', message.lower())

    # Count occurrences of positive words in the message
    count = sum(words.count(word) for word in POSITIVE_WORDS)
    POSITIVE_WORD_COUNT += count

    # Trigger an alert if the count crosses the threshold
    if POSITIVE_WORD_COUNT >= ALERT_THRESHOLD:
        print(f"ALERT: Positive word count reached {POSITIVE_WORD_COUNT}!")
        logger.warning(f"ALERT: Positive word count reached {POSITIVE_WORD_COUNT}!")
        POSITIVE_WORD_COUNT = 0


def track_trends(message: str) -> None:
    """
    Track the number of messages processed in a fixed time window (e.g., 60 seconds).
    Log the message count when the time window ends and reset the counter.

    Args:
        message (str): The log message to analyze.
    """
    global time_window, window_count

    # Increment the message count for the current time window
    window_count += 1

    # Check if the time window has elapsed
    if datetime.now() >= time_window:
        print(f"Messages in the last 60 seconds: {window_count}")
        logger.info(f"Messages in the last 60 seconds: {window_count}")

        # Reset the time window and message count
        time_window = datetime.now() + timedelta(seconds=60)
        window_count = 0


def process_message(log_file: str) -> None:
    """
    Continuously read a log file and process each new message in real-time. 
    Perform analytics such as trend tracking and positive word detection.

    Args:
        log_file (str): The path to the log file being monitored.
    """
    with open(log_file, "r", encoding="utf-8") as file:
        # Move the file pointer to the end to start reading new messages
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        while True:
            # Read the next line in the file
            line = file.readline()

            # If no new lines are available, wait briefly before retrying
            if not line:
                time.sleep(1)
                continue

            # Process the new log message
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Perform analytics on the message
            track_trends(message)  # Track message trends over time
            track_positive_words(message)  # Detect and count positive words


def main() -> None:
    """
    Main entry point for the consumer script.

    This function:
    - Locates the log file to monitor.
    - Continuously processes new log messages in real-time.
    - Handles graceful shutdown and final logging when stopped by the user.
    """
    logger.info("START...")

    # Locate the log file generated by the producer
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        # Start processing the log file
        process_message(log_file_path)
    except KeyboardInterrupt:
        # Handle user interruption gracefully
        print("User stopped the process.")
        logger.info(f"Final positive word count: {POSITIVE_WORD_COUNT}")

    logger.info("END.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()