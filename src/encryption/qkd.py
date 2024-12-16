import numpy as np
import random

class QuantumKeyDistribution:
    def __init__(self, num_bits):
        self.num_bits = num_bits
        self.alice_bits = []
        self.bob_bits = []
        self.basis_a = []
        self.basis_b = []
        self.shared_key = []

    def generate_bits(self):
        """Generate random bits for Alice and Bob."""
        self.alice_bits = [random.randint(0, 1) for _ in range(self.num_bits)]
        self.basis_a = [random.randint(0, 1) for _ in range(self.num_bits)]
        self.bob_bits = [None] * self.num_bits
        self.basis_b = [random.randint(0, 1) for _ in range(self.num_bits)]

    def encode_bits(self):
        """Encode Alice's bits using quantum states."""
        encoded_states = []
        for bit, basis in zip(self.alice_bits, self.basis_a):
            if basis == 0:  # Rectilinear basis
                encoded_states.append(0 if bit == 0 else 1)  # |0> or |1>
            else:  # Diagonal basis
                encoded_states.append(np.pi / 4 if bit == 0 else 3 * np.pi / 4)  # |+> or |->
        return encoded_states

    def measure_bits(self, encoded_states):
        """Bob measures the encoded states."""
        for i in range(self.num_bits):
            if self.basis_b[i] == 0:  # Rectilinear basis
                self.bob_bits[i] = 0 if encoded_states[i] < 0.5 else 1
            else:  # Diagonal basis
                self.bob_bits[i] = 0 if encoded_states[i] < np.pi / 2 else 1

    def sift_key(self):
        """Sift the shared key based on matching bases."""
        for i in range(self.num_bits):
            if self.basis_a[i] == self.basis_b[i]:
                self.shared_key.append(self.alice_bits[i])

    def get_shared_key(self):
        """Return the shared key."""
        return self.shared_key

if __name__ == "__main__":
    num_bits = 10
    qkd = QuantumKeyDistribution(num_bits)
    qkd.generate_bits()
    encoded_states = qkd.encode_bits()
    qkd.measure_bits(encoded_states)
    qkd.sift_key()
    print("Shared Key:", qkd.get_shared_key())
