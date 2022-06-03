from distutils.debug import DEBUG
from os import environ as env

HOST = env.get("HOST", "127.0.0.1")
PORT = env.get("PORT", "8899")
DEBUG = env.get("DEBUG", False)