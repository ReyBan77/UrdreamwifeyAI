
def capture_email(email, storage):
    if "@" in email:
        storage.append(email)
        return True
    return False
