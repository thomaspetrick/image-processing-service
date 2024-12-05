import bcrypt

def create_password(password: str):

    password_bytes = password.encode('utf-8')

    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed, salt 
    
def verify_password(password: str, hashed_password: str, salt: str):
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, salt) == hashed_password