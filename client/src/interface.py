import os
import sys
import time

from colorama import Fore, Style, init
from fuzzywuzzy import process
from logger import log_message
from network import receive_message, send_message


class Interface:
    """Manages the user interface for interacting with the chatbot server."""

    VALID_MOODS = {"default", "sarcastic", "enthusiastic", "serious"}

    def __init__(self, client_socket):
        init(autoreset=True)  # Initialize colorama with auto-reset
        self.client_socket = client_socket
        self.chat_history = []
        self.commands = {
            "/help": self.show_help,
            "/exit": self.exit_chat,
            "/clear": self.clear_chat,
        }

    def type_effect(self, text, delay=0.03, end="\n"):
        """Display text with a typing animation effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if end:
            print(end, end="")

    def show_help(self):
        """Display available commands and moods."""
        help_text = (
            f"\n{Fore.GREEN}Available commands:{Style.RESET_ALL}\n"
            f"{Fore.MAGENTA}/help{Style.RESET_ALL} - Show this help message\n"
            f"{Fore.MAGENTA}/exit{Style.RESET_ALL} - Quit the program\n"
            f"{Fore.MAGENTA}/clear{Style.RESET_ALL} - Clear chat history\n"
            f"{Fore.MAGENTA}/sysinfo{Style.RESET_ALL} - Display system information\n"
            f"\n{Fore.GREEN}Available moods:{Style.RESET_ALL} {', '.join(self.VALID_MOODS)}"
        )
        self.type_effect(help_text)

    def exit_chat(self):
        """Exit the chat application gracefully."""
        self.type_effect(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
        self.client_socket.close()
        sys.exit(0)

    def clear_chat(self):
        """Clear the chat history and screen."""
        os.system("cls" if os.name == "nt" else "clear")
        self.chat_history = []
        self.type_effect(f"{Fore.GREEN}Chat cleared successfully!{Style.RESET_ALL}")
        self.type_effect(f"{Fore.CYAN}New chat session started.{Style.RESET_ALL}\n")

    def get_user_input(self):
        """Get and process user input, handling commands locally."""
        try:
            user_input = input(f"{Fore.CYAN}You:{Style.RESET_ALL} ").strip()
            if not user_input:
                return None
            self.chat_history.append(user_input)
            if user_input.startswith("/"):
                self.handle_command(user_input)
                return None
            return user_input
        except KeyboardInterrupt:
            self.exit_chat()

    def handle_command(self, command):
        """Process user commands with fuzzy matching."""
        matches = process.extractOne(command, self.commands.keys())
        if matches and matches[1] > 70:
            self.commands[matches[0]]()
        elif command.lower() == "/sysinfo":
            from system_info import display_system_info

            display_system_info()
        else:
            self.type_effect(
                f"{Fore.RED}Unknown command. Type /help for options.{Style.RESET_ALL}"
            )

    def get_mood(self):
        """Prompt user for mood and validate input."""
        mood = (
            input("Choose mood (default/sarcastic/enthusiastic/serious): ")
            .strip()
            .lower()
        )
        return mood if mood in self.VALID_MOODS else "default"

    def display_response(self, response):
        """Display the chatbot's response with animation."""
        self.type_effect(f"\n{Fore.MAGENTA}Bot:{Style.RESET_ALL} ", end="")
        self.type_effect(response)

    def run(self):
        """Run the chat interface loop."""
        self.type_effect(
            f"{Fore.GREEN}Chat started. Type /help for commands.{Style.RESET_ALL}"
        )
        while True:
            user_input = self.get_user_input()
            if user_input:
                mood = self.get_mood()
                try:
                    send_message(
                        self.client_socket, {"mood": mood, "message": user_input}
                    )
                    response = receive_message(self.client_socket)
                    if response:
                        self.display_response(response["response"])
                        log_message("user", user_input)
                        log_message("bot", response["response"])
                    else:
                        self.type_effect(
                            f"{Fore.RED}Connection closed by server.{Style.RESET_ALL}"
                        )
                        break
                except Exception as e:
                    self.type_effect(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
                    break
