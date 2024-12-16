import subprocess

class ScriptExecution:
    def execute_script(self, script_path):
        """Execute a script securely."""
        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
            print("Script executed successfully.")
            print("Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error executing script:", e.stderr)

if __name__ == "__main__":
    # Example usage
    script_executor = ScriptExecution()
    script_executor.execute_script("example_script.py")  # Change to your script path
