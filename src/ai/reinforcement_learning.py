import numpy as np

class ReinforcementLearning:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_prob=1.0, exploration_decay=0.99):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.exploration_decay = exploration_decay
        self.q_table = {}

    def get_q_value(self, state, action):
        """Get the Q-value for a given state and action."""
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        """Update the Q-value based on the action taken and the reward received."""
        best_next_q = max(self.get_q_value(next_state, a) for a in self.actions)
        current_q = self.get_q_value(state, action)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * best_next_q - current_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, state):
        """Choose an action based on the exploration-exploitation trade-off."""
        if np.random.rand() < self.exploration_prob:
            return np.random.choice(self.actions)  # Explore
        else:
            q_values = [self.get_q_value(state, a) for a in self.actions]
            return self.actions[np.argmax(q_values)]  # Exploit

    def decay_exploration(self):
        """Decay the exploration probability."""
        self.exploration_prob *= self.exploration_decay

if __name__ == "__main__":
    # Example usage
    actions = ['block', 'allow', 'alert']
    rl_agent = ReinforcementLearning(actions)

    # Simulate a simple environment
    for episode in range(100):
        state = 'normal'  # Example state
        action = rl_agent.choose_action(state)
        reward = 1 if action == 'allow' else -1  # Simple reward structure
        next_state = 'normal'  # In a real scenario, this would change based on the action taken
        rl_agent.update_q_value(state, action, reward, next_state)
        rl_agent.decay_exploration()

    print("Q-Table:", rl_agent.q_table)
