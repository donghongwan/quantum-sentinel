from Crypto.Hash import SHA256, SHA512, MD5

class HashFunctions:
    @staticmethod
    def sha256(data):
        """Compute SHA-256 hash of the input data."""
        hash_object = SHA256.new(data.encode())
        return hash_object.hexdigest()

    @staticmethod
    def sha512(data):
        """Compute SHA-512 hash of the input data."""
        hash_object = SHA512.new(data.encode())
        return hash_object.hexdigest()

    @staticmethod
    def md5(data):
        """Compute MD5 hash of the input data."""
        hash_object = MD5.new(data.encode())
        return hash_object.hexdigest()

if __name__ == "__main__":
    data = "Hello, Quantum Sentinel!"
    print("SHA-256:", HashFunctions.sha256(data))
    print("SHA-512:", HashFunctions.sha512(data))
    print("MD5:", HashFunctions.md5(data))
