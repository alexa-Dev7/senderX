from sender.utils import encrypt_message_rsa, decrypt_message_rsa

def send_encrypted_message(public_key, message):
    return encrypt_message_rsa(public_key, message)

def receive_encrypted_message(private_key, encrypted_message):
    return decrypt_message_rsa(private_key, encrypted_message)