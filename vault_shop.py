
def unlock_nsfw(dreamcoin_manager, cost=200):
    if dreamcoin_manager.deduct(cost):
        return True
    return False
