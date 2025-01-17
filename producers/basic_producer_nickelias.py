"""
basic_producer_nickelias.py

This script generates a continuous stream of "buzz" messages for testing and analytics purposes. 
The messages are randomized and logged at regular intervals, configurable through environment variables.

Author: Elias Analytics
"""

#####################################
# Import Modules
#####################################

# Python Standard Library
import os
import random
import time

# External Libraries (ensure these are installed in the virtual environment)
from dotenv import load_dotenv

# Internal Modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from a `.env` file in the project directory
load_dotenv()

#####################################
# Configuration Functions
#####################################

def get_message_interval() -> int:
    """
    Fetch the message interval (in seconds) from environment variables.

    If no value is provided in the `.env` file, a default of 3 seconds is used.
    This interval determines how frequently new buzz messages are logged.

    Returns:
        int: The message interval in seconds.
    """
    interval_str: str = os.getenv("MESSAGE_INTERVAL_SECONDS", "3")
    interval: int = int(interval_str)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

#####################################
# Data for Generating Buzz Messages
#####################################

# Words and phrases used to generate randomized messages
ADJECTIVES = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS = ["found", "saw", "tried", "shared", "loved"]
TOPICS = ["a movie", "a meme", "an app", "a trick", "a story"]
LOCATIONS = ["in the park", "at the beach", "on the subway", "at the office", "at a friend's place"]
EMOTIONS = ["happy", "confused", "thrilled", "disappointed", "amazed"]

#####################################
# Message Generation Logic
#####################################

def generate_messages():
    """
    Generate an infinite stream of randomized buzz messages.

    The generator yields one message at a time, combining random elements 
    from predefined lists (e.g., adjectives, actions, topics). This approach 
    is memory-efficient and suitable for continuous streaming.

    Yields:
        str: A single buzz message.
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        location = random.choice(LOCATIONS)
        emotion = random.choice(EMOTIONS)
        yield f"I just {action} {topic} {location}! It was {adjective}, and now I feel {emotion}."

#####################################
# Main Function
#####################################

def main() -> None:
    """
    Main entry point for the message generator.

    This function:
    - Retrieves the message interval from environment variables.
    - Continuously generates and logs buzz messages at the specified interval.
    - Provides log outputs for monitoring and debugging.
    """
    logger.info("START producer...")
    logger.info("Hit CTRL+C (or CMD+C) to stop.")

    # Retrieve the message interval from the environment
    interval_secs: int = get_message_interval()

    # Generate and log buzz messages
    for message in generate_messages():
        logger.info(f"[BUZZ] {message}")
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder for detailed output.")
    logger.info("END producer...")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    # Execute the main function if this script is run directly
    main()