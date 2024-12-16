import socket
import ssl

class SecureCommunication:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.context = ssl.create_default_context()

    def create_secure_socket(self):
        """Create a secure socket using SSL."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_sock = self.context.wrap_socket(sock, server_hostname=self.host)
        return secure_sock

    def send_message(self, message):
        """Send a message securely."""
        with self.create_secure_socket() as secure_sock:
            secure_sock.connect((self.host, self.port))
            secure_sock.sendall(message.encode('utf-8'))
            print("Message sent securely.")

    def receive_message(self):
        """Receive a message securely."""
        with self.create_secure_socket() as secure_sock:
            secure_sock.bind((self.host, self.port))
            secure_sock.listen(1)
            print("Waiting for a secure connection...")
            conn, addr = secure_sock.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print("Received message:", data.decode('utf-8'))

if __name__ == "__main__":
    # Example usage
    host = 'localhost'
    port = 65432

    # To send a message
    sc = SecureCommunication(host, port)
    sc.send_message("Hello, secure world!")

    # To receive a message, run this in a separate terminal
    # sc.receive_message()
