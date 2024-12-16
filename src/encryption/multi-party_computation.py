import random

class MultiPartyComputation:
    def __init__(self):
        self.secret_shares = []

    def share_secret(self, secret, num_parties):
        """Share a secret among multiple parties using additive secret sharing."""
        shares = [random.randint(1, 100) for _ in range(num_parties - 1)]
        last_share = secret - sum(shares)
        shares.append(last_share)
        self.secret_shares = shares
        return shares

    def reconstruct_secret(self):
        """Reconstruct the secret from the shares."""
        return sum(self.secret_shares)

if __name__ == "__main__":
    mpc = MultiPartyComputation()
    secret = 100
    num_parties = 5
    shares = mpc.share_secret(secret, num_parties)
    print("Secret Shares:", shares)
    reconstructed_secret = mpc.reconstruct_secret()
    print("Reconstructed Secret:", reconstructed_secret)
