## WebSocket API Documentation

**Base URL:**

* If testing locally: `ws://localhost:8765`
* If hosting on a server: `ws://<your_server_ip_or_domain>:8765`

**Request Format:**

- Plain text message.

**Response Format:**

- JSON (streamed with 0.1s delay between characters)

```json
{
  "Message": "The original input message",
  "Reverse": "The reversed input message",
  "Last Character": "The last character of the message",
  "Occurrences of [last_char] (excluding the last character)": "Number of occurrences of the last character (excluding the last one)"
}
```

**Example Request:** Hello World! o

**Example Response:** (*Streaming with 0.1s delay between characters*):
```json
{
  "Message": "Hello World! o",
  "Reverse": "o !dlroW olleH",
  "Last Character": "o",
  "Occurrences of o (excluding the last character)": 2
}
```
**How to Test:**

*You can use a WebSocket client like websocat to test the server:*

1. Install websocat:

```bash
pip install websocat
```

2. Run websocat:

```bash
websocat ws://localhost:8765
```

3. Type your message in the websocat terminal and press Enter. The server's JSON response will be streamed back to you.