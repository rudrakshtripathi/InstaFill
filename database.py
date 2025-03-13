import sqlite3
from encryption import encrypt, decrypt

def create_table():
    """Creates the credentials table if it does not exist."""
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Call the function to ensure the table exists
create_table()

def save_credentials(email, password):
    """Saves encrypted credentials to the database."""
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()

    # Encrypt email and password
    encrypted_email = encrypt(email)
    encrypted_password = encrypt(password)

    # Ensure the table exists before inserting data
    create_table()

    # Delete old credentials to store only one set of credentials
    cursor.execute("DELETE FROM credentials")
    cursor.execute("INSERT INTO credentials (email, password) VALUES (?, ?)", (encrypted_email, encrypted_password))
    conn.commit()
    conn.close()

def save_credentials(email, password):
    """Encrypts and saves credentials in the database."""
    conn = sqlite3.connect("data/credentials.db")
    cursor = conn.cursor()
    encrypted_email = encrypt(email)
    encrypted_password = encrypt(password)
    create_table()
    cursor.execute("DELETE FROM credentials")  # Ensure only one credential is stored
    cursor.execute("INSERT INTO credentials (email, password) VALUES (?, ?)", (encrypted_email, encrypted_password))
    conn.commit()
    conn.close()

def get_credentials():
    """Retrieves and decrypts stored credentials."""
    conn = sqlite3.connect("data/credentials.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM credentials LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    if result:
        return decrypt(result[0]), decrypt(result[1])
    return None, None
