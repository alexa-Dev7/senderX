import json
import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class MessageStorage:
    def __init__(self):
        self.file_path = settings.DATA_FILE

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def save_message(self, sender, receiver, encrypted_msg):
        data = self.load_data()
        key = f"{sender}_{receiver}"
        if key not in data:
            data[key] = []
        data[key].append(encrypted_msg)
        self.save_data(data)