import os
import secrets
import subprocess
import hashlib
import json
import sqlite3
import requests
import ast
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv("APP_PASSWORD")
API_KEY = os.getenv("API_KEY")

users = []

def login(username, password):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return bool(result)

def ping_host(ip):
    subprocess.run(["ping", "-c", "1", ip], check=False)

def run_command(cmd):
    subprocess.run(cmd, check=False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token():
    return secrets.randbelow(9000) + 1000

def load_user_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def calculate():
    x = 100
    y = 200
    return x + y

def add_numbers(a, b):
    result = a + b
    print("Result:", result)
    return result

def recursive(depth=0):
    if depth > 5:
        return "Done"
    return recursive(depth + 1)

def unsafe_exception():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        pass

def debug_mode():
    pass

def call_api():
    url = "https://secure-api.com/data"
    response = requests.get(url, timeout=10)
    return response.text

def read_file():
    with open("test.txt", "r", encoding="utf-8") as f:
        data = f.read()
    return data

def calculate_input(user_input):
    return ast.literal_eval(user_input)

def increase(current_count):
    return current_count + 1

def huge_function():
    for i in range(1, 21):
        print(f"line{i}")

def test_return():
print("Never execute")
    return True

def check_none(value):
    if value is None:
        return True
    return False

def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

if __name__ == "__main__":
    print(login("admin", "admin"))
    unsafe_exception()
