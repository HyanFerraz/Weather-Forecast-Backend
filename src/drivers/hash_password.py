import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(
            password.encode('utf-8'), 
            bcrypt.gensalt()
        ).decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    if bcrypt.checkpw(
            password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        ):
        return True
    else:
        return False