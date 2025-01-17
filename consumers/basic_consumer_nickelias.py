"""
basic_consumer_nickelias

Read a log file as it is being written.
"""

#####################################
# Import Modules
#####################################

import os
import time
import re
from datetime import datetime, timedelta
from collections import Counter
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define global variables
#####################################

POSITIVE_WORDS = ["amazing", "funny", "exciting", "loved", "happy", "thrilled", "amazed"]
POSITIVE_WORD_COUNT = 0  # Global counter for positive words
ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 5))  # Configurable alert threshold
time_window = datetime.now() + timedelta(seconds=60)
window_count = 0

#####################################
# Define Functions
#####################################

def track_positive_words(message: str) -> None:
    """
    Track the total number of positive words in messages
    and trigger an alert if the count exceeds the threshold.

    Args:
        message (str): The log message to analyze.
    """
    global POSITIVE_WORD_COUNT

    # Extract words from the message, ignoring punctuation
    words = re.findall(r'\b\w+\b', message.lower())

    # Count occurrences of positive words
    count = sum(words.count(word) for word in POSITIVE_WORDS)
    POSITIVE_WORD_COUNT += count

    if POSITIVE_WORD_COUNT >= ALERT_THRESHOLD:
        print(f"ALERT: Positive word count reached {POSITIVE_WORD_COUNT}!")
        logger.warning(f"ALERT: Positive word count reached {POSITIVE_WORD_COUNT}!")
        POSITIVE_WORD_COUNT = 0


def track_trends(message: str) -> None:
    """
    Track trends in messages over time windows.

    Args:
        message (str): The log message to analyze.
    """
    global time_window, window_count

    window_count += 1

    if datetime.now() >= time_window:
        print(f"Messages in the last 60 seconds: {window_count}")
        logger.info(f"Messages in the last 60 seconds: {window_count}")
        time_window = datetime.now() + timedelta(seconds=60)
        window_count = 0


def process_message(log_file: str) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            message = line.strip()
            print(f"Consumed log message: {message}")

            track_trends(message)  # For trends
            track_positive_words(message)  # Track positive words and trigger alerts


def main() -> None:
    """Main entry point."""
    logger.info("START...")
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
        logger.info(f"Final positive word count: {POSITIVE_WORD_COUNT}")

    logger.info("END.....")


#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()