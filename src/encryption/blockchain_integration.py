import hashlib
import json
import requests

class BlockchainIntegration:
    def __init__(self, blockchain_url):
        self.blockchain_url = blockchain_url

    def create_transaction(self, sender, recipient, amount):
        """Create a new transaction."""
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        return transaction

    def sign_transaction(self, transaction, private_key):
        """Sign the transaction with the sender's private key."""
        transaction_string = json.dumps(transaction, sort_keys=True).encode()
        transaction_hash = hashlib.sha256(transaction_string).hexdigest()
        # In practice, use a proper signing method with the private key
        signature = f"signature_of_{transaction_hash}_with_{private_key}"
        transaction['signature'] = signature
        return transaction

    def send_transaction(self, transaction):
        """Send the signed transaction to the blockchain."""
        response = requests.post(f"{self.blockchain_url}/transactions/new", json=transaction)
        return response.json()

if __name__ == "__main__":
    blockchain = BlockchainIntegration("http://localhost:5000")
    transaction = blockchain.create_transaction("Alice", "Bob", 10)
    signed_transaction = blockchain.sign_transaction(transaction, "private_key_placeholder")
    response = blockchain.send_transaction(signed_transaction)
    print("Transaction Response:", response)
