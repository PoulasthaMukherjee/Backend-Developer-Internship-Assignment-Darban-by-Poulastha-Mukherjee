# WebSocket Backend Assignment - Darban, By Poulastha Mukherjee

This project implements a WebSocket backend (*in Python*) and a simple HTML client to interact with it. The backend performs the following actions:

1. **Echo:** Echoes the received message in a streaming format with a 0.1-second delay.
2. **Reverse:** Echoes the message in reverse, also in a streaming format with a 0.1-second delay.
3. **Last Character Count:** Counts the occurrences of the last character (*excluding the last one*) in the message.

## Project Structure

- `websocket_server.py`: Python script for the WebSocket server backend.
- `client.html`: HTML file for the client interface.
- `style.css`: CSS file for styling the client interface.
- `script.js`: JavaScript file for handling WebSocket communication and UI interactions.
- `requirements.txt`: List of Python dependencies (***websockets***).

## Setup and Running Locally

1. **Prerequisites:**
   - Make sure you have Python 3.7 or higher installed. You can download it from [https://www.python.org/](https://www.python.org/).
   - Ensure you have a web browser installed (*e.g., Google Chrome, Firefox*).

2. **Install Dependencies (Python):**
   - Open your terminal or command prompt.
   - Navigate to the project directory.
   - Run the following command to install the required Python library (***websockets***):
     ```bash
     pip install -r requirements.txt
     ```

3. **Start the Server:**
   - In the terminal, run the following command to start the WebSocket server:
     ```bash
     python websocket_server.py
     ```

4. **Open the Client:**
   - Double-click the `client.html` file to open it in your web browser. This will connect to the WebSocket server running locally.

## Usage

1. **Type a Message:** Enter your message in the input field on the web page.
2. **Click "Send":** The server will process your message and stream the JSON response back to the web page with a typing effect.
3. **View the Response:** The JSON response will include the original message, the reversed message, the last character, and the count of occurrences of the last character (*excluding the last one*).