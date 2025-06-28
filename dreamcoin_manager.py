# dreamcoin_manager.py

import os
import json

COIN_STORAGE_FILE = "dreamcoins.json"

def load_dreamcoins():
    if os.path.exists(COIN_STORAGE_FILE):
        with open(COIN_STORAGE_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_dreamcoins(data):
    with open(COIN_STORAGE_FILE, "w") as f:
        json.dump(data, f)

def get_dreamcoin_balance(user_id):
    coins = load_dreamcoins()
    return coins.get(user_id, 100)  # default 100 coins

def update_dreamcoin_balance(user_id, amount):
    coins = load_dreamcoins()
    coins[user_id] = coins.get(user_id, 100) + amount
    save_dreamcoins(coins)
    return coins[user_id]
