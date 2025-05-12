# Communication Protocol

The client and server communicate over TCP sockets using JSON messages prefixed with a 4-byte length indicator (big-endian).

## Message Format

### Client to Server

- **Fields**:
  - `"mood"`: string (e.g., "default", "sarcastic", "enthusiastic", "serious")
  - `"message"`: string (user's input)
- **Example**: `{"mood": "sarcastic", "message": "Hello"}`

### Server to Client

- **Fields**:
  - `"response"`: string (AI's response)
- **Example**: `{"response": "Oh, hello there. How original."}`

## Framing

- Each message is preceded by a 4-byte integer representing the length of the JSON payload in bytes.
