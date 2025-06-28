
class DreamCoinManager:
    def __init__(self):
        self.balance = 100

    def deduct(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def add(self, amount):
        self.balance += amount
