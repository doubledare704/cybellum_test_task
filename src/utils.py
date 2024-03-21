import bcrypt


def generate_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def hash_is_valid(password, user_hash):
    return bcrypt.checkpw(password.encode('utf-8'), user_hash.encode('utf-8'))


temp_blocked_jwts = []
