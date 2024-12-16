class CommandHandler:
    def __init__(self):
        self.commands = {
            "help": self.help_command,
            "status": self.status_command,
            "exit": self.exit_command,
        }

    def execute(self, command, options):
        """Execute the given command with options."""
        if command in self.commands:
            self.commands[command](options)
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

    def help_command(self, options):
        """Display help information for available commands."""
        print("Available commands:")
        for cmd in self.commands.keys():
            print(f" - {cmd}")

    def status_command(self, options):
        """Display the current status of the system."""
        print("System status: All systems operational.")

    def exit_command(self, options):
        """Exit the CLI."""
        print("Exiting the CLI. Goodbye!")
        exit(0)

if __name__ == "__main__":
    # This part is for testing the command handler independently
    handler = CommandHandler()
    handler.execute("help", [])
