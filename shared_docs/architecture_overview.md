# System Architecture

The Multi-Client AI Chatbot System is built on a client-server architecture:

- **Server**:

  - Implemented in Python using a multi-threaded design.
  - Utilizes Hugging Face Transformers (DialoGPT-medium) for AI-driven responses.
  - Manages multiple client connections concurrently via threading.

- **Python Client**:
  - Connects to the server over TCP sockets.
  - Features a command-line interface with commands: `/help`, `/exit`, `/clear`, `/sysinfo`.
  - Supports mood selection for AI responses.

**Communication**:

- Uses TCP sockets with a JSON-based protocol.
- Messages are prefixed with a 4-byte length indicator for reliable transmission.
