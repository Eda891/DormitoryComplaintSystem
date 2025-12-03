import bcrypt

def get_hashed_password(plain_text_password: str) -> bytes:
    # bcrypt expects bytes, so encode the password
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def check_password(plain_text_password: str, hashed_password: bytes) -> bool:
    # hashed_password must be bytes too
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

