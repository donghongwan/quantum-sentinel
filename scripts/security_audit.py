import os

def conduct_security_audit(directory):
    """Conduct a basic security audit of a directory."""
    print(f"Conducting security audit on directory: {directory}")

    # Check for sensitive files
    sensitive_files = ['config.json', 'secrets.txt']
    for file in sensitive_files:
        file_path = os.path.join(directory, file)
        if os.path.exists(file_path):
            print(f"Warning: Sensitive file found: {file_path}")

    # Check for file permissions
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            permissions = oct(os.stat(file_path).st_mode)[-3:]
            print(f"File: {file_path}, Permissions: {permissions}")

if __name__ == "__main__":
    directory = "logs"  # Replace with the directory you want to audit
    conduct_security_audit(directory)
