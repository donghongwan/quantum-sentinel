import hashlib
import random

class ZeroKnowledgeProof:
    def __init__(self):
        self.secret = None
        self.challenge = None
        self.response = None

    def generate_secret(self):
        """Generate a random secret."""
        self.secret = random.randint(1, 100)

    def commit(self):
        """Create a commitment to the secret."""
        r = random.randint(1, 100)
        commitment = (self.secret + r) % 101  # Simple commitment scheme
        return commitment, r

    def challenge_response(self, commitment):
        """Generate a challenge and response."""
        self.challenge = random.randint(0, 1)  # 0 or 1
        if self.challenge == 0:
            self.response = self.secret  # Reveal the secret
        else:
            self.response = (self.secret + random.randint(1, 100)) % 101  # Random value

    def verify(self, commitment):
        """Verify the response against the commitment."""
        if self.challenge == 0:
            return (self.response == self.secret)
        else:
            # Check if the response is consistent with the commitment
            return (commitment == (self.response - random.randint(1, 100)) % 101)

if __name__ == "__main__":
    zk_proof = ZeroKnowledgeProof()
    zk_proof.generate_secret()
    commitment, r = zk_proof.commit()
    print("Commitment:", commitment)
    zk_proof.challenge_response(commitment)
    print("Challenge:", zk_proof.challenge)
    print("Response:", zk_proof.response)
    is_valid = zk_proof.verify(commitment)
    print("Is the proof valid?", is_valid)
