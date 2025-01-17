# **Buzzline Streaming Data Project**

## **Overview**

The **Buzzline Streaming Data Project** by **Elias Analytics** demonstrates real-time data streaming and analysis. This project consists of two core components: a **Producer** that generates live streaming data and a **Consumer** that processes this data, tracking trends and detecting specific patterns for alerting.

Key features:
- **Producer**: Generates randomized "buzzline" messages and writes them to a log file at regular intervals.
- **Consumer**: Reads the log file in real time, analyzes the messages for positive word usage, tracks trends, and triggers alerts.

This project is ideal for understanding how to implement streaming data workflows, pattern detection, and analytics using Python.

## **Features**

- **Streaming Data Generation**: Using Python generators, the producer creates an endless stream of randomized messages.
- **Real-Time Data Processing**: The consumer reads the log file as it is updated, providing continuous analysis.
- **Alerting System**: Alerts are triggered based on specific conditions, such as when the total count of positive words exceeds a defined threshold.
- **Trend Analysis**: Periodic tracking of message counts over time windows for monitoring purposes.

## **Getting Started**

### **Prerequisites**

Before getting started, ensure you have the following installed:
- **Python 3.11+** (recommended version: 3.11 for compatibility with advanced tools)
- **Git** (for version control)
- **Visual Studio Code (VS Code)** (for development and debugging)

## **Getting Started**

### **Prerequisites**

Before getting started, ensure you have the following installed:
- **Python 3.11+** (recommended version: 3.11 for compatibility with advanced tools)
- **Git** (for version control)
- **Visual Studio Code (VS Code)** (for development and debugging)

Be sure to set up and activate your virtual environment, then install the requirements.txt


## **Usage**

### **Running the Producer**

The **Producer** generates a continuous stream of buzzline messages. To run the producer:

1. Open a terminal in VS Code.
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. Run the producer module:
   - **Windows**:
     ```bash
     py -m producers.basic_producer_case
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m producers.basic_producer_case
     ```

### **Running the Consumer**

The **Consumer** reads and analyzes the log file in real-time, detecting specific patterns and triggering alerts. To run the consumer:

1. Open a new terminal in VS Code.
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. Run the consumer module:
   - **Windows**:
     ```bash
     py -m consumers.basic_consumer_case
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m consumers.basic_consumer_case
     ```

## **License**

This project is licensed under the MIT License. You are free to fork, explore, and modify this project for your personal or professional use. See the [LICENSE](LICENSE.txt) file for more details.

---