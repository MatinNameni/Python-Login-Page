import os
import tkinter as tk

class File:
    def save(data: list):
        with open('users.txt', 'w') as file:
            file.write(str(data))

    def load():
        if os.path.isfile('users.txt'):
            with open('users.txt', 'r') as file:
                data = file.readlines()
                return eval(data[0])
        else:
            return []


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def add_user(self):
        new_user = {
            'username': self.username,
            'password': self.password
        }
        users = File.load()
        users.append(new_user)
        File.save(users)

    def login_status(self):
        for i in File.load():
            if i['username'] == self.username and i['password'] == self.password:
                return 1
        return 0

    def signup(self):
        for i in File.load():
            if i['username'] == self.username:
                tk.messagebox.showerror(title="Error", message="This username already exists")
                return 0
        self.add_user()
