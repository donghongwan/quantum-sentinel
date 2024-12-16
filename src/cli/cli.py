import sys
from commands import CommandHandler

def main():
    """Main entry point for the CLI."""
    command_handler = CommandHandler()
    
    if len(sys.argv) < 2:
        print("Usage: cli.py <command> [options]")
        sys.exit(1)

    command = sys.argv[1]
    options = sys.argv[2:]

    command_handler.execute(command, options)

if __name__ == "__main__":
    main()
