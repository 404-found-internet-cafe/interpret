import re

users = [
    {
        "username" : "beansebrrr",
        "age" : 19,
        "email" : "vmcaballero@proton.me",
        "ciphered_key" : "2-27-38-38-45"
    },
    {
        "username" : "nayanuhhhh",
        "age" : 20,
        "email" : "yanuhvillar@tuta.com",
        "ciphered_key" : "12-15-15-15-22-5"
    }
]


def register_user(username, age, email_address, password):

    if username in [u["username"] for u in users]:
        raise BaseException("Username already exists")
    
    if not re.match(r"/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$/", email_address):
        raise BaseException("Email is invalid")
    
    if age < 14:
        raise BaseException("You're too young to create an account")
    
    arr = password.split("")
    arr = list(map(lambda ch: str(ord(ch)), arr))
    ciphered_password = "-".join(arr)

    new_user = {
        "username": username,
        "age": age,
        "email": email_address,
        "ciphered_key": ciphered_password
    }

    users.append(new_user)
    return













def cipher_text(string: str) -> str:
    """Ciphers the text so that A = 1, a = 27, and so on. Separated by a `-` symbol."""
    arr = string.split("")
    arr = list(map(lambda char: str(ord(char)-64), arr))
    ciphered = "-".join(arr)
    return ciphered
