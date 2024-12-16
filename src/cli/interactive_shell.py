import cmd
from commands import CommandHandler

class InteractiveShell(cmd.Cmd):
    intro = 'Welcome to the interactive shell. Type help or ? to list commands.'
    prompt = '(shell) '

    def __init__(self):
        super().__init__()
        self.command_handler = CommandHandler()

    def do_help(self, arg):
        """Display help information for available commands."""
        self.command_handler.help_command([])

    def do_status(self, arg):
        """Display the current status of the system."""
        self.command_handler.status_command([])

    def do_exit(self, arg):
        """Exit the interactive shell."""
        print("Exiting the shell. Goodbye!")
        return True

    def default(self, line):
        """Handle unknown commands."""
        print(f"Unknown command: {line}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    # Start the interactive shell
    InteractiveShell().cmdloop()
