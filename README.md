# Multi-Client AI Chatbot System

This project implements a multi-client chatbot system with a Python server powered by Hugging Face Transformers and a Python client for user interaction. The server handles multiple concurrent clients using multi-threading, and the client provides a command-line interface with mood-based interactions.

## Features

- Client-server architecture over TCP
- AI chatbot powered by Hugging Face `DialoGPT-medium`
- Multi-threaded server for concurrent client support
- Commands: `/help`, `/exit`, `/clear`, `/sysinfo`
- Mood options: `default`, `sarcastic`, `enthusiastic`, `serious`
- Monorepo structure

## Directory Structure

- `server/`:
  - `src/`: Server source code
  - `tests/`: Server unit tests
  - `requirements.txt`: Server dependencies
- `client_python/`:
  - `src/`: Client source code
  - `tests/`: Client unit tests
  - `requirements.txt`: Client dependencies
- `shared_docs/`: Architecture and protocol documentation
- `scripts/`: Utility scripts for running components

## Prerequisites

- Python 3.8+
- Git
- (Optional) Conda (if using Conda for environment management)

## Setup

### Using Virtual Environments

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/moaz-loaie/chatbot.git
   cd chatbot
   ```

2. **Server Setup**:

   - **Unix-like systems**:

     ```bash
     cd server
     python -m venv venv_server
     source venv_server/bin/activate
     pip install -r requirements.txt
     cd ..
     ```

   - **Windows**:

     ```cmd
     cd server
     python -m venv venv_server
     venv_server\Scripts\activate
     pip install -r requirements.txt
     cd ..
     ```

3. **Client Setup**:

   - **Unix-like systems**:

     ```bash
     cd client_python
     python -m venv venv_client
     source venv_client/bin/activate
     pip install -r requirements.txt
     cd ..
     ```

   - **Windows**:

     ```cmd
     cd client_python
     python -m venv venv_client
     venv_client\Scripts\activate
     pip install -r requirements.txt
     cd ..
     ```

### Using Conda

If you prefer to use Conda for managing environments, follow these steps:

#### Server Setup with Conda

```bash
conda env create -p server_env -f environment.yml
conda activate server_env
```

#### Client Setup with Conda

```bash
conda env create -p client_env -f environment.yml
conda activate client_env
```

**Note**: Ensure you have Conda installed. If not, refer to the Conda installation guide.

## Running the Application

### Using Virtual ENvironments

1. **Start the Server**:

   - **Unix-like systems**:

     ```bash
     cd server
     source venv_server/bin/activate
     python src/main_server.py
     ```

   - **Windows**:

     ```cmd
     cd server
     venv_server\Scripts\activate
     python src/main_server.py
     ```

2. **Start the Client**:

   - In a new terminal:

     - **Unix-like systems**:

       ```bash
       cd client_python
       source venv_client/bin/activate
       python src/main_client.py
       ```

     - **Windows**:

       ```cmd
       cd client_python
       venv_client\Scripts\activate
       python src/main_client.py
       ```

### Using COnda

1. **Start the Server**:

   - Activate the server environment:

     ```bash
     conda activate server_env
     ```

   - Run the server:

     ```bash
     python server/src/main_server.py
     ```

2. **Start the Client**:

   - In a new terminal, activate the client environment:

     ```bash
     conda activate client_env
     ```

   - Run the client:

     ```bash
     python client_python/src/main_client.py
     ```

### Using Scripts (Optional)

Alternatively, you can use the provided scripts for convenience:

- **Unix-like systems**:

  - Start the server: `./scripts/run_server.sh`
  - Start the client: `./scripts/run_python_client.sh`

- **Windows**:

  - Start the server: `scripts\run_server.bat`
  - Start the client: `scripts\run_python_client.bat`

**Note**: Ensure you run the server before starting any clients.

## Interaction

- Type messages or commands (e.g., `/help`).
- Select a mood when prompted.

## Running Tests

The project includes unit tests for both the server and client components. These tests use Python's built-in `unittest` module, so no additional libraries are required beyond the standard Python installation.

### Server Tests

1. Navigate to the `server/` directory.
2. Activate the server environment:
   - Virtual environment: `source venv_server/bin/activate` (Unix) or `venv_server\Scripts\activate` (Windows)
   - Conda: `conda activate server_env`
3. Run the tests:

   ```bash
   python -m unittest discover tests
   ```

### Client Tests

1. Navigate to the `client_python/` directory.
2. Activate the client environment:
   - Virtual environment: `source venv_client/bin/activate` (Unix) or `venv_client\Scripts\activate` (Windows)
   - Conda: `conda activate client_env`
3. Run the tests:

   ```bash
   python -m unittest discover tests
   ```

## Notes

- Logs are saved in `logs/` directories within `server/` and `client_python/`.
- Ensure the server is running before starting clients.
- The AI model is loaded once at server startup for efficiency, as implemented in `ai_model_interface.py`.
